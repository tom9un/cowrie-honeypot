# Copyright (c) 2019 Nuno Novais <nuno@noais.me>
# All rights reserved.
# All rights given to Cowrie project

"""
This module contains the chpasswd commnad
"""

from __future__ import absolute_import, division

import getopt

from twisted.python import log

from cowrie.shell.command import HoneyPotCommand

commands = {}


class command_chpasswd(HoneyPotCommand):

    def help(self):
        output = (
            'Usage: chpasswd [options]',
            '',
            'Options:',
            '  -c, --crypt-method METHOD     the crypt method (one of NONE DES MD5 SHA256 SHA512)',
            '  -e, --encrypted               supplied passwords are encrypted',
            '  -h, --help                    display this help message and exit',
            '  -m, --md5                     encrypt the clear text password using',
            '                                the MD5 algorithm'
            '  -R, --root CHROOT_DIR         directory to chroot into'
            '  -s, --sha-rounds              number of SHA rounds for the SHA*'
            '                                crypt algorithms'
        )
        for l in output:
            self.write(l + '\n')

    def chpasswd_application(self, contents):
        c = 1
        try:
            for line in contents.split(b'\n'):
                if len(line):
                    u, p = line.split(b':')
                    if not len(p):
                        self.write('chpasswd: line {}: missing new password\n'.format(c))
                    else:
                        """
                        TODO:
                            - update shadow file
                            - update userDB.txt (???)
                            - updte auth_random.json (if in use)
                        """
                        pass
                c += 1
        except Exception:
            self.write('chpasswd: line {}: missing new password\n'.format(c))

    def start(self):
        try:
            opts, args = getopt.getopt(self.args, 'c:ehmr:s:',
                                       ['crypt-method', 'encrypted', 'help', 'md5', 'root', 'sha-rounds'])
        except getopt.GetoptError:
            self.help()
            self.exit()
            return

        # Parse options
        for o, a in opts:
            if o in "-h":
                self.help()
                self.exit()
                return
            elif o in "-c":
                if args not in ["NONE", "DES", "MD5", "SHA256", "SHA512"]:
                    self.errorWrite("chpasswd: unsupported crypt method: {}\n".format(a))
                    self.help()
                    self.exit()

        if not self.input_data:
            pass
        else:
            self.chpasswd_application(self.input_data)
            self.exit()
            return

    def lineReceived(self, line):
        log.msg(eventid='cowrie.command.input',
                realm='chpasswd',
                input=line,
                format='INPUT (%(realm)s): %(input)s')
        self.chpasswd_application(line.encode())

    def handle_CTRL_D(self):
        self.exit()


commands['/usr/sbin/chpasswd'] = command_chpasswd
commands['chpasswd'] = command_chpasswd
