import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('events.xml')
root = tree.getroot()

# *Add whatever words you want to search for
keywords = ['food', 'free food', 'breakfast', 'lunch', 'dinner', 'snacks', 'drinks', 'beverages']

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
        print(f"Title: {title}\nDate: {date}\nKeywords: {keywordsMatched}\nLink: {link}\n")