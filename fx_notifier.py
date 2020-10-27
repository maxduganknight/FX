from forex_python.converter import CurrencyRates
from argparse import ArgumentParser 
import smtplib, ssl
from creds import gmail_password

'''
This script uses a python library called forex to pull an exchange rate daily and notify someone 
via email if the exchange rate is above a certain threshold. I used this code to help decide when 
to do a foreign currency exchange between USD and GBP.
'''

parser = ArgumentParser()
parser.add_argument('-f', '--first_currency', help = 'currency to convert from', required = True)
parser.add_argument('-s', '--second_currency', help = 'currency to convert to', required = True)
parser.add_argument('-e', '--emails', help = 'email addresses to send notification', required = True)
parser.add_argument('-r', '--rate_threshold', help = 'rate threshold above which script should send email', required = True)


def grab_exchange_rate(first_currency, second_currency):
	c = CurrencyRates()
	rate = round(c.get_rate(first_currency, second_currency), 3)
	return rate

def write_email(first_currency, second_currency, rate_threshold, rate):
	message = """\
	{first_currency}:{second_currency} is {rate}

	You are being notified because the rate is above {rate_threshold}.
	""".format(first_currency = first_currency, second_currency = second_currency, 
		rate = rate, rate_threshold = rate_threshold)
	return message

def send_email(sender_email, receiver_email, message, password):
	port = 465
	password = gmail_password
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login("automate.mdk@gmail.com", password)
		server.sendmail(sender_email, emails, message)
		print("Sent email to {email}".format(email = receiver_email))

if __name__ == "__main__":
	args = parser.parse_args()
	first_currency = args.first_currency
	second_currency = args.second_currency
	emails = args.emails
	rate_threshold = float(args.rate_threshold)
	sender_email = "automate.mdk@gmail.com"
	rate = grab_exchange_rate(first_currency, second_currency)
	if rate > rate_threshold:
		message = write_email(first_currency, second_currency, rate_threshold, rate)
		send_email(sender_email, emails, message, gmail_password)
	else:
		print("Rate did not meet threshold. Not sending an email.")
