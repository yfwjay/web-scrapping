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