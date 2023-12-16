from email import encoders
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import os

def sending(student, me, msg, server):
    try:
        os.system("cls || clear")
        print(f'Email sending to {student[3]}')
        server.sendmail(me, student[3], msg.as_string())
        print(f'Email sent to {student[3]}')
    except Exception as e:
        print(f"Error: {e}")

def sendCertiToMail(student, me, server):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "From Scaler"
    msg["From"] = me
    msg["To"] = student[3]
    text = MIMEText(f"Hey {student[2]}!\nCongratulations. Here is your certificate.")
    msg.attach(text)
    # attachment
    f = student[5]
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(f,"rb").read() )
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)
    # attachment ends here
    sending(student, me, msg, server)
    


