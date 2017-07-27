from GwentDatabase import *
from GwentScript import *

Game = GameBoard()

myHand = Hand([])
myDeck = Deck([AncientFoglet,Wyvern,AncientFoglet])
myDeck.draw(myHand,2)

enemyDeck = Deck([AlzursThunder,Wyvern,Wyvern])
enemyHand = Hand([])
enemyDeck.draw(enemyHand,3)

myHand.use(Game,myHand.cards[0],0,0,'none','r')

enemyHand.use(Game,enemyHand.cards[0],1,0,Game.board[0]['r'][0])
enemyHand.use(Game,enemyHand.cards[0],1,0)
enemyHand.use(Game,enemyHand.cards[0],1,0)

Game.display()

Game.board[1]['s'][0]['unit'].deployUnit(Game.board[0]['r'][0])
Game.board[1]['s'][1]['unit'].deployUnit(Game.board[0]['r'][0])

BitingFrost.cast(Game,0,'1s')

Game.display()
Game.update()

print(Game.score)

Lacerate.cast(Game,0,'1s')
