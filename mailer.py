import smtplib
import secrets

adresat = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

mailer = smtplib.SMTP('smtp.gmail.com', 587)
mailer.ehlo()
mailer.starttls()
mailer.login(nadawca, haslo)

temat = 'Subject: Hello from Arek in Python\n'
wiadomosc = 'To jest wiadomosc z pythona'

tresc_wiadomosc = temat + wiadomosc

mailer.sendmail(nadawca, adresat, tresc_wiadomosc)
print('Wyslano maila')
mailer.quit()
