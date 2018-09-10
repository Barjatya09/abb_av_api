"""
follow abb naming convention for each class
"""
class PlantInformation(object):
	def __init__(self, responseJSON):
		self.plantName = responseJSON['plantName']
		self.plantState = responseJSON['plantState']
		self.portfolioEID = responseJSON['portfolioEID']
		self.plantEntityID = responseJSON['plantEntityID']
		self.plantGroupEID = responseJSON['plantName']
		self.plantDescription = responseJSON['plantDescription']
