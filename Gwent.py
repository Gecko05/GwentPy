from GwentDatabase import *
from GwentScript import *
Game = GameBoard()
myHand = Hand([])
enemyHand = Hand([])
def SampleGame1():
    
#myHand.use(CurrentGame,card,)
    
    myDeck = Deck([ancientFoglet,swallowPotion,bitingFrost,mardroeme])
    myDeck.draw(myHand,4)

    enemyDeck = Deck([wyvern,alzursThunder,firstLight])
    enemyDeck.draw(enemyHand,3)

    me = Player(Game,myHand,0)
    enemy = Player(Game,enemyHand,1)

#myHand.use('Ancient Foglet',0,'r')
#myHand.use(Game,myHand.cards[0],0,0,'none','r') #PLAY FOGLET IN RANGE ROW
    me.play(ancientFoglet,0,False,'r')

#PLAY WYVERN IN SIEGE AND ATTACK ENEMY FOGLET IN RANGE
    enemy.play(wyvern,0,Game.board[0]['r'][0])
#enemyHand.use(Game,enemyHand.cards[0],1,0,Game.board[0]['r'][0],'s')

#USE SWALLOW POTION ON ANCIENT FOGLET
    me.play(swallowPotion,0,Game.board[0]['r'][0])

#USE ALZUR'S THUNDER ON ANCIENT FOGLET
    enemy.play(alzursThunder,0,Game.board[0]['r'][0])

#USE BITING FROST ON ENEMY WYVERN
    me.play(bitingFrost,0,'1s')

    Game.tick('start',1)
    Game.update()
    Game.display()
    print(Game.score)
    return 0

def SampleGame2():
    myDeck = Deck([ancientFoglet,ancientFoglet,ancientFoglet,ancientFoglet])
    myDeck.draw(myHand,4)

    enemyDeck = Deck([torrentialRain,bitingFrost,impenetrableFog])
    enemyDeck.draw(enemyHand,3)

    me = Player(Game,myHand,0)
    enemy = Player(Game,enemyHand,1)

    me.play(ancientFoglet,0,False,'m')
    me.play(ancientFoglet,0,False,'r')
    me.play(ancientFoglet,0,False,'r')
    me.play(ancientFoglet,0,False,'s')

    enemy.play(bitingFrost,0,'0m')
    enemy.play(impenetrableFog,0,'0r')
    enemy.play(torrentialRain,0,'0s')

    Game.display()
    Game.tick('start',0)
    Game.update()
    Game.display()
    print(Game.score)
    Game.tick('start',0)
    Game.update()
    Game.display()
    print(Game.score)
    Game.tick('start',0)
    Game.update()
    Game.display()
    print(Game.score)
    Game.tick('start',0)
    Game.update()
    Game.display()
    print(Game.score)
    Game.tick('start',0)
    Game.update()
    Game.display()
    print(Game.score)
    Game.tick('start',0)
    Game.update()
    Game.display()
    print(Game.score)
    return 0
    



