from bs4 import BeautifulSoup

# read from the local file

try:
    with open("alice.html") as fp:
        soup = BeautifulSoup(fp , 'html.parser')
        print("Successfully parsed Alice HTML file")
except FileNotFoundError:
    print("alice.html not found")


# Option b we pass it a direct string


html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup2 = BeautifulSoup(html_doc , 'html.parser')
print(soup2.prettify())


# How to navigate the different datastructures of a html document

# 1. get the title

print(soup2.title) # gets the title with even the tags

print(soup2.title.name)

print(soup2.title.string) # ignores the strings


print(soup2.a) # gets a single link

print(soup2.find_all('a')) # gets all the possible links

print(soup.find(id = 'link3')) #get by id



# extract all teh urls found within a page <a> tag

for link in soup.find_all('a'):
    print(link.get('href'))

# getting all the text from a page

print(soup.get_text())