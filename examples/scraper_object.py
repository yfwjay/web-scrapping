from bs4 import BeautifulSoup


# Beautifulsoup transforms complex html document into a complex of python objects.

# 4 kind of objects involved are as follows: 
        # 1.Tag
        # 2.Navigable string
        # 3.Beautiful soup
        # 4. Comment

# 1. CLASS TAG 
# Corresponds to a html tag 

try:
    with open("alice.html") as fp:
        soup = BeautifulSoup(fp , 'html.parser')
        print("Successfully parsed Alice HTML file")
except FileNotFoundError:
    print("alice.html not found")

bold_tag = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = bold_tag.b
tag_type = type(bold_tag.b)
print(f"The type tag is = {tag_type}")

# attributes and methods of different tags

# 1. name
tag.name = 'blockquote'
tag
print(f"Name of the bold tag is  = {tag.name}")

# 2. Attribute
print(f"Attribute of the bold tag is = {tag['class']}")

# 3. Accessing the dictionary of attributes
print(f"Dictionary of the b tag = {tag.attrs}")

# 4. keys of that dictionary
print(f"Keys of the b tag = {tag.attrs.keys()}")

# 5. values of the dictionary
print(f"Values of the b tag = {tag.attrs.values()}")

# CLASS NAVIGABLE STRING

# a tag can contain strings as pices of text

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')

tag = soup.b

tag.string

print(type(tag.string))  #  <class 'bs4.element.NavigableString'>

# You can convert a NavigableString to a Unicode string with str:

unicode_string = str(tag.string)
unicode_string
# 'Extremely bold'
type(unicode_string)
# <type 'str'>

# You can't edit a string in place, but you can replace one string with another, using replace_with():

tag.string.replace_with("No longer bold")
tag
# <b class="boldest">No longer bold</b>

# BEAUTIFUL SOUP OBJECT

#  represents the parsed document as a whole. For most purposes, you can treat it as a Tag object

doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text="INSERT FOOTER HERE").replace_with(footer)
# 'INSERT FOOTER HERE'
print(doc)
# <?xml version="1.0" encoding="utf-8"?>
# <document><content/><footer>Here's the footer</footer></document>


# CLASS COMMENT

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
type(comment)
# <class 'bs4.element.Comment'>

# NAVIGATING THE TREE

# GOING DOWN

