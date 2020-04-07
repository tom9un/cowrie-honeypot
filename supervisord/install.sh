#!/bin/bash

DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

([ -d /etc/supervisor ] || mkdir /etc/supervisor) && \
([ -d /etc/supervisor/conf.d ] || mkdir /etc/supervisor/conf.d) && \
([ -d /var/log/supervisor ] || mkdir /var/log/supervisor) && \
cp $DIR/supervisord-default /etc/default/supervisord && \
cp $DIR/supervisord.conf /etc/supervisor/supervisord.conf && \
cp $DIR/supervisord /etc/init.d/supervisord && \
ln -s /etc/supervisor/supervisord.conf /etc/supervisord.conf && \
chmod +x /etc/init.d/supervisord && \
update-rc.d supervisord defaults
