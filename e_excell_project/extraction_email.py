import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')
#imaplib module implements connection based on IMAPv4 protocol
mail.login(' upfeatemailproject@gmail.com', 'Ouvert2019')
# >> ('OK', [username at gmail.com Vineet authenticated (success)'])
mail.list() #lists all labels in gmail
mail.select('inbox') #connect to inbox


#Fetching the latest emails
result, data = mail.uid('search',None, "ALL") #search and return uids instead

i = len(data[0].split())
for x in range(i):
    latest_email_uid = data[0].split()[x] #get the latest

    result, email_data = mail.uid('fetch',latest_email_uid, '(RFC822)') #Fetch

    raw_email = email_data[0][1] #here's the body, which is raw text of
    #including headers and alternate payloads

raw_email_string = raw_email.decode('utf-8')
#converts byte literal to string removing b''
email_message = email.message_from_string(raw_email_string)
#loop in all the the avail multipart in the emails
for part in email_message.walk():
 if part.get_content_type() == "text/plain": #ignore attachments/html
     body = part.get_payload(decode=True)
     save_string = str("D:Dumpgmailemail_" + str(x) + ".txt")
     #locate on disk
     myfile = open(save_string, 'a')
     myfile.write(body.decode('utf-8'))
     #body is again a byte literal
     myfile.close()
 else:
     continue
