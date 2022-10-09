# Bare bone py

from asyncore import write
from lyrics import fetch_lyrics
from transliterate import transliterate
import  csv
import os

# Credits: https://stackoverflow.com/questions/29310792/how-to-save-a-list-as-a-csv-file-with-new-lines
def write_to_file(filename=None, data=[], transliterated=False):
    if (os.path.exists(os.path.join(os.getcwd(), 'original'))):
        pass
    else:
        # Make directory to store original lyrics files
        os.mkdir(os.path.join(os.getcwd(), 'original'))

    if (os.path.exists(os.path.join(os.getcwd(), 'transliterated'))):
        pass
    else:
        # Make directory to store original lyrics files
        os.mkdir(os.path.join(os.getcwd(), 'transliterated'))

    if not transliterated:
        with open('original/' + filename, "w", encoding="utf-8") as f:
            wr = csv.writer(f,delimiter="\n")
            wr.writerow(data)
    else:
        with open('transliterated/' + filename, "w", encoding="utf-8") as f:
            wr = csv.writer(f,delimiter="\n")
            wr.writerow(data)


# Todo: Check khalamgwr nang gou file ya dong na gwiya!
def remove_files():
    print("Removing pre-existing files")
    if (os.path.exists(os.path.join(os.getcwd(), 'original'))):
        files = os.listdir(os.path.join(os.getcwd(), 'original'))
        for f in files:
            os.remove(os.path.join(os.getcwd(), 'original') + '/'+ f)

    else:
        pass

    if (os.path.exists(os.path.join(os.getcwd(), 'transliterated'))):
        files = os.listdir(os.path.join(os.getcwd(), 'transliterated'))
        for f in files:
            os.remove(os.path.join(os.getcwd(), 'transliterated') + '/' + f)
    else:
        pass


if __name__ == "__main__":

    # remove files
    remove_files()

    lyrics_list = fetch_lyrics() # list of song-name, lyrics


    for l in lyrics_list:
        d = dict(l)

        # For debugging
        # print(d['lyrics']) 
        # print(transliterate(d['lyrics']))
        transliterated_lyrics = transliterate(d['lyrics'])

        write_to_file(d['song-name'], d['lyrics'])

        write_to_file(d['song-name'], transliterated_lyrics, transliterated=True)

        # writing to files


    print("Done!")
    print("Check Original and Transliterated Directories")
    # pass