from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

# Start a Selenium webdriver
driver = webdriver.Chrome()

# Open the webpage containing the dynamic table
driver.get("https://bordeauxindex.com/livetrade/marketplace")

# Scroll down to load more rows
SCROLL_PAUSE_TIME = 0

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Extract the HTML content
html = driver.page_source

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find and extract the table
table = soup.find('table', class_='livetrade-table')

# Extract headers from the table
headers = [header.text.strip() for header in table.find_all('th')]

# Extract data from the table
data = []
table_body = table.find('tbody')
for row in table_body.find_all('tr'):
    #vintage = int(row.find('td', 'hide-mobile-tablet').text.replace('|', '').strip())
    #wine_name = row.find('span', "product product-name").text.strip()
    wine_details = row.find('span', "subscript").text.strip()
    print(wine_details)


    #print(wine_name)
    #cells = row.find_all('td')
    #data.append([cell.text.strip() for cell in cells])

# Create a DataFrame
#df = pd.DataFrame(data[1:], columns=headers)

# Close the browser
driver.quit()

# Print the DataFrame
#print(df)
#df.to_excel('sample.xlsx')
