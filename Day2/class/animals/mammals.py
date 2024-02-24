class Mammals:
       
       def __init__(self):
           self.members = ["Lion", "Dog", "Elephant", "Cat"]

       
       def printMembers(self):
           print('Members of the Mammals class')
           for member in self.members:
               print('\t%s ' % member)


