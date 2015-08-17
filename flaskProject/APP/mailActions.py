import email, re, os

svdir = '/tmp/'

def parse_list_response(line):
    list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')
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
                criteria='(from "Richard Hayes" since "01-Aug-2015")',
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
    #print msg_ids[0]
    msg_ids = msg_ids[0].split()
    #print msg_ids
    return result, msg_ids

def fetch_mail(connection, msg_ids, selected_mailbox='', criteria='', verbose=False):
    # connect.fetch(msg_ids, message_portions)

#    def get_messages(msg_ids):
#        for id in msg_ids[0].split():
#            result, msg_data = c.fetch(id,'(RFC822)')
#            msg = email.message_from_string(msg_data[0][1])
#            result, data = c.store(id,'-FLAGS','\\Seen')
#            yield msg

    basic_fetch = False;
    if verbose:
        if criteria == '':
            print 'No fetch criteria given. Defaulting to basic header fetch.'
            basic_fetch=True
        if selected_mailbox == '':
            print 'No mailbox selected.'
        else:
            print 'Fetching mail from "'+selected_mailbox+'", using criteria:'
            if basic_fetch:
                print '(FROM TO DATE SUBJECT)'
            else:
                print criteria+'...'

    def fetch_basic():
        print "Fetching basic headers..."
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

    if criteria == '':
        fetch_basic()


    # Defaults to fetching 5 latest emails
    fetched_mail_ids = msg_ids[0]
    print 'msg_ids[0] = '+ msg_ids[0]
    fetched_mail_ids = msg_ids[0].split() # ids is a space separated string
    print 'fetched_mail_ids: ', fetched_mail_ids
    for ids in fetched_mail_ids:
        try:
            result, msg_data = connection.fetch(ids,"(RFC822)")
            msg = email.message_from_string(msg_data[0][1])
            # NOTE: fetched_data[0][1] is assumed to be the body

            if msg.get_content_maintype() != 'multipart':
                continue

            for part in msg.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()
                if filename is not None:
                    sv_path = os.path.join(svdir, filename)
                    if not os.path.isfile(sv_path):
                        print sv_path
                        fp = open(sv_path, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()


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

