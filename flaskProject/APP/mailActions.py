import email

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
    print msg_ids
    return result, msg_ids

def fetch_mail(connection, msg_ids, selected_mailbox='', criteria='', verbose=False):
    # connect.fetch(msg_ids, message_portions)
    def fetch_all():
        print "Fetching all..."
        for id in msg_ids:
            try:
                print
                result, msg_data = connection.fetch(id,"(RFC822)")
                print 'Message ID:',id
                msg = email.message_from_string(msg_data[0][1])
                print "From: \t\t"+msg["FROM"]
                print "To: \t\t"+msg["TO"]
                print "Date: \t\t"+msg["DATE"]
                print "Subject: \t"+msg["SUBJECT"]
            except Exception, e:
                print "-- Failed to fetch all --"
                print e

    if verbose:
        if criteria == '':
            print 'No search criteria given.'
        if criteria == 'ALL':
            fetch_all()
        if selected_mailbox == '':
            print 'No mailbox selected.'
        else:
            print 'Fetching mail from "'+selected_mailbox+'"...'
        # TODO



#        for response_part in msg_data:
#            if isinstance(response_part, tuple):
#                print response_part[1]
        

    # Defaults to fetching 5 latest emails
        fetched_mail_ids = search_data[0]
        print 'search_data[0] = '+ search_data[0]
        fetched_mail_ids = ids.split() # ids is a space separated string
        print 'fetched_mail_ids: ', fetched_mail_ids
        for ids in fetched_mail_ids:
            try:
                result, requestedList = mail.fetch(ids,"(RFC822)")
                msg = email.message_from_string(data[0][1])
            except Exception, e:
                print e

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

