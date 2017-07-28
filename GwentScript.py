########################################################################################################
#                               GWENT-PY        GECKO05      26/07/17                                  #
########################################################################################################
import random

class Unit:
    def __init__(self,name,base,deploy,color,row,loyal='L',doom='N',stub='N',dw='',tick=''):
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
        self.resi = True
        self.lock = False
        self.tick = tick
    def deployUnit(self,target = False):                                #DEPLOY ABILITY FOR CARD
        '''target optional'''
        if(self.deploy[0])=='d' and target!= False and (not(isGolden(target))):
            target['power'] = target['power'] - int(self.deploy[1])
####################################
class Special:
    def __init__(self,name,ability):
        self.name = name
        self.ability = ability
####################################
class Card:
    def __init__(self,name,unit,special=False):
        self.name = name
        self.unit = unit
        self.special = special
    def cast(self,game,player,target):                                  #CAST FOR SPECIAL CARDS
        if(self.unit.ability[0])=='d' and target!= False:               #DAMAGE
            if(self.unit.ability[2])=='e':                              #SINGLE TARGET
                target['power'] = target['power'] - int(self.unit.ability[1])
            elif(self.unit.ability[2])=='r':                            #ROW DAMAGE
                side = int(target[0])
                row = target[1]
                for unitpos in game.getRowUnits(side,row):
                    game.board[side][row][unitpos]['power'] = game.board[side][row][unitpos]['power'] - int(self.unit.ability[1])
        elif(self.unit.ability[0])=='w' and target!=False:
            game.weather[int(target[0])][target[1]] = self.unit.ability[1]  #CAST WEATHER
        elif(self.unit.ability[0])=='b' and target!=False:
            target['power'] = target['power'] + int(self.unit.ability[1])
    def summon(self,game,player,row,pos):                                   #SUMMON UNIT FROM CARD
        if(self.unit.row=='a'):
            game.board[player][row].insert(pos,{'name':self.unit.name,'power':self.unit.power,'color':self.unit.color,'base':self.unit.base,'unit':self.unit})
        else:
            game.board[player][self.unit.row].insert(pos,{'name':self.unit.name,'power':self.unit.power,'color':self.unit.color,'base':self.unit.base,
                                                          'unit':self.unit,'resi':self.unit.resi,'lock':self.unit.lock})


#0 is self
#1 is enemy
########################################################################################################
class GameBoard:
    def __init__(self):
        self.board = [{"s":[],"r":[],"m":[]},{"s":[],"r":[],"m":[]}]
        self.weather = [{"s":0,"r":0,"m":0},{"s":0,"r":0,"m":0}]
        self.score = [0,0]
        self.played = {0:[],1:[]}
        self.graveyard = {0:[],1:[]}
    def change(self,board,player):
        self.board[player] = board
    def tick(self,turnphase,side):
        if(turnphase=='start'):
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

    def update(self):                        #UPDATE DESTROYED/BANISHED UNITS
        for side in self.board:
            for row in side:
                for unit in side[row]:
                    if(unit['power']<=0):
                        if(unit['unit'].doom == 'D'):
                            side[row].pop(side[row].index(unit))
                        else: 
                            self.graveyard[self.board.index(side)].append(side[row].pop(side[row].index(unit)))
                            self.graveyard[self.board.index(side)][-1]['power'] = self.graveyard[self.board.index(side)][-1]['base']
                            

        self.score = [0,0]                   #UPDATE SCORE
        for side in self.board:
            for row in side:
                for unit in side[row]:
                    self.score[self.board.index(side)] = self.score[self.board.index(side)] + unit['power']

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
        maxUnit = max(self.board[side][row],key=lambda x:x['power'])['power'] #GET MAX POWER ON THE ROW
        units = []
        auxRow = self.board[side][row][:]
        for unit in auxRow:
            if((unit['power']) == maxUnit) and (not(isGolden(unit))):
                units.append(auxRow.index(unit))
                auxRow[auxRow.index(unit)] = 0
        return units
    
    def getRowMinUnits(self,side,row):
        minUnit = min(self.board[side][row],key=lambda x:x['power'])['power'] #GET MIN POWER ON THE ROW
        units = []
        auxRow = self.board[side][row][:]
        for unit in auxRow:
            if((unit['power']) == minUnit) and (not(isGolden(unit))):
                units.append(auxRow.index(unit))
                auxRow[auxRow.index(unit)] = 0
        return units
    def getRowUnits(self,side,row):
        units = []
        auxRow = self.board[side][row][:]
        for unit in auxRow:
            if(not(isGolden(unit))):
                units.append(auxRow.index(unit))
                auxRow[auxRow.index(unit)] = 0
        return units

            
###########################################################################################################
class Hand:
    def __init__(self,cards):
        self.cards = cards
    def use(self,game,card,player,pos=0,target='none',row='m'):                   #USE CARD FROM HAND
        '''myHand.use(CurrentGame,myHand.cards[2],0)'''
        if(card.special==False and target!='none'):
            card.summon(game,player,row,pos)                    #SUMMON UNIT CARDS
            game.board[player][row][pos]['unit'].deployUnit(target) #DEPLOY UNIT WITH TARGET
        elif(card.special==False and target=='none'):
            card.summon(game,player,row,pos)
            game.board[player][row][pos]['unit'].deployUnit()       #DEPLOY UNIT TARGETLESS
        elif(card.special==True):
            card.cast(game,player,target)                           #CAST SPECIAL CARDS
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

###################################                 CARD PROPERTIES FUNCTION

def isGolden(unit):
    if(unit['color']=='g'):
       return True
    else:
       return False
