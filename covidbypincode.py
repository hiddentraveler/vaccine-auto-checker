import requests

user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}
url1 = 'https://www.cowin.gov.in/api/v2/appointment/sessions/public/calendarByPin?pincode=741121&date=02-05-2021'
url2 = 'https://www.cowin.gov.in/api/v2/appointment/sessions/public/calendarByPin?pincode=741502&date=02-05-2021'
url3 = 'https://www.cowin.gov.in/api/v2/appointment/sessions/public/calendarByPin?pincode=741121&date=02-05-2021'
url4 = 'https://www.cowin.gov.in/api/v2/appointment/sessions/public/calendarByPin?pincode=741402&date=02-05-2021'
url5 = 'https://www.cowin.gov.in/api/v2/appointment/sessions/public/calendarByPin?pincode=741505&date=02-05-2021'
url6 = 'https://www.cowin.gov.in/api/v2/appointment/sessions/public/calendarByPin?pincode=741404&date=02-05-2021'
url7 = 'https://www.cowin.gov.in/api/v2/appointment/sessions/public/calendarByPin?pincode=741101&date=02-05-2021'

response1 = requests.get(url1, headers=user_agent)
response2 = requests.get(url2, headers=user_agent)
response3 = requests.get(url3, headers=user_agent)
response4 = requests.get(url4, headers=user_agent)
response5 = requests.get(url5, headers=user_agent)
response6 = requests.get(url6, headers=user_agent)
response7 = requests.get(url7, headers=user_agent)

print(response1.text, response2.text, response3.text, response4.text, response5.text, response6.text, response7.text)
