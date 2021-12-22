# data-representation-project
Jon Ishaque GMIT  G00398244: 

## The Risk Register
This project is a attempt to replicate a MS Access application in my work place with the context of the assigmen brief.

The purpose of the risk register is to allow the director of corporate service to assess risks to organisation activity and put into place control measures and periodically review the risks

Functionality included:
Archiving of risks rather deleting risks(in the context of the assigment, once risks are achived, they can they then be deleted.)
Highlighting risks due for review. The frequency of risk review is determined by the Risk level, this in turn is a function of likelihood and impact of the risk. 

On ids: The applications has a unique id for risks on the database and this used for under the cover access of the risk. However, an addional risk id exists for the application users giving meaning to a risk by number and prefix. This is generated from the risk category. This funcionality relies on 

Because my risks have server side processing, such as rid, frequency etc, and reviewdates the risk register reloads the risks list from the server  after a new risk is added or a risk is updated.

Content
nav-table
CreateUpdateRisks
ListRisks
ListArchiveRisks

JavaScript Functions
showCreate()
showUpdate()
showViewAll()
showArchive()

getRisk(id)

getUpdate(r)
loadRisks()
doUpdate()
doCreate()
doDelete(r)
loadRisks()
loadArchivedRisks()

getCategories()
formatdt(date)

addRisktoTable(risk)
addRiskArchivetoTable(risk)

getRiskFromForm()

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