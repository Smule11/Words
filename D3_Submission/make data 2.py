import nltk 
from thesaurus import Word, fetchWordData
import numpy as np
import re
import wordfreq
from wordfreq import word_frequency
from wordfreq import zipf_frequency
from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer

lancaster=LancasterStemmer()
porter=PorterStemmer()
inputArray = []
wordPut = "bed"

def precision(word):
    synList = []
    nomRatio = 0
    denomRatio = 0
    # theSyns = []
    # for i in Word(wordPut).synonyms('all'):
    #     for j in i:
    #         thesSyns.append(lancaster.stem(j))
    # theSyns1 = set(thesSyns)
    # for j in meaningList:
    #     wordList.append(lancaster.stem(j))
    # wordList = set(mean)
    for j in fetchWordData(word)[i]['syn']:
        synList.append(lancaster.stem(j.word))
    meaningList = re.sub("[^\w]", " ",  fetchWordData(wordPut)[i]['meaning']).split()
    wordList = []
    for j in meaningList:
        wordList.append(lancaster.stem(j))
    for j in wordList:
        if j in synList:
            nomRatio += 1
        denomRatio += 1
    for i in range(len(fetchWordData(wordPut))-1):
        for j in fetchWordData(word)[i]['syn']:
            synList.append(lancaster.stem(j.word))
        meaningList = re.sub("[^\w]", " ",  fetchWordData(wordPut)[i]['meaning']).split()
        wordList = []
        for j in meaningList:
            wordList.append(lancaster.stem(j))
        for j in wordList:
            if j in synList:
                nomRatio += 1
            denomRatio += 1
    return (nomRatio*1.0) / (1.0*denomRatio)
    


counter = 0
for i in range(len(fetchWordData(wordPut))-1)  :
    counter += 1
    inputRow = []
    synonymList = []
    nomRatio = 0
    denomRatio = 0
    # print("6", fetchWordData(wordPut)[i])
    for j in fetchWordData(wordPut)[i]['syn']:
        synonymList.append((j.word),)
    inputRow.append(counter)
    inputRow.append(wordPut)
    inputRow.append(fetchWordData(wordPut)[i]['partOfSpeech'])
    inputRow.append(fetchWordData(wordPut)[i]['meaning'])
    inputRow.append(set(synonymList))
    inputRow.append(zipf_frequency(wordPut, 'en', wordlist='best'))
    wordList = []
    synList = []
    meaningList = re.sub("[^\w]", " ",  fetchWordData(wordPut)[i]['meaning']).split()
    for j in meaningList:
        wordList.append(lancaster.stem(j))
    meanList = set(wordList)
    for j in set(synonymList):
        synList.append(lancaster.stem(j))
    print("hmmmmmm", fetchWordData(wordPut)[i]['meaning'], set(synonymList))
    print("AHHAHAH", meanList, synList)
    for j in meanList:
        if j in synList:
            nomRatio += 1
        denomRatio += 1

    inputRow.append((nomRatio*1.0) / (1.0*denomRatio))
    if len(inputArray) is 0:
        inputArray = inputRow
    else:
        inputArray = np.vstack((inputArray,inputRow))
    
print(fetchWordData(wordPut))
print(inputArray)