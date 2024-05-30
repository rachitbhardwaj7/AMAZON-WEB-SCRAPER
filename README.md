
# Amazon Product Scraper
#### Video Demo:  <https://youtu.be/ACqhn6wVFkU>
 #### Description:
this project help the users in web scrappig of the amazon websites to fetch the total number of products, product name
,price,their  rating with the help of web scraping another website to get and use free proxies in web scraping .
the scraped data is shown by pandas data frame and also saved in .csv file which can be further used in data analysis using numpy and pandas
feautures
- Searches Amazon for a specified item.
- Retrieves product details such as name, price, and rating.
- Uses free proxies to fetch content.
- Saves the scraped data to a CSV file.
  Requirements
- Python 3.x
- Requests library
- BeautifulSoup library
- Pandas library
working :
 the program take first the item to search  then the search function return the url to the page
 then we extract the html code trough request function if the content is fetched we then use the BeautifulSoup library to permorm the search of the text and specific html tag to extract the data those data are then converted to pandas dataframe then converted to .csv file
Install the required packages:

bash
Copy code
pip install requests beautifulsoup4 pandas
Usage
Run the main script:

bash
Copy code
python project.py
Enter the item you want to search for when prompted.

The script will fetch the search results from Amazon using free proxies and display the total results found.

The product information (name, price, and rating) will be saved to products.csv in the same directory.

Example
bash
Copy code
$ python project.py
Enter the item to search: laptop
Retrieved 300 proxies
Using proxy 123.456.789.012:8080
Successfully fetched content with proxy 123.456.789.012:8080
Total results: 10000 results for "laptop"
                                      Name    Price    Rating
0      Acer Aspire 5 Slim Laptop       52,990  4.5 out of 5 stars
1      Lenovo IdeaPad 3 Laptop         34,999  4.2 out of 5 stars
...
Data saved to products.csv
Testing
To test the project, you can use the provided test.py file:

bash
Copy code
python test.py
The test script uses unittest and unittest.mock to test the main function and other top-level functions.

Code Overview
project.py: The main script that performs the scraping and saves the data to a CSV file.
test.py: The test script to validate the functionality of project.py.
Functions
get_free_proxies(): Fetches a list of free proxies from "https://free-proxy-list.net/".
search(string): Creates the Amazon search URL based on the provided search string.
page_content(url, proxies): Fetches the page content using the provided proxies.
total_results(soup): Extracts the total number of results from the search results page.
product_info(soup): Extracts the product name, price, and rating from the search results page.
save_csv(data, filename): Saves the extracted product data to a CSV file.
main(): The main function that coordinates the scraping process.


Acknowledgements
Free Proxy List for providing free proxies.
BeautifulSoup for HTML parsing.
Requests for making HTTP requests.
Pandas for data manipulation and CSV handling.
