# In this program you can extract what ever the links will be in the website it will extract and provide it with you
#first of all pip install requests in cmd prompt to link with the server to extract the data
# also pip install Beautifulsoup to parse the html content using beatutiful soup
import requests 
from bs4 import BeautifulSoup
import re

def extract_info(url):
    try:
        #GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        #Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract social links 
        social_links = []
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if re.search(r'(facebook|twitter|linkedin|instagram)', href):
                social_links.append(href)

        #Extract email addresses using regular expressions
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
        emails = re.findall(email_pattern, response.text)

        #contact section
        contact_patterns = [r'(?i)phone\s?:?\s?(\d[\d\s\-]+)', r'(?i)contact\s?:?\s?(\d[\d\s\-]+)']
        contacts = []
        for pattern in contact_patterns:
            contacts.extend(re.findall(pattern, response.text))

        return social_links, emails, contacts

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return [], [], []

# Get user input 
user_input_url = input("Enter the website URL:")

social_links, emails, contacts = extract_info(user_input_url)
print("Social Links:")
for link in social_links:
    print(link)

print("\nEmails:")
for email in emails:
    print(email)

print("\nContacts:")
for contact in contacts:
    print(contact)
