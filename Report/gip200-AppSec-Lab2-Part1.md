# George Papadopoulos - gip200@nyu.edu

LAB 2, Part 1
-------------

## Task 1 (18pts): Cross-Site Scripting (XSS)


Learn about XSS here:  [https://portswigger.net/web-security/cross-site-scripting](https://portswigger.net/web-security/cross-site-scripting)

Find a GET or POST parameter that is vulnerable to reflected cross-site scripting vulnerability.

**Task 1.a:**  Describe the technique(s) used to find and confirm the presence of the vulnerability. As a proof-of-concept exploit, log into the website and submit a JavaScript payload that generates an alert box containing the authenticated user's cookie data. Include screenshots of exploitation and snippets of relevant, vulnerable source code.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task1a.jpg?raw=true)

**Task 1.b:**  Using the Python  `requests`  library, write script that will check for the presence of the vulnerability. The script should send an HTTP request to the web server with a payload that triggers the vulnerability, and then it should parse the web server's response for any indication that the vulnerability was successfully exploited. If the the vulnerability is present, the script should simply print "Vulnerable to XSS!" Save the file as  `<NetID>-xss.py`  in the root of your repository. Run the script and show its output.

> **Remember!**  Your script will first need to perform a login task to create a session if the vulnerability is only exploitable while logged in.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task1b.jpg?raw=true)


**Task 1.c:**  Modify the source code to mitigate the vulnerability identified. Describe the modifications, including specific source code snippets and related filenames affected, and describe why they are effective against the weakness. Do not remove the reflected value; santize the input.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task1c.jpg?raw=true)



**Task 1.d**  Update  `<NetID>-xss.py`  and modify the output to conditionally print "Not vulnerable to XSS!" if the vulnerability is not successfully exploited. Run the script and show its output.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task1d.jpg?raw=true)




## Task 2 (18pts): Cross-Site Request Forgery (CSRF)

Learn about CSRF here:  [https://portswigger.net/web-security/csrf](https://portswigger.net/web-security/csrf).

Register two (2) distinct user accounts on the web application, one to serve as the target user (-target) and one to serve as the attacking user (-threat). Find a feature that allows users to send a gift card to another user, and confirm that the feature can successfully send a gift card between the two accounts (using one regular browser and one InPrivate/Incognito browser - one for each user - is a good technique for logging into the application with two different users).

**Task 2.a:**  Describe the technique(s) used to find and confirm the presence of the vulnerability. As a proof-of-concept exploit, create an HTML exploit that abuses cross-site request forgery to coerce a transfer from the target user to the attacking user. Confirm the exploit works by executing the exploit in the target user's browser, and then verifying receipt of the gift card in the attacking user's browser.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task2a.jpg?raw=true)


**Task 2.b:**  Using the Python  `requests`  library, write script that will check for the  **potential**  presence of the vulnerability. Due to the nature of CSRF, your approach will be slightly different than that for the XSS vulnerability, and you will check for the presence of a mitigating token. The script should send a routine HTTP request to the affected web resource, and then it should parse the web server's response for the presence of an HTML element containing  `csrfmiddlewaretoken`  within it. If the the mitigating control is not present, the script should simply print "Vulnerable to CSRF!" Save the file as  `<NetID>-csrf.py`  in the root of your repository. Run the script and show its output.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task2b.jpg?raw=true)

**Task 2.c:**  Modify the source code to mitigate the vulnerability identified. Describe the modifications, including specific source code snippets and related filenames affected, and describe why they are effective against the weakness.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task2c.jpg?raw=true)

**Task 2.d**  Update  `<NetID>-csrf.py`  and modify the output to conditionally print "Not vulnerable to CSRF!" if the vulnerability is not successfully exploited. Run the script and show its output. Explain why the technique employed by the script to determine the state of vulnerability may not be ideal.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task2d.jpg?raw=true)


## HeadingTask 3 (18pts): Structured Query Language Injection (SQLi)

Learn about SQLi here:  [https://portswigger.net/web-security/sql-injection](https://portswigger.net/web-security/sql-injection)

The application seems to process gift cards in a way that is vulnerable to SQL injection. Buy a gift card, and open the gift card file. One of the JSON parameters' values within it will ultimately be improperly processed by the application when you use the card.

**Task 3.a:**  Describe the technique(s) used to find and confirm the presence of the vulnerability. As a proof-of-concept exploit, construct an SQLi attack string that will be used as malicious input within the gift card file. Confirm the exploit works by attepting using the card within the application and retrieving the password hash for your own user account as well as the  `administrator`  user account. Include screenshots and ensure to denote the specific field/parameter that was vulnerable, along with the exact attack string used to carry out the attack. Save the malicious gift card file as  `<NetID>-sqli.gftcrd`  in the root of your repository.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task3a.jpg?raw=true)

**Task 3.b:**  Using the Python  `requests`  library, write script that will check for the presence of the vulnerability. The script should send an HTTP request to the web server with a payload that triggers the vulnerability, and then it should parse the web server's response for any indication that the vulnerability was successfully exploited. If the the vulnerability is present, the script should simply print "Vulnerable to SQLi!" Save the file as  `<NetID>-sqli.py`  in the root of your repository. Run the script and show its output.

> **Remember!**  Your script will first need to perform a login task to create a session if the vulnerability is only exploitable while logged in.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task3b.jpg?raw=true)

**Task 3.c:**  Modify the source code to mitigate the vulnerability identified. Describe the modifications, including specific source code snippets and related filenames affected, and describe why they are effective against the weakness.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task3c.jpg?raw=true)

**Task 3.d**  Update  `<NetID>-sqli.py`  and modify the output to conditionally print "Not vulnerable to SQLi!" if the vulnerability is not successfully exploited. Run the script and show its output.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task3d.jpg?raw=true)

## HeadingTask 4 (18pts): Command Injection (SQLi)

Learn about command injection here:  [https://portswigger.net/web-security/os-command-injection](https://portswigger.net/web-security/os-command-injection)

The  `useCard`  resource also appears to be vulnerable to an arbitrary command injection vulnerability whenever a gift card file is used that contains an invalid JSON structure. Review the  `extras.py`  and  `views.py`  to determine the vulnerable parameter.

**Task 4.a:**  Describe the technique(s) used to find and confirm the presence of the vulnerability. As a proof-of-concept exploit, capture an HTTP request while using a gift card, and then modify the request to execute arbitrary commands by abusing the vulnerable parameter. Confirm the exploit works by reviewing the command terminal where you launched the  `runserver`  command earlier. If successful, you should see your command output among the logs (`ls -la`  is a good command to inject that will be easily visible).

Use the reverse shell technique in the last section of Lab 1 to inject a command to obtain a reverse shell on the web server. Once established, execute the the following command:

```
hostname; date; id;

```

Include screenshots and ensure to denote the specific field/parameter that was vulnerable, along with the exact attack string used to carry out the attack. Also be sure your screenshot of the command above includes the netcat command that was used to set up the listener for the reverse shell. Save the malicious gift card file as  `<NetID>-sqli.gftcrd`  in the root of your repository.

_Note._  For this proof-of-concept, you are likely obtaining a reverse shell on the same system as the web server is running. Adjust the IP address accordingly. Additionally, you may need to wrap your injected command as an argument to  `bash`  (a la  `bash -c "echo Command Injection!"`) if you see errors similar to  `sh: 1: cannot create . . . Directory nonexistent`, indicating execution within a shell that may not support the command.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task4a.jpg?raw=true)



**Task 4.b:**  Using the Python  `requests`  library, write script that will check for the presence of the vulnerability. The script should send an HTTP request to the web server with a payload that triggers the vulnerability, and then it should parse the web server's response for any indication that the vulnerability was successfully exploited. If the the vulnerability is present, the script should simply print "Vulnerable to CMDi!" Save the file as  `<NetID>-cmdi.py`  in the root of your repository. Run the script and show its output.

> **Remember!**  Your script will first need to perform a login task to create a session if the vulnerability is only exploitable while logged in.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task4b.jpg?raw=true)


**Task 4.c:**  Modify the source code to mitigate the vulnerability identified. Describe the modifications, including specific source code snippets and related filenames affected, and describe why they are effective against the weakness.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task4c.jpg?raw=true)

**Task 4.d**  Update  `<NetID>-cmdi.py`  and modify the output to conditionally print "Not vulnerable to CMDi!" if the vulnerability is not successfully exploited. Run the script and show its output.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task4c.jpg?raw=true)

# Part 2: Automated Regression & Database Encryption

With several vulnerbailities identified, exploited, and mitigated, we can focus on stepping up the security maturity of our application stack - from development automation to database storage.


## Task 5 (10pts): Continuous Integration and Development

----------

Now that we have automated the ability to identify weaknesses in the application, we want to make sure there are no regressions in future developments.

Using GitHub Actions, automate the execution of the four automated vulnerability testing scripts you created in tasks 1 through 4.

-   `<NetID>-xss.py`
-   `<NetID>-csrf.py`
-   `<NetID>-sqli.py`
-   `<NetID>-cmdi.py`

The resulting GitHub Actions log should show an individual log - with a checkbox - for each test, each of which should be able to be expanded to show the result of the selected test (a la  `Vulnerable to ...!`  or  `Not vulnerable to ...!`)

Ensure your final workflow file is saved to your repository, in  `.github/workflows/<NetID>-regression.yml`.

You can learn about GitHub Actions at  [https://docs.github.com/en/actions/learn-github-actions](https://docs.github.com/en/actions/learn-github-actions).

## [](https://github.com/gip200/gip200-appsec2#task-6-18pts-encrypting-the-database)Task 6 (18pts): Encrypting the Database

----------

The web application's back-end database contains valuable gift card data. If a threat actor gains unauthorized access to the gift card data, they can use it to obtain free merchandise, or even pay off their tuition with the NYU tuition gift cards.

**Task 6.a:**  Implement database encryption controls to ensure a compromised gift card entry in the database is not immediately usable without decryption or cracking techniques. Using the  `django-cryptography`  library, encrypt all of the sensitive fields in the  `Cards`  table. Once complete, take a screenshot of the  `Cards`  table, showing the encrypted field values. Finally, demonstrate that the application still works by purchasing and using a gift card after the encryption is in place.

**Task 6.b:**  Assume that you have recently discovered that the decryption key for your database encryption has been compromised. Document the process for rotating your encryption key, and then show a screenshot of your  `Cards`  table again, showing the encrypted field values. Describe technically specific precautions you can take in the future to mitigate unauthorized access to your symmetric key.

## END OF LAB 2, Part 1 SUBMISSION
