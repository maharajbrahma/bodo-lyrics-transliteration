from ai4bharat.transliteration import XlitEngine
from indicnlp.tokenize import indic_tokenize
import pandas as pd

b = XlitEngine("brx", beam_width=5, rescore=False)

# Roman Script to Devanagari
def transliterate(lyrics_list):
    # Convert list to data frame
    lyrics_df = pd.Series(lyrics_list, index=None)
    
    # print(lyrics_df)
    
    tokenized_df = lyrics_df.apply(sentence_english_tokenize)

    # print(tokenized_df)

    devanagarized_df = tokenized_df.apply(devanagarized)

    return devanagarized_df.tolist()

# Bad naming
def devanagarized(x):
    l = []
    for t in x.split():
        o = b.translit_word(t, topk=5)
        l.append(o['brx'][0])
        
    x = ' '.join(l)
    return x

def sentence_english_tokenize(x):
    # english sentence tokenize
    l = []
    for t in indic_tokenize.trivial_tokenize(x):
        l.append(t)
    x = ' '.join(l)
    return x