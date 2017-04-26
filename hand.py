import random 
from card import Card
class Hand:
	def __init__(self):
		self.value = []
		self.validSuits=["Clubs","Spades","Hearts","Diamonds"]
		self.validRanks=["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
		for suit in self.validSuits:
			for rank in self.validRanks:
			    self.value.append(Card(rank,suit))
        def Cut(self):
    	    first= Hand()
    	    second= Hand()
    	    halfway= len(self.value)/2
    	    first.value= self.value[halfway:]
    	    second.value= self.value[:halfway]
    	    self.value= []
    	    return first,second
  











'''
    def Cut(self):
        first = Hand()
        second = Hand()
        halfway = len(self.value)/2
        first.value = self.value[halfway:]
        second.value=self.value[:halfway]
        self.value = []
        return first,second
'''