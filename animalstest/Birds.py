class Birds:
	def __init__(self):
		self.members = ['Sparrow', 'Robin', 'Duck']

	def printMembers(self):
		print "Printing Bird Class member"
		for member in self.members:
			print '\t%s ' %member
