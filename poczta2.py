import smtplib
import secrets
from email.mime.text import MIMEText

# dane nizbedne do wyslania maila
odbiorca = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

temat = 'Hello znowu z Pythona Arek'
tresc = 'To jest wiadomość z polskimi znakami óóóó'

# wiadomosc w formacie MIME, okreslam kodowanie na utf8
# dzieki temu moge wysylac polskie znaki
wiadomosc = MIMEText(tresc,_charset='utf-8')
wiadomosc['Subject'] = temat
wiadomosc['From'] = nadawca
wiadomosc['To'] = odbiorca

# nawiazuje polaczenie z serwerem, autoryzacja i wysylam maila
mailer = smtplib.SMTP('smtp.gmail.com', 587)
mailer.ehlo()
mailer.starttls()
mailer.login(nadawca, haslo)
mailer.sendmail(nadawca, odbiorca, wiadomosc.as_string())

print('Wyslano maila')
mailer.close()








