import requests as r
from bs4 import BeautifulSoup as bs
from lxml import etree

#headers
tei = etree.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")
tei_header = etree.SubElement(tei, "teiHeader")
file_desc = etree.SubElement(tei_header, "fileDesc")
title_stmt = etree.SubElement(file_desc, "titleStmt")
title = etree.SubElement(title_stmt, "title")
title.text = "Rozhlas - celá stránka na zprávách, archív"
text = etree.SubElement(tei, "text")

url = "https://www.irozhlas.cz/zpravy-archiv"

session= r.Session()
response = session.get(url)
result = bs(response.content, 'html.parser')


articles = result.find_all("article")

for article in articles:
    link = "https://www.irozhlas.cz" + article.find("a").get("href")
    page = session.get(link)
    soup = bs(page.content, 'html.parser')
    content = soup.find("article").text
    authors = soup.find_all("a", class_="meta__link")
    title = soup.find_all("h1")[1].text.strip()

    #document creation
    div1 = etree.SubElement(text, "div", type="document")
    div1_title = etree.SubElement(div1, "head")
    div1_title.text = title
    
    #authors
    div_author = etree.SubElement(div1, "author")
    for author in authors:
        author1 = etree.SubElement(div_author, "name")
        author1.text = author.text

    div1_body = etree.SubElement(div1, "body")
    p1 = etree.SubElement(div1_body, "p")
    p1.text = content
    

tree = etree.ElementTree(tei)
tree.write("corpus.xml", pretty_print=True, xml_declaration=True, encoding="UTF-8")

print("TEI corpus created succesfully!")


