#!/usr/bin/env python3
import sys
import signal
import secrets
from datetime import datetime as dt
import hackchat

print('log bot for hack.chat')

def logMessage(chat, message, user):
    log = '%s | %-16s > %s' % (dt.now().isoformat(' ', 'seconds'), user, message)
    print(log)
    with open(logfile, 'a+') as file:
        file.write(log + '\n')

def logJoin(chat, user):
    log = '%s | %-16s * joined' % (dt.now().isoformat(' ', 'seconds'), user)
    print(log)
    with open(logfile, 'a+') as file:
        file.write(log + '\n')

def logLeave(chat, user):
    log = '%s | %-16s * left' % (dt.now().isoformat(' ', 'seconds'), user)
    print(log)
    with open(logfile, 'a+') as file:
        file.write(log + '\n')

def signal_handler(sig, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if(len(sys.argv) != 3):
    print('usage: python hack.log.py CHATROOM LOGFILE')
    sys.exit(1)

room = sys.argv[1]
logfile = sys.argv[2]

# use random nick, since duplicates are not allowed to join
nick = 'h3lferlein_' + secrets.token_hex(2)
print('joining as: ' + nick)

print('running...')
chat = hackchat.HackChat(nick, room)
chat.on_message += [logMessage]
chat.on_join += [logJoin]
chat.on_leave += [logLeave]
chat.run()
