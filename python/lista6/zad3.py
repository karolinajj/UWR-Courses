#Karolina Jędraszek
#lista 6, zadanie 3

import requests
from bs4 import BeautifulSoup
import re


def get_content(pages): #returns a dictionary with urls as keys and content as values
    result = dict()
    for url in pages:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        result[url] = re.findall(r'\b\w+\b', soup.body.text.lower()) #regular expression: w+ words, \b word boundary anchor
        #print(soup.body.text)
    return result

def make_index(pages): 
    dict_pages = get_content(pages)
    index = dict()
    for url, content in dict_pages.items():
        for word in content:
            word = word.lower()
            if word not in index:
                index[word] = [url]
            else:
                index[word].append(url)
    return index

def count_word(url, word): #counts how many times the given word appeared on a page
    word = word.lower()
    content = get_content([url])[url]

    result = 0

    for text in content:
        if text.lower() == word:
            result+=1
    return result

    
def most_popular(index, word):
    pages = index[word] #table of pages that contain the given word
    word_count = []

    for url in pages:
        word_count.append((count_word(url,word),url))
    
    word_count.sort()
    return word_count[len(word_count)-1][1]

#------------------------------------------    

pages = ["https://dev.d3a7t2felf3dzs.amplifyapp.com","https://uwr.edu.pl"]

word = "hello"


print("Index:\n", make_index(pages))
print()
print(f"Word '{word}' is the most popular on page: \n{most_popular(make_index(pages), word)}")



