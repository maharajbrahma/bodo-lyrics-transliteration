# Bare bone py

import enum
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests
import re

def fetch_lyrics():
    tree = ET.parse('sitemap.xml')
    root = tree.getroot()
    tag = "{http://www.sitemaps.org/schemas/sitemap/0.9}loc"
    urls = []

    for d in root.iter(tag):
        # print(d.text)
        urls.append(d.text)
    
    # print(urls)
    print("Total urls found {}".format(len(urls)))

def extract_lyrics(url=''):
    if not url:
        return
    req = requests.get(url)
    parse = BeautifulSoup(req.text, 'html.parse')
    
    body_content = parse.find("div", class_="post-body post-content")

    body = body_content.find_all("span")

    # just to debug
    for i, b in enumerate(body):
        print(i, b.text.strip())

def remove_metadata(text):
    text = re.sub("Starring.*", "", text, 0, flags=re.I)
    text = re.sub("DOP.*", "", text, 0, flags=re.I)
    text = re.sub("Arial.*", "", text, 0, flags=re.I)
    text = re.sub("Singer.*", "", text, 0, flags=re.I)
    text = re.sub("Starring.*", "", text, 0, flags=re.I)
    text = re.sub("Mijing.*", "", text, 0, flags=re.I)
    text = re.sub("Concept.*", "", text, 0, flags=re.I)
    text = re.sub(".*Lyrics", "", text, 0, flags=re.I)
    text = re.sub("Makeup.*", "", text, 0, flags=re.I)
    text = re.sub("\nCo Cast.*", "", text, 0, flags=re.I)
    text = re.sub("\n.*Music.*", "", text, 0, flags=re.I)
    text = re.sub("\n.*Guiter.*", "", text, 0, flags=re.I)
    text = re.sub("\n.*Light.*", "", text, 0, flags=re.I)
    text = re.sub("\n.*", "", text, 0, flags=re.I)
    text = re.sub("Produced.*", "", text, 0, flags=re.I)
    
    return text

def remove_music_clues(text):
    text = re.sub("Music.*", "", text)
    return text

def remove_footnote(text):
    text = re.sub("You make.*", "", text)
    return text