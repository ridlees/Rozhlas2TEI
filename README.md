# Rozhlas2TEI
Exactly as title says. Homework that scrapes Rozhlas data and creates TEI XML from it. 


# Install

`pip install -r requirements.txt `

# Usage

`python3 digitalnimetody.py` if you want single TEI file that contains everything in one document (according to voyant tools)

OR

`python3 digitalnimetody-víc-korpusu.py` if you want everything in seperate TEI files (so it generates around 70 documents)

I HAVE NO CLUE WHAT IS BETTER :D 

I cannot make voyant tools to show author, probably I must provide them in the main header (will explore and update later).

Probably it would be good idea to "clear the content". Sadly, for Rozhlas almost everything is a paragraph (p tag), so it gets little messy. I decided to let all the other paragraphs stay (which makes the analysis little messy, but use stopword for things like "sdílet na twitteru" and you will be fine) because things like related articles or hidden paragraphs could show something interesting in analysis. 

STOPWORDS to add:
* Sdílet na Facebooku
* Sdílet na Twitteru
* Sdílet na LinkedIn
* Kopírovat url adresu
* Zkrácená adresa
* Kopírovat do schránky
* Tisknout
* Související články  
* Další články
* Zavřít