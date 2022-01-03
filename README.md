Extract Data from the IRS website
A bot using Python with BeautifulSoup that scraps IRS website (prior form publication) by form number and returns the results as json. It provides the option to download pdfs over a range of years.

How to run the script?
This script runs on Python 3.8. Install the libraries on requirements.txt into a new environment, then run 'Script.py'.

What should I expect?
The script will ask you for the form number(s) then scrap the IRS website.
--> Please enter the complete tax form number separated by a comma followed by a space (not case sensitive): 
    (ie. Form W-2, Form 1095-C, Form W-3, etc)
    --> Form W-2, Form 1095-C

Then the bot will ask if the user would like to download the forms.
--> Would you like to download all related pdfs? (Y/N)

If selected, the bot will follow up by asking a year range.
--> Please provide the year range by using a dash in between the years (starting year must be smaller than ending year): (ie. 2018-2020)

Once executed, the bot will automatically create a folder and download the relevant pdfs into the folder. 

Finally, the results will be returned as a json string. If there are no results, the user will get a 'No results' instead.

Sample output: 
[ 
    {'form_number': 'Form W-2', 'form_title': 'Wage and Tax Statement (Info Copy Only)', 'min_year': '1954', 'max_year': '2022'}, 
    {'form_number': 'Form 1095-C', 'form_title': 'Employer-Provided Health Insurance Offer and Coverage', 'min_year': '2014', 'max_year': '2022'}, {'form_number': 'Form W-3', 'form_title': 'Transmittal of Wage and Tax Statements (Info Copy Only)', 'min_year': '1990', 'max_year': '2022'} 
]

Note: To keep users engaged, the bot will display which task it is performing and what URL it is currently searching.

