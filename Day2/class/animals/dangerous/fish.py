
class Fish:


       def __init__(self):
           self.members = ["Stonefish", "Tigerfish", "Shark", "Pufferfish"]

       
       def printMembers(self) :
           print('These are the dangerous fish')
           for member in self.members:
               print('\t%s ' % member)