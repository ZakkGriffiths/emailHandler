
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
