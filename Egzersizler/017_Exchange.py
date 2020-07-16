import requests
import sys

url = "http://data.fixer.io/api/latest?access_key=ad56a866ca7a44d2340dd6bcc67a315a&base=EUR&symbols="

print("-------Para Birimi Dönüştürücü-------")
print("Çevirebileceğiniz para birimleri: \n")
print("""AED AFN ALL AMD ANG AOA ARS AUD 
AWG AZN BAM BBD BDT BGN BHD BIF
BMD BND BOB BRL BSD BTC BTN BWP
BYN BYR BZD CAD CDF CHF CLF CLP
CNY COP CRC CUC CUP CVE CZK DJF
DKK DOP DZD EGP ERN ETB EUR FJD
FKP GBP GEL GGP GHS GIP GMD GNF
GTQ GYD HKD HNL HRK HTG HUF IDR
ILS IMP INR IQD IRR ISK JEP JMD
JOD JPY KES KGS KHR KMF KPW KRW
KWD KYD KZT LAK LBP LKR LRD LSL
LTL LVL LYD MAD MDL MGA MKD MMK
MNT MOP MRO MUR MVR MWK MXN MYR
MZN NAD NGN NIO NOK NPR NZD OMR
PAB PEN PGK PHP PKR PLN PYG QAR
RON RSD RUB RWF SAR SBD SCR SDG
SEK SGD SHP SLL SOS SRD STD SVC
SYP SZL THB TJS TMT TND TOP TRY
TTD TWD TZS UAH UGX USD UYU UZS
VEF VND VUV WST XAF XAG XAU XCD
XDR XOF XPF YER ZAR ZMK ZMW ZWL""")

para_birimi1 = input("\nEldeki para birimi: ")
para_birimi2 = input("\nHedef para birimi: ")
miktar = float(input("Miktar: "))

response = requests.get(url)

json_verisi = response.json()

para_birimi1_degeri = json_verisi["rates"][para_birimi1]
para_birimi2_degeri = json_verisi["rates"][para_birimi2]

try:
	print(miktar*para_birimi2_degeri/para_birimi1_degeri)
except KeyError:
	sys.stderr.write("Para birimini yanlış yazdınız, kontrol edin.")
	sys.stderr.flush()
