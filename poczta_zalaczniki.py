import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

class Poczta(object):

    def __init__(self, login, haslo, server='smtp.gmail.com'):
        """Tworzy serwer pocztowy"""
        self.login = login
        self.haslo = haslo
        self.server = server

    def send_mail(self, send_to, subject, text, files=None):
        """
        Wysyła wiadomość email do użytkownika w formacie utf-8
        :param send_to: Lista odbiorców [str]
        :param subject: Temat wiadomości
        :param text: Tresc wiadomości
        :param files: lista plików do przesłania [str]
        :return: None
        """
        assert isinstance(send_to, list)

        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = COMMASPACE.join(send_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach(MIMEText(text, _charset='utf-8'))

        # tworze zalaczniki
        for f in files or []:
            with open(f, "rb") as fil:
                part = MIMEApplication(fil.read(), Name=basename(f))
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)


        mailer = smtplib.SMTP(self.server, 587)
        mailer.ehlo()
        mailer.starttls()
        mailer.login(self.login, self.haslo)
        mailer.sendmail(self.login, send_to, msg.as_string())
        mailer.close()
        