#nltk
import nltk
import Stopword
import WordFilter
import InterestCreator
import User

nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from collections import Counter

nltk.download('stopwords')

'''Main.py -
    In here, a file is passed into run. The file is then read and tokenized,
    filtered, and then it's interests are generated.'''


def run(UserFile):

    debug = False
    # opening a text file.
    f = open(UserFile , "r")


    essay = ""
    for line in f:
        essay += line
        if debug == True:
            print(line)
    essay = essay.replace("'", "")
    essay = essay.replace(",", "")
    essay = essay.replace(".", "")
    #replace comma, and more thing like that.

    wordfilter = stopwords.words('english')
    wordfilter = Stopword.Addstopwords(wordfilter)

    word = word_tokenize(essay)
    word = [t.lower() for t in word]
    if debug == True:
        print(len(word), 'word', word)

    filterList = WordFilter.wordsfilter(word, wordfilter)
    #wordfilter system
    if debug == True:
        print(filterList)

    interestList = InterestCreator.interestCreator(filterList)
    f.close()
    #summary of the text.
    return interestList

