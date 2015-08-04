#!/usr/bin/env python

######## IMPLEMENTATION AT END OF FILE ########

import imaplib, email, ConfigParser, os, re
from pprint import pprint

print; print 'Starting...'; print

svdir = '/tmp'
list_response_pattern = re.compile(
    r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')

def open_connection(verbose=False):
    # Read config file
    config = ConfigParser.ConfigParser()
    config.read([os.path.expanduser('~/.zakkGmailConfig.ini')])

    # Connect to server
    hostname = config.get('Server', 'hostname')
    if verbose: print 'Connecting to', hostname
    connection = imaplib.IMAP4_SSL(hostname)

    # Log in to account
    username = config.get('Account', 'username')
    password = config.get('Account', 'password')
    if verbose: print 'Logging in as ', username
    try:
        connection.login(username, password)
        print "Logged in as %r" % username
    except imaplib.IMAP4.error:
        print "Log in failed."
    return connection

def list_mail(connection, mailbox='', verbose=True):
    # Lists mailboxes (aka "folders", or "labels" in gmail).
    if verbose: print "Getting mailbox list..."
    try:
        result, mailbox_data = connection.list()

        if verbose:
            print; print "Printing mailbox_data, line by line, with re (parser):"
        for line in mailbox_data:
#            print 'Server response:', line
            flags, delimiter, mailbox = parse_list_response(line)
            print mailbox
#            print 'Parsed response:', (flags, delimiter, mailbox)

        mailbox_list = mailbox_data[0]
        return mailbox_list
    except Exception, e:
        print "Couldn't list mailboxes.\nException:"
        print e

def parse_list_response(line):
    flags, delimiter, mailbox = list_response_pattern.match(line).groups()
    mailbox = mailbox.strip('"')
    return (flags, delimiter, mailbox)

def select_mailbox(connection, mailbox='inbox', verbose=False):
    if verbose: print "Selecting mailbox '"+mailbox+"'..."
    # connect to inbox by default.
    result, selection_data = connection.select(mailbox, readonly=True)
    selected_mailbox = mailbox # NOTE NOTE
    num_msgs = int(selection_data[0])
    print "There are %d messages in %s" % (num_msgs, mailbox)
    return selected_mailbox

def search_mail(connection,
                mailbox='',
                criteria='(from "Richard Hayes" since "01-May-2015")',
                verbose=False):
    # TODO -- provide search options; accept string
    
    if mailbox == '':
        print "No mailbox selected."
    # TODO Catch returned Nones

    if verbose: print 'Searching '+mailbox+' with criteria: '+criteria
    result, msg_ids = connection.search(None, criteria)
    if verbose:
        print 'Mailbox:', mailbox
        print 'Message IDs:', msg_ids
    print msg_ids[0]
    msg_ids = msg_ids[0].split()
    return result, msg_ids

def fetch_mail(connection, msg_ids, selected_mailbox='', criteria='', verbose=False):
    # connect.fetch(msg_ids, message_portions)
    if criteria == '':
        print 'No search criteria given.'
    if selected_mailbox == '':
        print 'No mailbox selected.'
    else:
        print 'Fetching mail from "'+selected_mailbox+'"...'
        # TODO

#        result, msg_data = []
        print "#####"
        print msg_ids
        print "#####"
        for id in msg_ids:
            result, msg_data = connection.fetch(id, '(BODY.PEEK[HEADER])')
            print 'ID:',id
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    print response_part[1]
            print; print 'Printing fetched_data['+id+']...'
        
#    # Defaults to fetching 5 latest emails
#    if verbose: print 'Fetching mail...'
#    result, search_data = search_mail(connection, verbose=False)
#    if criteria == '':
#        result, search_data = fetch_latest_emails(connection,search_data, verbose)
#        print "Testing fetch_latest_emails( VERBOSE ) verbose =", verbose
#    print; print 'search_data:'
#    print search_data
#    if search_data[0]:
#        fetched_mail_ids = search_data[0]
#        print 'search_data[0] = '+ search_data[0]
#        fetched_mail_ids = ids.split() # ids is a space separated string
#        print 'fetched_mail_ids: ', fetched_mail_ids
#        for ids in fetched_mail_ids:
#            try:
#                result, requestedList = mail.fetch(ids,"(RFC822)")
#                msg = email.message_from_string(data[0][1])
#                print "From: "
#                print msg["FROM"]
#                print "Subject: "
#                print msg["SUBJECT"]
#                print "Date: "
#                print msg["DATE"]
#                print "Text: "
#                print msg["TEXT"]
#                print
#            except Exception, e:
#                print e

    return msg_data

def fetch_latest_emails(connection, fetched_mail, number=1, verbose=True):
    latest_emails_ids = fetched_mail[-1:-number] # get latest emails

    result, requestedList = connection.fetch(latest_emails_ids, "(RFC822)")
    # fetch the email body (RFC822) for the given ID

    raw_email = data[0][1] # here's the body, which is raw text of the whole email
    # including headers and alternate payloads

    email_message = email.message_from_string(raw_email)

    print (email_message['Subject'])

def close_mailbox(connection, mailbox='inbox'):
    # NOTE Shouldn't this be mailbox.close()?
    connection.close() # close mailbox

def logout(connection):
    print "Logging out..."
    connection.logout()


def list_all_emails( connection ):
    try:
        result, mailbox_data = connection.list()
        for line in mailbox_data:
            flags, delimiter, mailbox = parse_list_response(line)
            
#            print; print 'Selecting '+mailbox+' ...'
            result, selection_data = connection.select(mailbox, readonly=True)
            num_msgs = int(selection_data[0])
            
#            print; print 'Searching '+mailbox+' ...'
            result, msg_ids = connection.search(None, 'ALL')
            if msg_ids[0] == '':
                print 'Mailbox "'+mailbox+'" is empty.'
            else:
                print 'Mailbox "'+mailbox+'" contains '+str(num_msgs)+' emails:'
                print msg_ids
            print
    except Exception, e:
        print "Couldn't list all emails"
        print e

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
            connection, msg_ids, selected_mailbox, verbose=True)

        close_mailbox(connection)
        logout(connection)
    except Exception, e:
        print "-- Something went wrong --"
        print e

