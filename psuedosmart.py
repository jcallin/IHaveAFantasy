#!/usr/bin/python3

import pyperclip, random
from PyDictionary import PyDictionary

dictionary = PyDictionary()
origText = str(pyperclip.paste())
finalWordList = []

for word in origText.split():
    if(len(word) > 5):
        #print("replacing word " + word)
        newWords = dictionary.synonym(word)
        if (newWords == None):
            continue
        newWord = random.choice(newWords)
        newWord = newWord + " "
        finalWordList.append(newWord)
        continue
    word = word + " "
    finalWordList.append(word)
finalText = ""
for word in finalWordList:
    finalText = finalText + word
print(finalText)
