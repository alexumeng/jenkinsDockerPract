import nltk



from nltk.corpus import stopwords 
nltk.download('stopwords')


'''takes out unimportant word.'''
def Addstopwords(wordfilter):
    wordfilter.append("[")
    wordfilter.append("]")
    return wordfilter