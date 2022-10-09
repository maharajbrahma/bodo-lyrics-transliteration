# Bare bone py

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

    # Todo: variable naming
    # Final Lyrics list contains dictionary of song name and lyrics
    lyrics = []
    
    # buggy: fetching only first 7 songs lyrics
    for url in urls[:7]:
        lyrics.append(extract_lyrics(url))
        # print(extract_lyrics(url))

    return lyrics

def extract_lyrics(url=''):
    if not url:
        return
    req = requests.get(url)
    parse = BeautifulSoup(req.text, 'html.parser')
    
    body_content = parse.find("div", class_="post-body post-content")

    body = body_content.find_all("span")

    # just to debug
    for i, b in enumerate(body):
        # print(i, b.text.strip())
        pass
    
    lyrics = []

    for i, t in enumerate(body):
        k = remove_metadata(t.text.strip())
        k = remove_music_clues(k)
        k = remove_footnote(k)
        
        if k:
            lyrics.append(k)

    ly = {
        "song-name": "",
        "lyrics": []
    }

            
    ly["song-name"] = song_name(url)
    ly["lyrics"] = lyrics

    return ly

def song_name(url):
    s = str(url.split("/")[-1]).split("-")
    n = s[0] + "-" + s[1]
    return n

def remove_metadata(text):
    text = re.sub("Vocal.*", "", text, flags=re.I)
    text = re.sub("Master.*", "", text, flags=re.I)
    text = re.sub("Direction.*", "", text, flags=re.I)
    text = re.sub("Starring.*", "", text, flags=re.I)
    text = re.sub("DOP.*", "", text, flags=re.I)
    text = re.sub("Arial.*", "", text, flags=re.I)
    text = re.sub("Singer.*", "", text, flags=re.I)
    text = re.sub("Starring.*", "", text, flags=re.I)
    text = re.sub("Mijing.*", "", text, flags=re.I)
    text = re.sub("Concept.*", "", text, flags=re.I)
    text = re.sub(".*Lyrics.*", "", text, flags=re.I)
    text = re.sub("Makeup.*", "", text, flags=re.I)
    text = re.sub("Make-Up.*", "", text, flags=re.I)
    text = re.sub("\nCo Cast.*", "", text, flags=re.I)
    text = re.sub("\n.*Music.*", "", text, flags=re.I)
    text = re.sub("\n.*Guiter.*", "", text, flags=re.I)
    text = re.sub("\n.*Light.*", "", text, flags=re.I)
    text = re.sub("\n.*", "", text, flags=re.I)
    text = re.sub("Produced.*", "", text, flags=re.I)
    text = re.sub("Assist.*", "", text, flags=re.I)
    text = re.sub("Aeriel.*", "", text, flags=re.I)
    text = re.sub("Lyricist.*", "", text, flags=re.I)
    text = re.sub("Genres.*", "", text, flags=re.I)
    text = re.sub("Romantic.*", "", text, flags=re.I)
    text = re.sub("Producer.*", "", text, flags=re.I)
    text = re.sub("Riya Brahma.*", "", text, flags=re.I)
    text = re.sub("Audio.*", "", text, flags=re.I)
    text = re.sub("Recording.*", "", text, flags=re.I)
    text = re.sub("Mixing.*", "", text, flags=re.I)
    text = re.sub("Video.*", "", text, flags=re.I)
    text = re.sub("Director.*", "", text, flags=re.I)
    text = re.sub("Editor.*", "", text, flags=re.I)
    text = re.sub("Production.*", "", text, flags=re.I)
    text = re.sub("Phwi phwi phwi Bodo Melody song is sung by Nikita Boro and written by Ibson Lal Baruah", "", text, flags=re.I)
    return text

def remove_music_clues(text):
    text = re.sub("Music.*", "", text, flags=re.I)
    text = re.sub("\..*", "", text, flags=re.I)
    text = re.sub("times", "", text, flags=re.I)
    return text

def remove_footnote(text):
    text = re.sub("Thanks for visiting Bodo Song Lyrics Site.", "", text, flags=re.I)
    text = re.sub("Thanks.*", "", text, flags=re.I)
    text = re.sub("Related.*", "", text, flags=re.I)
    text = re.sub("Visiting.*", "", text, flags=re.I)
    text = re.sub("You make.*", "", text, flags=re.I)
    return text