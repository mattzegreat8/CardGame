from deck import Deck 
from hand import Hand 


startdeck= Deck()
startdeck.Shuffle()
first, second= startdeck.Cut()
print(first)