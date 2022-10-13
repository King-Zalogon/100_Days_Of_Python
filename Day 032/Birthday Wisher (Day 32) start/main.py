# import smtplib
#
# my_email = "zalogonking@gmail.com"
# password = 'notapassword'
#
# gmail_smtp = 'smtp.gmail.com'
# hotmail_smtp = 'smtp.live.com'
# yahoo_smtp = 'smtp.mail.yahoo.com'
#
# with smtplib.SMTP('smtp.gmail.com', port=587) as connection:  # to connect to de smtp of our mail
#     connection.starttls()  # to encrypt the messages
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="zalogonking@yahoo.com",
#                         msg='Subject: Praise the Omnissiah\n\nThis is the body of my test email using python.')
#     # connection.close()  # always close afterwards if i don't use the "with" method
