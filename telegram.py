import requests

user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}
url = 'https://api.telegram.org/bot1748393244:AAES20VpuN7-WtAfzXPwVXRcBKJLqLdnLsE/sendMessage?chat_id=-589704601&text=something changed check if vaccine is avaliable'

response = requests.get(url, headers=user_agent)
