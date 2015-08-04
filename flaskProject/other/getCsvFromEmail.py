#!/usr/bin/env python

import imaplib, email, os

print "Starting..."

svdir = '/tmp'

mail = imaplib.IMAP4('imap.gmail.com')
mail.login(email_address = raw_input("Input email address:"),
           password = raw_input("Input password"))
mail.select("Inbox")

typ, msgs = mail.search(None, '(SUBJECT "test")')
msgs = msgs[0].split()

for emailid in msgs:
    print "Email "+str(emailid)
    resp, data = mail.fetch(emailid, "(RFC822)")
    email_body = data[0][1] 
    m = email.message_from_string(email_body)


    if m.get_content_maintype() != 'multipart':
        continue

    for part in m.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        filename=part.get_filename()
        if filename is not None:
            sv_path = os.path.join(svdir, filename)
            if not os.path.isfile(sv_path):
                print sv_path       
                fp = open(sv_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()

