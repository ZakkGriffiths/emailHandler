import imaplib, ConfigParser, os

def open_connection(verbose=False):
    # Read config file
    config = ConfigParser.ConfigParser()
    config.read([os.path.expanduser('~/.zakkGmailConfig.ini')])

    # Connect to server -- NOTE: .ini fields are CASE-sensitive
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

