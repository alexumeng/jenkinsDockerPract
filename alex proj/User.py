"""basiclly creating userobject, can update interestlist here."""

class user:

    def __init__(self, name, interestList):
        self.name = name
        self.userinterestlist = interestList

    def assignlist(self, interestList):
        print("assigning")
        for x in interestList:
         self.userinterestlist.append(x)
        return self.userinterestlist

    def Showinterest(self):
        print("This is the interests lists of the user: ")
        print(self.userinterestlist)
        print("hi")
