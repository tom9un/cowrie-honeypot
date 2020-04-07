# Copyright (c) 2019 Nuno Novais <nuno@noais.me>
# All rights reserved.
# All rights given to Cowrie project

"""
This module contains the crontab commnad
"""

from __future__ import absolute_import, division

import getopt

from twisted.python import log

from cowrie.shell.command import HoneyPotCommand

commands = {}


class command_crontab(HoneyPotCommand):

    def help(self):
        output = (
            'usage:    crontab [-u user] file',
            '          crontab [-u user] [-i] {-e | -l | -r}',
            '                  (default operation is replace, per 1003.2)',
            '          -e      (edit user\'s crontab)',
            '          -l      (list user\'s crontab)',
            '          -r      (delete user\'s crontab)',
            '          -i      (prompt before deleting user\'s crontab)'
        )
        for l in output:
            self.write(l + '\n')

    def start(self):
        try:
            opts, args = getopt.getopt(self.args, 'u:elri')
        except getopt.GetoptError as err:
            self.write("crontab: invalid option -- \'{0}\'\n".format(err.opt))
            self.write("crontab: usage error: unrecognized option\n")
            self.help()
            self.exit()
            return

        # Parse options
        user = self.protocol.user.avatar.username
        opt = ""
        for o, a in opts:
            if o in "-u":
                user = a
            else:
                opt = o

        if opt == "-e":
            self.write("must be privileged to use {0}\n".format(opt))
            self.exit()
            return
        elif opt in ["-l", "-r", "-i"]:
            self.write("no crontab for {0}\n".format(user))
            self.exit()
            return

        if len(self.args):
            pass

    def lineReceived(self, line):
        log.msg(eventid='cowrie.command.input',
                realm='crontab',
                input=line,
                format='INPUT (%(realm)s): %(input)s')

    def handle_CTRL_D(self):
        self.exit()


commands['/usr/bin/crontab'] = command_crontab
commands['crontab'] = command_crontab
