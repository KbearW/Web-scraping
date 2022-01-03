from bs4 import BeautifulSoup
import requests
import os

data = []
year_list = []
result = {
            "form_number": '',
            "form_title": '',
            "min_year": '',
            "max_year": ''
                }

def pdf_download(pdf_url, form_number, year):
    '''download pdfs from IRS website and save in its own folder '''
    
    r = requests.get(pdf_url, stream = True)
    
    try:
        os.mkdir(form_number)
    except: 
        pass 

    with open(f'{form_number}/{form_number} - {year}.pdf',"wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            # writing one chunk at a time to pdf file
            if chunk:
                pdf.write(chunk)


def find(search_url):
    '''Search the search_url for specific elements in all pages.
    The result is part of the final json output. '''

    req = requests.get(search_url)
    if req.status_code == requests.codes.ok:
        # print(f'*****Weblink is working properly!*****')
        soup = BeautifulSoup(req.content, 'html.parser')

        all_rows = soup.findAll("tr")

        for row in all_rows[5:]:
            form_number = row.find(class_="LeftCellSpacer").get_text(strip=True)
            form_title = row.find(class_="MiddleCellSpacer").get_text(strip=True)
            year = row.find(class_= 'EndCellSpacer').get_text(strip=True)
            pdf_url = row.find(class_='LeftCellSpacer').find('a')['href']
            if form_number.lower() == search_item.lower():    
                result["form_number"] = form_number
                result["form_title"] = form_title
                year_list.append(year)
            
                if download.lower() == 'y':
                    for print_year in print_years:
                        if print_year == int(year):
                            print(f'downloading.. {print_year}')
                            pdf_download(pdf_url, form_number, year)

        if soup.find(class_='errorBlock'):
            print('No Results were found, check inputs')
            return
        
        elif soup.find(class_='NumPageViewed').find_all('a'):
            next_page_text = soup.find('th', class_='NumPageViewed').find_all('a')[-1].text

            if next_page_text == 'Next »':
                next_page_partial = soup.find('th', class_='NumPageViewed').find_all('a')[-1]['href']
                next_page_url = base_url + next_page_partial
                find(next_page_url)
                return

    result["min_year"] = year_list[-1]
    result["max_year"] = year_list[0]
    data.append(result.copy())
    return data

####################################################

searches = input('Please enter the complete tax form number seperate by a comma follow by a space (not case sensitive): \n(ie. Form W-2, Form 1095-C, Form W-3, etc)\n>>').split(', ')

# testing:
# searches = ['forc', "Form W-2", "Form 1095-C"]
# searches = ['form 1095-c']
# download = 'y'

download = input('Would you like to download all related pdfs? (Y/N)\n>>')

'''If download is yes, this will generate a list of year based on input'''
if download =='y':
    print_range = input('Please provide the year range by using a dash in between the years (starting year must be smaller than ending year): (ie. 2018-2020)\n').split('-')
    # print_range = '2018-2021'.split('-')
    if int(print_range[0])> int(print_range[1]):
        print('Date range error. Unable to download files. Please rerun the program.\n')
        print_years = []

    else:
        print_years = [year for year in range(int(print_range[0]), int(print_range[1])+1)]
else:
    print_years = []



#Set initial URLs
base_url = 'https://apps.irs.gov/'

# Starts here
for search_item in searches:
    format_search = search_item.replace(' ', '+')

    # Generate a search url based on inputs.
    search_url = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value={format_search}&criteria=formNumber&submitSearch=Find'

    print(f'Currently searching {search_item} at this link: \n{search_url}\n')
    find(search_url)

print('***Task completed***')

if print =='y':
    print('All pdf files have been downloaded')

print(f'Final output is --> \n \n{data}')
