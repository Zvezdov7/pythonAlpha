import sys
import imaplib
import getpass
import email
import datetime

M = imaplib.IMAP4_SSL('imap.mail.ru')
try:
    M.login("login", "pass")
except imaplib.IMAP4.error:
    print("Fail")
rv, mailbox = M.list()
if rv == 'OK':
    print("Mailboxes:")
    print(mailbox)

M.select()
typ, data = M.search(None, 'ALL')
ids = data[0]
id_list = ids.split()
print(len(id_list))
M.close()
M.logout()
