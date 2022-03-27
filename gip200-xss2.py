import requests
with requests.Session() as session:
    session.verify = False
    session.trust_env = False

    session.get(url='http://127.0.0.1/')

    login=session.post(url='http://127.0.0.1/login.html', data={'uname' : 'gip200@nyu.edu', 'pword' : 'aaaaaa'})

    print (login)







    #url = "http://127.0.0.1/gift/0"
    #values = {
    #  "username" : '"<script> alert( "XSS " ) ; </script>"'
    #}
    #req = session.post(url,data=values)
    #print (req.text)

#session = requests.Session()
#session.verify = False
#session.trust_env = False
#req=session.post(url='http://127.0.0.1/login.html', data={'gip200@nyu.edu':'aaaaaa'})
#print (req.text)

