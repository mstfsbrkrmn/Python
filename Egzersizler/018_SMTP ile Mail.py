import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()
mesaj["From"] = "mstfsbrkrmn@gmail.com"
mesaj["To"] = "m.sabrikaraman@gmail.com"
mesaj["Subject"] = "Smtp ile Mail Gönderme"
yazi="""
Deneme
Test
SMTP ile mail gönderme
Test
DENEME
"""
mesaj_govdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

try:
	mail = smtplib.SMTP("smtp.gmail.com",587)
	mail.ehlo()
	mail.starttls()
	mail.login("","") # mail adresi, şifre
	mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
	print("Mail başarı ile gönderildi.")
	mail.close()
except:
	sys.stderr.write("Bir sorun oluştu.")
	sys.stderr.flush()




