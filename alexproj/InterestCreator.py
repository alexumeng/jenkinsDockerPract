from collections import Counter



'''passes through the filtered essay, and take out the five most important word from it.'''


def interestCreator(filterList):
    summary = Counter(filterList)
    print(summary.most_common(5))
    
    return summary.most_common(5)
