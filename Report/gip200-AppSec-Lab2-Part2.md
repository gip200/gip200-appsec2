# George Papadopoulos - gip200@nyu.edu

LAB 2, Part 2
-------------

## Task 5 (10pts): Continuous Integration and Development


Now that we have automated the ability to identify weaknesses in the application, we want to make sure there are no regressions in future developments.

Using GitHub Actions, automate the execution of the four automated vulnerability testing scripts you created in tasks 1 through 4.

-   `<NetID>-xss.py`
-   `<NetID>-csrf.py`
-   `<NetID>-sqli.py`
-   `<NetID>-cmdi.py`

The resulting GitHub Actions log should show an individual log - with a checkbox - for each test, each of which should be able to be expanded to show the result of the selected test (a la  `Vulnerable to ...!`  or  `Not vulnerable to ...!`)

Ensure your final workflow file is saved to your repository, in  `.github/workflows/<NetID>-regression.yml`.

You can learn about GitHub Actions at  [https://docs.github.com/en/actions/learn-github-actions](https://docs.github.com/en/actions/learn-github-actions).

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task5.jpg?raw=true)


# Task 6 (18pts): Encrypting the Database

The web application's back-end database contains valuable gift card data. If a threat actor gains unauthorized access to the gift card data, they can use it to obtain free merchandise, or even pay off their tuition with the NYU tuition gift cards.

**Task 6.a:**  Implement database encryption controls to ensure a compromised gift card entry in the database is not immediately usable without decryption or cracking techniques. Using the  `django-cryptography`  library, encrypt all of the sensitive fields in the  `Cards`  table. Once complete, take a screenshot of the  `Cards`  table, showing the encrypted field values. Finally, demonstrate that the application still works by purchasing and using a gift card after the encryption is in place.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task6a.jpg?raw=true)

**Task 6.b:**  Assume that you have recently discovered that the decryption key for your database encryption has been compromised. Document the process for rotating your encryption key, and then show a screenshot of your  `Cards`  table again, showing the encrypted field values. Describe technically specific precautions you can take in the future to mitigate unauthorized access to your symmetric key.

![enter image description here](https://github.com/gip200/gip200-appsec1/blob/main/Reports/Artifacts/gip200-lab2task6b.jpg?raw=true)

## END OF LAB 2, Part 2 SUBMISSION
