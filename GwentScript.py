########################################################################################################
#                               GWENT-PY        GECKO05      26/07/17                                  #
########################################################################################################
import random


class Card:
    def __init__(self,name,special=False,deploy='',color='b',doom=False,row='a',base=0,loyal='L',stub=False,dw='',tick='',vet=False):
        self.name = name
        self.base = base
        self.deploy = deploy
        self.color = color
        self.row = row
        self.loyal = loyal
        self.power = base
        self.armor = 0
        self.doom = doom
        self.stub = stub
        self.dw = dw
        self.resi = False
        self.lock = False
        self.tick = tick
        self.vet = vet
        self.special = special
    def deployUnit(self,target = False):                                #DEPLOY ABILITY FOR CARD
        '''target optional'''
        print(self.name)
        if(self.deploy[0])=='d' and target!= False and (not(isGolden(target))):
            target['power'] = target['power'] - int(self.deploy[1])
    def summon(self,game,player,row,pos):                                   #SUMMON UNIT FROM CARD
        if(self.row=='a'):
            game.board[player][row].insert(pos,{'name':self.name,'power':self.power,'color':self.color,'base':self.base,
                                                'unit':self,'resi':self.resi,'lock':self.lock,'tick':self.tick})
        else:
            game.board[player][self.row].insert(pos,{'name':self.name,'power':self.power,'color':self.color,'base':self.base,
                                                          'unit':self,'resi':self.resi,'lock':self.lock,'tick':self.tick})
    def cast(self,game,player,target,sel=0):                                  #CAST FOR SPECIAL CARDS
        if(self.deploy[0])=='d' and target!= False and not(isGolden(target)):               #DAMAGE
            if(self.deploy[2])=='e':                              #SINGLE TARGET
                target['power'] = target['power'] - int(self.deploy[1])
            elif(self.deploy[2])=='r':                            #ROW DAMAGE
                side = int(target[0])
                row = target[1]
                for unitpos in game.getRowUnits(side,row):
                    game.board[side][row][unitpos]['power'] = game.board[side][row][unitpos]['power'] - int(self.deploy[1])
        elif(self.deploy[0])=='w' and target!=False:
            game.weather[int(target[0])][target[1]] = self.deploy[1]  #CAST WEATHER
        elif(self.deploy)=='wc':
            game.weather[player] = {"s":'',"r":'',"m":''}                           #CLEAR WEATHER       
        elif(self.deploy[0])=='b' and target!=False and not(isGolden(target)):
            target['power'] = target['power'] + int(self.deploy[1])   #BOOST SPECIAL CARD
        elif(self.deploy[0])=='x':
            self.deploy[sel].cast(game,player,target,sel)             #CAST INSIDE SPECIAL
        elif(self.deploy[0])=='t' and target!= False and not(isGolden(target)):     #STRENGTHTEN UNIT
            target['power'] = target['base'] + int(self.deploy[1])
            target['base'] = target['base'] + int(self.deploy[1])
        elif(self.deploy[0])=='k' and target!= False and not(isGolden(target)):     #WEAKEN UNIT
            target['power'] = target['base'] - int(self.deploy[1])
            target['base'] = target['base'] - int(self.deploy[1])
        if(self.doom==False):
            game.graveyard[player].insert(0,self)   

####################################
            
#0 is self
#1 is enemy
########################################################################################################
class GameBoard:
    def __init__(self):
        self.board = [{"s":[],"r":[],"m":[]},{"s":[],"r":[],"m":[]}]
        self.weather = [{"s":'',"r":'',"m":''},{"s":'',"r":'',"m":''}]
        self.score = [0,0]
        self.played = {0:[],1:[]}
        self.graveyard = {0:[],1:[]}
    def change(self,board,player):
        self.board[player] = board

    def update(self):                        #UPDATE DESTROYED/BANISHED UNITS
        for side in self.board:
            for row in side:
                for unit in side[row]:
                    if(unit['base']<=0):
                        side[row].pop(side[row].index(unit))
                    elif(unit['power']<=0):
                        if(unit['unit'].doom == True):
                            side[row].pop(side[row].index(unit))
                        else: 
                            self.graveyard[self.board.index(side)].insert(0,side[row].pop(side[row].index(unit)))
                            self.graveyard[self.board.index(side)][0]['power'] = self.graveyard[self.board.index(side)][0]['base']
                            

        self.score = [0,0]                   #UPDATE SCORE
        for side in self.board:
            for row in side:
                for unit in side[row]:
                    self.score[self.board.index(side)] = self.score[self.board.index(side)] + unit['power']
                    
    def tick(self,turnphase,side):
        if(turnphase=='start'): 
            for row in self.board[side]:
                for unit in self.board[side][row]:                  #FOR EVERY UNIT
                    if(unit['lock']==False):                        #IF UNLOCKED
                        if(unit['tick'][0]=='s'):                   #START OF TURN
                            
                            if(unit['tick'][1]=='b'):               #BOOST
                                
                                if(unit['tick'][2]=='f'):           #WEATHER FOG PRESENT
                                    if 'f' in (self.weather[TogTurn(side)]['r'] or self.weather[TogTurn(side)]['m'] or self.weather[TogTurn(side)]['s']):
                                        unit['power'] = unit['power'] + int(unit['tick'][3])                       
            
            for row in self.board[side]:
                if(self.weather[side][row]=='r'):             #TORRENTIAL RAIN WEATHER
                    minunits = self.getRowMinUnits(side,row)
                    if(minunits!=[]):
                        for unitpos in minunits:
                            self.board[side][row][unitpos]['power'] = self.board[side][row][unitpos]['power']-1
                if(self.weather[side][row]=='b'):             #BITING FROST DAMAGE
                    minunits = self.getRowMinUnits(side,row)
                    if(minunits!=[]):
                        unitpos = random.choice(minunits)
                        self.board[side][row][unitpos]['power'] = self.board[side][row][unitpos]['power']-2
                if(self.weather[side][row]=='f'):             #IMPENETRABLE FOG DAMAGE
                    maxunits = self.getRowMaxUnits(side,row)
                    if(maxunits!=[]):
                        unitpos = random.choice(maxunits)
                        self.board[side][row][unitpos]['power'] = self.board[side][row][unitpos]['power']-2
        self.update()

    def display(self):                 #####DISPLAY THE CURRENT BOARD######
        print('===============')
        for side in self.board:
            if(side==self.board[0]):
                print('--- Player ---')
            else:
                print('--- Enemy ---')
            for row in side:
                if(row=='m'):
                    print('\nMelee --',end=' ')
                elif(row=='r'):
                    print('\nRange --',end=' ')
                else:
                    print('\nSiege --',end=' ')
                for unit in side[row]:
                    print(unit['name'] + '/' + str(unit['power']),end=" ")
            print('\n')

    def getRowMaxUnits(self,side,row):
        if(self.board[side][row]!=[]):
            maxUnit = max(self.board[side][row],key=lambda x:x['power'])['power'] #GET MAX POWER ON THE ROW
            units = []
            auxRow = self.board[side][row][:]
            for unit in auxRow:
                if((unit['power']) == maxUnit) and (not(isGolden(unit))):
                    units.append(auxRow.index(unit))
                    auxRow[auxRow.index(unit)] = 0
        else:
            units = []
        return units
    
    def getRowMinUnits(self,side,row):
        if(self.board[side][row]!=[]):
            minUnit = min(self.board[side][row],key=lambda x:x['power'])['power'] #GET MIN POWER ON THE ROW
            units = []
            auxRow = self.board[side][row][:]
            for unit in auxRow:
                if((unit['power']) == minUnit) and (not(isGolden(unit))):
                    units.append(auxRow.index(unit))
                    auxRow[auxRow.index(unit)] = 0
        else:
            units = []
        return units
    def getRowUnits(self,side,row):
        if(self.board[side][row]!=[]):
            units = []
            auxRow = self.board[side][row][:]
            for unit in auxRow:
                if(not(isGolden(unit))):
                    units.append(auxRow.index(unit))
                    auxRow[auxRow.index(unit)] = 0
        else:
            units = []
        return units
        

            
###########################################################################################################
class Hand:
    def __init__(self,cards):
        self.cards = cards
    def use(self,game,card,player,pos=0,target=False,row='m',sel=0):                   #USE CARD FROM HAND
        '''myHand.use(CurrentGame,myHand.cards[2],0)'''
        if(card.special==False):
            if(card.row!='a'):
                row = card.row
            if(target!=False):
                card.summon(game,player,row,pos)                    #SUMMON UNIT CARDS
                game.board[player][row][pos]['unit'].deployUnit(target) #DEPLOY UNIT WITH TARGET
            elif(target==False):
                card.summon(game,player,row,pos)
                game.board[player][row][pos]['unit'].deployUnit()       #DEPLOY UNIT TARGETLESS
        elif(card.special==True):
            card.cast(game,player,target,sel)                           #CAST SPECIAL CARDS
        game.played[player].append(self.cards.pop(self.cards.index(card))) #REMOVE A CARD FROM HAND
    def display(self):
        for card in self.cards:
            print(card.name)
####################################    
class Deck:
    def __init__(self,cards):
        self.cards = cards
    def display(self):
        for card in self.cards:
            print(card.name)
    def draw(self,hand,number):
        for i in range(0,number):
            hand.cards = hand.cards + [self.cards.pop(0)] #DRAW A CARD FROM DECK

###################################
class Player:
    def __init__(self,game,hand,num):
        self.hand = hand
        self.num = num
        self.game = game
    def play(self,card,pos=0,target=False,row='m',sel=0):
        self.game.tick('start',self.num)
        self.hand.use(self.game,self.hand.cards[CardPos(card,self.hand)],self.num,pos,target,row,sel)
        self.game.tick('end',self.num)
        

###################################                 CARD PROPERTIES FUNCTIONS

def isGolden(unit):
    if(unit['color']=='g'):
       return True
    else:
       return False

#----------------------------------
def CardPos(card,hand):
    return hand.cards.index(card)

def TogTurn(turn):
    if(turn==1):
        return 0
    else:
        return 1
