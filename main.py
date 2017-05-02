from deck import Deck 
from hand import Hand 


startdeck= Deck()
startdeck.Shuffle()
first, second= startdeck.Cut()

'''plyr1crd=first.TakeFromTop()
plyr1crd.displayCard()

plyr2crd=second.TakeFromTop()
plyr2crd.displayCard()'''

plyr1win=first.Length()
plyr2win=second.Length()
deck=startdeck.Length()

if(plyr1win != deck and plyr2win != deck):
	plyr1crd=first.TakeFromTop()
    plyr1crd.displayCard()

    plyr2crd=second.TakeFromTop()
    plyr2crd.displayCard()

    if(plyr1crd>plyr2crd):
    	



