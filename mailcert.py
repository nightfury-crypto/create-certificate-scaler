from pandas import read_csv
from features.SendMail import sendCertiToMail
import smtplib

if __name__ == "__main__":
    data = read_csv("js-list.csv").values.tolist()
    me = "pradhankarnail@gmail.com"
    app_pass = "pemabogzjcjrbscv"
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(me, app_pass)
        for student in data:
            sendCertiToMail(student, me, server)
        server.quit()
    except Exception as e:
        print("Error", e)
    