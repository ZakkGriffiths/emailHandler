#!/usr/bin/env python

import imaplib, re
from connecting import *
from listMail import *
from mailActions import *
from parseCsv import *
from pprint import pprint

print; print 'Starting...'; print

svdir = '/tmp'

def logout(connection):
    print "Logging out..."
    connection.logout()


################## IMPLEMENTATION ################## 
if __name__ == '__main__':
    connection = open_connection(verbose=True)
    try:

#        print; print 'LIST ALL EMAILS:'
#        result, msg_ids = list_all_emails( connection  )

        print; print 'LIST MAILBOXES:'
        mailbox_list = list_mail(connection, verbose=True)

        print; print 'SELECT MAILBOX:'
        selected_mailbox = select_mailbox(connection, verbose=True)
        
        print; print 'SEARCH MAIL:'
        result, msg_ids = search_mail(connection, selected_mailbox, verbose=True)

        print; print 'FETCH MAIL:'
        fetched_mail = fetch_mail(
            connection, msg_ids, selected_mailbox='Work/dev', criteria='ALL', verbose=True)

        close_mailbox(connection)
        logout(connection)
    except Exception, e:
        print "-- Something went wrong --"
        print e

