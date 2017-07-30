from GwentDatabase import *
from GwentScript import *
Game = GameBoard()
myHand = Hand([])
enemyHand = Hand([])

myDeck = Deck([ancientFoglet,impenetrableFog,ancientFoglet,ancientFoglet],0)
##myDeck.draw(myHand,4)

enemyDeck = Deck([torrentialRain,bitingFrost,impenetrableFog,mardroeme],1)
##enemyDeck.draw(enemyHand,4)

##me = Player(Game,myHand,0)
##enemy = Player(Game,enemyHand,1)
##
##me.play(0,0,False,'m')  #A FOGLET
##Game.display()
##enemy.play(0,0,'0m')    #RAIN
##Game.display()
##    
##me.play(0,0,'1r')   #FOG
##Game.display()
##enemy.play(0,0,'0r') #FROST
##Game.display()
##    
##me.play(0,0,False,'r')
##Game.display()
##enemy.play(0,0,'0s') #FOG
##Game.display()
##    
##me.play(0,0,False,'s')
##Game.display()
##enemy.play(0,0,Game.board[0]['r'][0],'m',2) #MARDROEME
##Game.display()




