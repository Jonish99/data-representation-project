# Data-representation-project
Jon Ishaque GMIT  G00398244:
December 2021

## The Risk Register
This project is an attempt to replicate a MS Access application in my work place within the context of the assignment brief.

The purpose of the *Risk Register* is to enable the Director of Corporate Services to assess risks to organisation activity,put into place control measures and periodically review the risks. Access was originally chosen as features of Access made it more suitable to the project. 

### Functionality included:
*Archiving* of risks rather deleting risks(in the context of the assignment, once risks are archived, they can they then be deleted.)

The frequency of risk review is determined by the risk level, this in turn is a function of likelihood and impact of the risk. This then applied to date of last review (default creation date) and the next review date is generated

#### On ids:
The application has a unique id for risks on the database and this is used for under the cover access of the risk. However, an additional risk id (rid) exists for the application users giving meaning to a risk by number and prefix. This is generated from the risk category. 

The risks have some server side processing, such as generate rid, frequency etc, and review dates the risk register reloads the risks list from the server after a new risk is added or a risk is updated, rather copying the risk to the to the main risks or archive tables.

The export risks function has not been implemented. Possibly within scope of the assignment however time did not allow. The intention is to export risks to formatted excel .xlxs files.

The highlighting of due risks has also not been implemented.

Transferring from the Access database raised some observations, for example the look up tables suited the way Access worked. In fact they could be dictionaries in the html file.

As a working model the application is not complete. The plan now is to take this prototype to the project sponsor and work towards an enhanced register, making better use of potential developed in this unit. They are aware that it is coming, and IT Services have agreed to hosting it!. On reflection there should be a health warning with real projects. 

The application the following python libraries:

dateutil - included with Anaconda or:
pip3 install python-dateutil or pip install python-dateutil
datetime is a standard python library
flask is included with Anaconda or:
pip install Flask


To run the application, you must have MySQL on the host machine.
The file tables.sql contains contains SQL commands to:
Create the database
Create tables
and Create Essential content for look up tables.

You will also need to configure a dbconfig.py file
in the following format:

mysql = {
        
        'host':Yourhost,

        'user':yourusername,

        'password':yourpassword,

        'database':'risk_register'

        }



## References:

Codegrepper.com. 2021. js date to string yyyy-mm-dd Code Example. [online] Available at: <https://www.codegrepper.com/code-examples/javascript/js+date+to+string+yyyy-mm-dd> [Accessed 19 December 2021].

GeeksforGeeks. 2021. Switch Case in Python (Replacement) - GeeksforGeeks. [online] Available at: <https://www.geeksforgeeks.org/switch-case-in-python-replacement/> [Accessed 21 December 2021].

Hufford, M., 2021. Delete all rows on a table except first with Javascript. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/16270087/delete-all-rows-on-a-table-except-first-with-javascript> [Accessed 21 December 2021].

Javascript?, H., 2021. How to trim a string to N chars in Javascript?. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/7463658/how-to-trim-a-string-to-n-chars-in-javascript> [Accessed 22 December 2021].

Lu, R., Hewgill, G. and Desanze, M., 2021. How do you find out the caller function in JavaScript?. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/280389/how-do-you-find-out-the-caller-function-in-javascript> [Accessed 19 December 2021].

Meddows, S. and Natraaj, V., 2021. How do I get the current date in JavaScript?. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/1531093/how-do-i-get-the-current-date-in-javascript> [Accessed 22 December 2021].

MySQL, I., 2021. Inserting a Python datetime.datetime object into MySQL. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/1136437/inserting-a-python-datetime-datetime-object-into-mysq> [Accessed 21 December 2021].

Nixon, R., 2018. Learning PHP, MySQL & Javascript: With jQuery, CSS & HTML5. 5th ed. Sebastapol: O'Reilly.

Pieters, M. and Kumar, B., 2021. Flask: How to serve static html?. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/24578330/flask-how-to-serve-static-html> [Accessed 12 December 2021].

Roms, D. and Mhatre, A., 2021. Add css to button. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/47267399/add-css-to-button> [Accessed 20 December 2021].

Stack Abuse. 2021. How to Format Dates in Python. [online] Available at: <https://stackabuse.com/how-to-format-dates-in-python/> [Accessed 22 December 2021].

Stocks, N. and Ragazzi, D., 2021. How do you add "3 months" to a datetime.date object in python?. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/9594282/how-do-you-add-3-months-to-a-datetime-date-object-in-python> [Accessed 22 December 2021].

Thomas, D. and Vidas, Š., 2021. Adding options to select with javascript. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/8674618/adding-options-to-select-with-javascript> [Accessed 20 December 2021].

ラッコツールズ. 2021. MySQL Syntax Checker: Check MySQL syntax error online | RAKKOTOOLS🔧. [online] Available at: <https://en.rakko.tools/tools/36/> [Accessed 22 December 2021].