import requests
import xml.etree.ElementTree as ET

# Fetch the XML from the GVSU Events Calander
url = 'https://www.gvsu.edu/events/events.xml'
response = requests.get(url)
response.raise_for_status()  # raises an error if the request failed

# Parse the XML content (note: fromstring, not parse)
root = ET.fromstring(response.content)

# *Add whatever words you want to search for
keywords = ['food', 'breakfast', 'lunch', 'dinner', 'snack', 'drink', 'beverage']

# Iterate through elements (in our case item tags)
for item in root.findall('.//item'):
    description = item.find('description').text.lower()

    # Search for keywords
    keywordsMatched = []
    for word in keywords:
        if word in description:
            keywordsMatched.append(word)

    # Print title, keywords matched, date, and link to any events found
    if keywordsMatched:
        title = item.find('title').text
        date = item.find('pubDate').text
        link = item.find('link').text
        print(f"Title: {title}\nDate: {date}\nKeywords: " + ", ".join(keywordsMatched) + f"\nLink: {link}\n")