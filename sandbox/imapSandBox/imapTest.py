#!/usr/bin/env python

import imaplib, re
from pprint import pprint
from connecting import open_connection

list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')

def parse_list_response(line):
    flags, delimiter, mailbox = list_reponse_pattern.match(line).groups()
    mailbox = mailbox.strip('"')
    return (flags, delimiter, mailbox)


if __name__ == '__main__':
    c = open_connection()
    try:
        print; print 'OPEN CONNECTION'
        print 'Connection:', c
        
        print; print 'LIST MAILBOXES'
        typ, mailbox_data = c.list()
        print 'Response code:', typ
        print 'Response:'
        pprint(mailbox_data)
    
    except Exception, e:
        print "Didn't work."
        print e

    finally:
        c.logout()

    for line in mailbox_data:
        print 'Server response:', line
        flags, delimiter, mailbox = parse_list_response(line)
        print 'Parsed response:', (flags, delimiter, mailbox)
