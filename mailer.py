import smtplib
import secrets

# definiuje dane potrzebne do wysylania maili
adresat = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

# tworze instancje silnika pocztowego
mailer = smtplib.SMTP('smtp.gmail.com', 587)
# witam sie z serwerem
mailer.ehlo()
# szyfruje polaczenie z serwerem
mailer.starttls()
# loguje sie do swojego konta
mailer.login(nadawca, haslo)

temat = 'Subject: Hello from Arek in Python\n'
wiadomosc = 'To jest wiadomosc z pythona'
tresc_wiadomosc = temat + wiadomosc

# wysylam wiadomosc
mailer.sendmail(nadawca, adresat, tresc_wiadomosc)
print('Wyslano maila')
# koncze prace silnika pocztowego
mailer.quit()
