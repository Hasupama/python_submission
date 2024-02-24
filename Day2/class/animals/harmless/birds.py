
class Birds:
           	
           	def __init__(self):
           		self.members = ["Parakeets", "Pionus Parrot", "Pigeon","Hyacinth Macaw"]

           	
           	def printMembers(self):
           		print('These are the harmless birds')
           		for member in self.members:
           			print('\t%s ' % member)