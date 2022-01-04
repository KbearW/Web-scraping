Extract Data from IRS website:

A bot using Python with BeautifulSoup that scrapes the IRS website (prior form publication) by form number and returns the results as json and downloads a copy of the prospective pdf into a folder if the user chooses to.

How to run the script:

This script runs on Python 3.8. Install the libraries on requirements.txt into a new environment, then run 'Script.py'.

The script will ask you for a form number then scrap the IRS website.

Please separate the tax form number by a comma follow by a space, such as:

--> Form W-2, Form 1095-C

The results will be returned as a json string. If there are no results, you'll get a 'No results' message instead.

Sample output: 
[{'form_number': 'Form W-2',
  'form_title': 'Wage and Tax Statement (Info Copy Only)',
  'max_year': '2022',
  'min_year': '1954'},
 {'form_number': 'Form 1095-C',
  'form_title': 'Employer-Provided Health Insurance Offer and Coverage',
  'max_year': '2022',
  'min_year': '2014'}]

Note: To keep users engaged, the bot will display which task it is performing and what URL it is currently searching.

