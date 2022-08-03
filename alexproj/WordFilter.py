'''filter the essay'''


def wordsfilter(word, wordfilter):
    filterList = []
   
    for w in word:
        if w not in wordfilter:
            filterList. append(w)
            
    return filterList
#wordfilter system

