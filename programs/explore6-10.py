html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names
, →were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,features="html.parser")
print(soup.contents)
# ['\n', <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names
# , →were
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p></body></html>]
print(soup.contents[0])
# \n
print(soup.head)
# <head><title>The Dormouse's story</title></head>
print(soup.title)
# <title>The Dormouse's story</title>
print(soup.head.title)
# <title>The Dormouse's story</title>
print(soup.head.contents)
# [<title>The Dormouse's story</title>]
print(soup.title.contents)
# ["The Dormouse's story"]
print(soup.body.b)
# <b>The Dormouse's story</b>
print(soup.body.b.contents)
#["The Dormouse's story"]
print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

for child in soup.title.children:
    print(child)
    # The Dormouse's story

for child in soup.html.children:
    print(child)
# <head><title>The Dormouse's story</title></head>


# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names
# , →were
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p></body>

for child in soup.head.descendants:
    print(child)
# <title>The Dormouse's story</title>
# The Dormouse's story


print(len(list(soup.children)))
#2
print(len(list(soup.descendants)))
#26


# STRING
print(soup.title.string)
#The Dormouse's story
print(soup.head.contents)
# [<title>The Dormouse's story</title>]
print(soup.head.string)
# The Dormouse's story
print(type(soup.head.string))
#<class 'bs4.element.NavigableString'>
print(type(str(soup.head.string)))
# <class 'str'>

# If a tag contains more than one thing, then 
# it’s not clear what .string should refer to, so .string is deﬁned
#  to be None:
print(soup.html.string)
# None


#STRINGS STRIPPED_STRINGS
for string_soup in soup.html.strings:
    print(str(string_soup)) #class string
    # print(string_soup)    #class beautiful
# ...
for string_no_white_space in soup.stripped_strings:
    print(repr(string_no_white_space))
# "The Dormouse's story"
# "The Dormouse's story"
# 'Once upon a time there were three little sisters; and their names\n, →were'
# 'Elsie'
# ','
# 'Lacie'
# 'and'
# 'Tillie'
# ';\nand they lived at the bottom of a well.'
# '...'

#PARANT
print(soup.html.title)
# <title>The Dormouse's story</title>
print(soup.html.title.parent)
# <head><title>The Dormouse's story</title></head>
print(soup.parent)
# None
print(soup.html.head.title.parent)
# <head><title>The Dormouse's story</title></head>

# PARENTS
for parent in soup.a.parents:
    print(parent.name)
# p
# body
# html
# [document]


# .next_sibling and .previous_sibling
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>") 
print(sibling_soup.prettify())
#  sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
# <html>
#  <body>
#   <a>
#    <b>
#     text1
#    </b>
#    <c>
#     text2
#    </c>
#   </a>
#  </body>
# </html>

print(sibling_soup.b.next_sibling)
# <c>text2</c>
print(sibling_soup.c.previous_sibling)
# <b>text1</b>
print(sibling_soup.b.previous_sibling)
# None
print(sibling_soup.c.next_sibling)
# None

# The strings “text1” and “text2” are not siblings,
#  because they don’t have the same parent:

# In real documents, the .next_sibling or .previous_sibling 
# of a tag will usually be a string containing whitespace
print(soup.a.next_sibling)
# ,
# \n
print(soup.a.next_sibling.next_sibling)
#<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>

for sibling in soup.a.next_siblings:
    print(repr(sibling))
# ,

# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# ',\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# ' and\n'
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# ';\nand they lived at the bottom of a well.'
print("-----------------")
for sibling in soup.find(id="link3").previous_siblings: 
    print(repr(sibling))
# ' and\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# ',\n'
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# 'Once upon a time there were three little sisters; and their names\n, →were\n'

print(soup.find("a", id = "link3"))
#<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

print(soup.find("a", id="link3").next_sibling)
# ;
# and they lived at the bottom of a well.


print(soup.find("a", id = "link3").next_element)
#Tillie
#  .next_element of that <a> tag, the thing that was parsed immediately
#   after the <a> tag, is not the rest of that sentence:
#    it’s the word “Tillie”:

print(soup.find("a", id = "link3").previous_element)
# and
print(soup.find("a", id = "link3").previous_element.next_element)
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


# for element in soup.find("a",id="link3").next_elements: 
#     print(repr(element)