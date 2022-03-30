# George Papadopoulos - gip200@nyu.edu

LAB 2, Part 2
-------------

## Task 5 (10pts): Continuous Integration and Development

**Now that we have automated the ability to identify weaknesses in the application, we want to make sure there are no regressions in future developments.
Using GitHub Actions, automate the execution of the four automated vulnerability testing scripts you created in tasks 1 through 4.*
-   `<NetID>-xss.py`
-   `<NetID>-csrf.py`
-   `<NetID>-sqli.py`
-   `<NetID>-cmdi.py`
*The resulting GitHub Actions log should show an individual log - with a checkbox - for each test, each of which should be able to be expanded to show the result of the selected test (a la  `Vulnerable to ...!`  or  `Not vulnerable to ...!`)
Ensure your final workflow file is saved to your repository, in  `.github/workflows/<NetID>-regression.yml`.**

	The process of setting up a workflow requires the creation of a yaml file that calls the appropriate scripts from the root directory of the repository and completes the runtime tasks and reporting for each stage.



# Task 6 (18pts): Encrypting the Database

The web application's back-end database contains valuable gift card data. If a threat actor gains unauthorized access to the gift card data, they can use it to obtain free merchandise, or even pay off their tuition with the NYU tuition gift cards.

***Task 6.a:**  Implement database encryption controls to ensure a compromised gift card entry in the database is not immediately usable without decryption or cracking techniques. Using the  `django-cryptography`  library, encrypt all of the sensitive fields in the  `Cards`  table. Once complete, take a screenshot of the  `Cards`  table, showing the encrypted field values. Finally, demonstrate that the application still works by purchasing and using a gift card after the encryption is in place.*

Could not get this to work as expected.

For the DB encryption, using django-cryptography, we need to invoke the the library and following, as per documentation:

    ##generate encryption key
    ./manage.py generate_encryption_key
    #update installed apps in settings file with
    ```INSTALLED_APPS = (
    ...
    'encrypted_model_fields',)
   
   And subsquently apply Encrypted fields in the models.py field.

    from encrypted_model_fields.fields import EncryptedCharField
    
    class EncryptedFieldModel(models.Model):
        encrypted_char_field = EncryptedCharField(max_length=100)





***Task 6.b:**  *Assume that you have recently discovered that the decryption key for your database encryption has been compromised. Document the process for rotating your encryption key, and then show a screenshot of your  `Cards`  table again, showing the encrypted field values. Describe technically specific precautions you can take in the future to mitigate unauthorized access to your symmetric key.*

As per the documentation for django-encrypted-model-fields, we can leverage a FIELD_ENCRYPTION_KEY from the os environment

import os

FIELD_ENCRYPTION_KEY = os.environ.get('FIELD_ENCRYPTION_KEY', '')

To rotate the key, we could easily write a CRON task with permissions outside the context of django to roll the key periodically, and restart/HUP django.


## END OF LAB 2, Part 2 SUBMISSION

