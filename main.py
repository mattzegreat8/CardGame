from deck import Deck 
from hand import Hand 


startdeck= Deck()
startdeck.Shuffle()
deck=startdeck.Length()



first, second= startdeck.Cut()
plyr1win=first.Length()
plyr2win=second.Length()



plyr1crd=first.TakeFromTop()
plyr2crd=second.TakeFromTop()


'''plyr1win=first.Length()
plyr2win=second.Length()
deck=startdeck.Length()
'''
while(plyr1win != deck and plyr2win != deck):

	plyr1crd=first.TakeFromTop()
	plyr1crd.displayCard()

	plyr2crd=second.TakeFromTop()
	plyr2crd.displayCard()

	print(plyr1win)
	print(plyr2win)
	print(deck)

	if(plyr1crd>plyr2crd):
		first.AddToBottom(plyr1crd)
		first.AddToBottom(plyr2crd)

		plyr1win += 2
		plyr2win -= 2
		print("Player 1 won that round! He gets both cards!")
	if(plyr2crd>plyr1crd):
		second.AddToBottom(plyr1crd)
		second.AddToBottom(plyr2crd)
		plyr2win += 2
		plyr1win -= 2

		print("Player 2 won that round! He gets both cards!")
	if(plyr1crd==plyr2crd):
		plyr1crd1=first.TakeFromTop()
		plyr1crd2=first.TakeFromTop()
		plyr1crd3=first.TakeFromTop()
		plyr1crd4=first.TakeFromTop()
		plyr1crd4.displayCard()
		plyr2crd1=second.TakeFromTop()
		plyr2crd2=second.TakeFromTop()
		plyr2crd3=second.TakeFromTop()
		plyr2crd4=second.TakeFromTop()
		plyr2crd4.displayCard()

	if(plyr1win == deck):
		print("Player 1 won the game")
	if(plyr2win == deck):
		print("Player 2 won the game")






    	





