from deck import Deck 
from hand import Hand 


startdeck= Deck()
startdeck.Shuffle()
first, second= startdeck.Cut()

plyr1crd=first.TakeFromTop()


plyr2crd=second.TakeFromTop()


plyr1win=first.Length()
plyr2win=second.Length()
deck=startdeck.Length()

if(plyr1win != deck and plyr2win != deck):
	plyr1crd=first.TakeFromTop()
	plyr1crd.displayCard()

	plyr2crd=second.TakeFromTop()
	plyr2crd.displayCard()

	if(plyr1crd>plyr2crd):
		first.AddToBottom(plyr1crd)
		first.AddToBottom(plyr2crd)
		print("Player 1 won that round! He gets both cards!")
	if(plyr2crd>plyr1crd):
		second.AddToBottom(plyr1crd)
		second.AddToBottom(plyr2crd)
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
    	





