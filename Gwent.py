from GwentDatabase import *
from GwentScript import *
#myHand.use(CurrentGame,card,)
Game = GameBoard()

myHand = Hand([])
myDeck = Deck([AncientFoglet,SwallowPotion,BitingFrost])
myDeck.draw(myHand,3)

enemyDeck = Deck([Wyvern,AlzursThunder])
enemyHand = Hand([])
enemyDeck.draw(enemyHand,2)

#myHand.use('Ancient Foglet',0,'r')
myHand.use(Game,myHand.cards[0],0,0,'none','r') #PLAY FOGLET IN RANGE ROW

#PLAY WYVERN IN SIEGE AND ATTACK ENEMY FOGLET IN RANGE
enemyHand.use(Game,enemyHand.cards[0],1,0,Game.board[0]['r'][0],'s')

#USE SWALLOW POTION ON ANCIENT FOGLET
myHand.use(Game,myHand.cards[0],0,0,Game.board[0]['r'][0])

#USE ALZUR'S THUNDER ON ANCIENT FOGLET
enemyHand.use(Game,enemyHand.cards[0],1,0,Game.board[0]['r'][0])

#USE BITING FROST ON ENEMY WYVERN
myHand.use(Game,myHand.cards[0],0,0,'1s')

Game.update()
Game.display()

print(Game.score)

