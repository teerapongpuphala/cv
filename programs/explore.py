

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
soup = BeautifulSoup(html_doc, 'html.parser')


print(soup)                       #no tab form
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names
# , →were
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p></body></html>
print(soup.prettify())
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names
# , →were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link3">
#     Tillie
#    </a>
#    ;
# and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>

print(soup.title.name)
#title                
print(soup.title.string)             
# The Dormouse's story
print(soup.title.parent.name)       
#head
print(soup.p)
#<p class="title"><b>The Dormouse's story</b></p>
print(soup.p["class"])
#['title']
print(soup.a)
#<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(soup.a["class"])
#['sister']
print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(soup.find(id="link3"))
#<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
for link in soup.find_all('a'): print(link.get('href')) 
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie
print(soup.get_text())
# The Dormouse's story

# The Dormouse's story
# Once upon a time there were three little sisters; and their names
# , →were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
# ...

########################################################
####################chapter4############################
########################################################
# from bs4 import BeautifulSoup
# with open("index.html") as fp:
#     soup = BeautifulSoup(fp)

# soup = BeautifulSoup("<html>data</html>")


########################################################
####################chapter5############################
########################################################
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>',features="lxml")
type(soup.b)
print(type(soup.b))
#<class 'bs4.element.Tag'>
print(soup.b)
#<b class="boldest">Extremely bold</b>
print(soup.b.name)
#b
soup.b.name = "blockqoute"
print(soup)
#<blockqoute class="boldest">Extremely bold</blockqoute>
print(soup.b)
#None
print(soup.blockqoute)
#<blockqoute class="boldest">Extremely bold</blockqoute>
print(soup.blockqoute.name)
#blockqoute

soup = BeautifulSoup('<a id="boldest">',features="html.parser")
print(soup.a['id'])
#boldest
print(soup.a.attrs)
#{'id': 'boldest'}

soup.a['another-attr']=20
print(soup.a['another-attr'])
#20
print(soup.a)
#<a another-attr="20" id="boldest"></a>
del soup.a['another-attr']
print(soup.a)
#<a id="boldest"></a>
print(soup.a.get('id'))
#boldest
print(soup.a['id'])
#boldest
css_soup = BeautifulSoup('<p class="body strikeout">',features="html.parser")
print(css_soup.p['class'])
#['body', 'strikeout']                                       #wichtig
id_soup = BeautifulSoup('<p id = "my id">',features="html.parser")
print(id_soup.p['id'])
#my id                                                        #not as list

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">Homepage</a></p>',features="html.parser")
print(rel_soup.a['rel'])
#['index']
rel_soup.a['rel']=['index','content']
print(rel_soup.a)
#<a rel="index content">Homepage</a>
print(rel_soup.a['rel'])
#['index', 'content']
no_soup = BeautifulSoup('<p>Back to the <a rel="index content">Homepage</a></p>', multi_valued_attributes =None,features="html.parser")
print(no_soup.a['rel'])
#index content
print(no_soup.a.get_attribute_list('rel'))
#['index content']



# im didnt install xml-package

# xml_soup =BeautifulSoup('<p> class="body strikeout"></p>','xml')
# print(xml_soup.p['class'])
# u'body strikeout'

# class_is_multi= { '*' : 'class'} 
# xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_, →attributes=class_is_multi) 
# xml_soup.p['class'] 
# [u'body', u'strikeout']


#navigatestring
soup = BeautifulSoup('<p>Back to the <a rel="index content">Homepage</a></p>', multi_valued_attributes =None,features="html.parser")
print(soup.p.string)
#None               ???????????
print(type(soup.p.string))
#<class 'NoneType'>         ????????????


print(type(soup.a.string))
#<class 'bs4.element.NavigableString'>
print(soup.a.string)
#Homepage

unicode_string = str(soup.a.string)
print(unicode_string)
#Homepage
print(type(unicode_string))
#<class 'str'>

soup.a.string.replace_with("YYYYYYYYYYYYY")
print(soup.a.string)
#YYYYYYYYYYYYY
print(soup.a)
#<a rel="index content">YYYYYYYYYYYYY</a>


# If you want to use a NavigableString outside of BeautifulSoup,
# you should call unicode() on it to turn it into a normal Python Unicode string.
# If you don’t, your string will carry around a reference to the entire Beautiful Soup parse tree,
# even when you’re done using Beautiful Soup.
# This is a big waste of memory

doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml") 
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text="INSERT FOOTER HERE").replace_with(footer)
print(doc)
#<?xml version="1.0" encoding="utf-8"?>
#<document><content/><footer>Here's the footer</footer></document>
print(doc.name)
#[document]


markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup,features="lxml")
comment = soup.b.string
print(type(comment))
#<class 'bs4.element.Comment'>
print(comment)
#Hey, buddy. Want to buy a used parser?
print(soup.b.prettify())
# <b>
#  <!--Hey, buddy. Want to buy a used parser?-->
# </b>
#Here’s an example that replaces the comment with a CDATA block:
from bs4 import CData 
cdata = CData("A CDATA block") 
comment.replace_with(cdata)
print(soup.b.prettify())
# <b>
#  <![CDATA[A CDATA block]]>  
# </b>