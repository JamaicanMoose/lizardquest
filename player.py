class Player:
    """Holds Relevant data to the current state of the player character"""
    name=""
    inventory=[]
    titles=[]
    accolades=[]

    def addAccolade(self, accolade):
        self.accolades.append(accolade)
        print("New Accolade Acquired! Henceforth, you shall be known as:")
        print(self.name+", "+accolade)

    def addTitle(self, title):
        self.titles.append[title]
        print("New Title Acquired! Henceforth, you shall be known as:")
        print(title+" "+self.name)

    def examineSelf(self):
        print("You're known as",end=" ")
        for x in self.titles:
            print(x, end=" ")
        print(self.name, end=", ")
        for x in self.accolades:
            print(x, end=", ")
        print()
