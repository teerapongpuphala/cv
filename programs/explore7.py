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


# find and find_all
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,features='html.parser')

print(soup.find_all('b'))
# [<b>The Dormouse's story</b>]
print(type(soup.find_all('b')))
# <class 'bs4.element.ResultSet'>

# start with b
import re 
for tag in soup.find_all(re.compile("^b")): 
    print(tag.name)
# body
# b

# contain t
for tag in soup.find_all(re.compile("t")): 
    print(tag.name) 

# html
# title

for tag_a_b in soup.find_all(["a", "b"]):
    print(tag_a_b)
# <b>The Dormouse's story</b>
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

for tag in soup.find_all(True): 
    print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# p

# FUNCTION
def has_class_but_no_id(tag): 
    return tag.has_attr('class') and not tag.has_attr('id')
print(soup.find_all(has_class_but_no_id))
# [<p class="title"><b>The Dormouse's story</b></p>, <p class="story">Once upon a time there were three little sisters; and their names
# , →were
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>, <p class="story">...</p>]


def not_lacie(href): 
    return href and not re.compile("lacie").search(href)
print(soup.find_all(href=not_lacie))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

from bs4 import NavigableString 
def surrounded_by_strings(tag): 
    return (isinstance(tag.next_element, NavigableString) and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
     print(tag.name)
# body
# p
# a
# a
# a
# p

#FIND_ALL()
print(soup.find_all("title"))
# [<title>The Dormouse's story</title>]
print(soup.find_all("p","title"))
# [<p class="title"><b>The Dormouse's story</b></p>]
print(soup.find_all("a"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(soup.find_all(id="link2"))
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

import re
print(soup.find(string=re.compile("sisters")))
# Once upon a time there were three little sisters; and their names
# , →were
# 
print(soup.find_all("title"))
# [<title>The Dormouse's story</title>]

# keyword arguments
print(soup.find_all(id="link2"))
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

print(soup.find_all(href=re.compile("elsie")))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

print(soup.find_all(id=True))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(soup.find_all(href=re.compile("elsie"), id='link1'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
print(data_soup.find_all(attrs={"data-foo": "value"}))
# [<div data-foo="value">foo!</div>]

name_soup = BeautifulSoup('<input name="email"/>') 
print(name_soup.find_all(name="email"))
# []
print(name_soup.find_all(attrs={"name": "email"}))
# [<input name="email"/>]