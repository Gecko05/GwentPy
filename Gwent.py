from GwentDatabase import *
from GwentScript import *
#myHand.use(CurrentGame,card,)
Game = GameBoard()

myHand = Hand([])
myDeck = Deck([AncientFoglet,SwallowPotion,BitingFrost])
myDeck.draw(myHand,3)

enemyDeck = Deck([Wyvern,AlzursThunder,FirstLight])
enemyHand = Hand([])
enemyDeck.draw(enemyHand,3)

me = Player(Game,myHand,0)
enemy = Player(Game,enemyHand,1)

#myHand.use('Ancient Foglet',0,'r')
#myHand.use(Game,myHand.cards[0],0,0,'none','r') #PLAY FOGLET IN RANGE ROW
me.play(AncientFoglet,0,False,'r')

#PLAY WYVERN IN SIEGE AND ATTACK ENEMY FOGLET IN RANGE
enemy.play(Wyvern,0,Game.board[0]['r'][0])
#enemyHand.use(Game,enemyHand.cards[0],1,0,Game.board[0]['r'][0],'s')

#USE SWALLOW POTION ON ANCIENT FOGLET
me.play(SwallowPotion,0,Game.board[0]['r'][0])

#USE ALZUR'S THUNDER ON ANCIENT FOGLET
enemy.play(AlzursThunder,0,Game.board[0]['r'][0])

#USE BITING FROST ON ENEMY WYVERN
me.play(BitingFrost,0,'1s')

Game.tick('start',1)

#USE CLEAR SKIES FROM FIRST LIGHT
enemy.play(FirstLight,0,False,'m',1)

Game.update()
Game.display()

print(Game.score)

