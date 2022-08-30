import pandas as pd
from gtts import gTTS
import sys

def tts(word):
    tts = gTTS(text=word, lang="en")
    tts.save(str(i) + "." + word + ".mp3")

if __name__ == "__main__":
    filename = sys.argv[1]
    csv = pd.read_csv(filename, header=None)
    words = csv[0].tolist()
    for i, word in enumerate(words):
        tts(word)
