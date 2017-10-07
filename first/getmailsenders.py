import imaplib
import sys
import email
import re
import quopri



#FOLDER=sys.argv[1]
FOLDER=''
LOGIN='@.ru'
PASSWORD=''
IMAP_HOST = 'imap..'  # Change this according to your provider

email_list = []
email_unique = []

mail = imaplib.IMAP4_SSL(IMAP_HOST)
mail.login(LOGIN, PASSWORD)
mail.select()

result, data = mail.search(None, 'ALL')
ids = data[0]
id_list = ids.split()
for i in id_list:
    typ, data = mail.fetch(i,'(RFC822)')
    # print('Message %s\n%s\n' % (i, data[0][1]))
    for response_part in data:
        if isinstance(response_part, tuple):
            # msg = email.message_from_string(response_part[1])
            msg = email.message_from_bytes(response_part[1])
            # msg = email.message_from_string(quopri.decodestring(response_part[1]).decode('utf-8'))
            print(msg['From'])
            # sender = msg['from'].split()[-1]
            # address = re.sub(r'[<>]','',sender)
# Ignore any occurences of own email address and add to list
    # if not re.search(r'' + re.escape(LOGIN),address) and not address in email_list:
    #     email_list.append(address)
    #     print(address)