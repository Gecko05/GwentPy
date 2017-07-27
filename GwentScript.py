########################################################################################################
#                               GWENT-PY        GECKO05      26/07/17                                  #
########################################################################################################
class Unit:
    def __init__(self,name,base,deploy,color,row,loyal):
        self.name = name
        self.base = base
        self.deploy = deploy
        self.color = color
        self.row = row
        self.loyal = loyal
        self.power = base
        self.armor = 0
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
    def summon(self,game,player,row,pos):                                   #SUMMON UNIT FROM CARD
        if(self.unit.row=='a'):
            game.board[player][row].insert(pos,{'name':self.unit.name,'power':self.unit.power,'color':self.unit.color,'base':self.unit.base,'unit':self.unit})
        else:
            game.board[player][self.unit.row].insert(pos,{'name':self.unit.name,'power':self.unit.power,'color':self.unit.color,'base':self.unit.base,'unit':self.unit})


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
    def tick(self):
        for side in self.board:
            for row in side:
                if(self.weather[self.board.index(side)][row]=='r'):             #TORRENTIAL RAIN WEATHER
                    minunits = self.getRowMin(self.board.index(side),row)
                    if(minunits!=[]):
                        for unitpos in minunits:
                            self.board[self.board.index(side)][row][unitpos]['power'] = self.board[self.board.index(side)][row][unitpos]['power']-1
        
    def update(self):                        #UPDATE DESTROYED UNITS
        for side in self.board:
            for row in side:
                for unit in side[row]:
                    if(unit['power']<=0):
                        self.graveyard[self.board.index(side)].append(side[row].pop(side[row].index(unit)))

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

    def getRowMax(self,side,row):
        maxUnit = max(self.board[side][row],key=lambda x:x['power'])['power'] #GET MAX POWER ON THE ROW
        units = []
        auxRow = self.board[side][row][:]
        for unit in auxRow:
            if((unit['power']) == maxUnit) and (not(isGolden(unit))):
                units.append(auxRow.index(unit))
                auxRow[auxRow.index(unit)] = 0
        return units
    
    def getRowMin(self,side,row):
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
        if(card.special==False):
            card.summon(game,player,row,pos)                    #SUMMON UNIT CARDS
        elif(card.special==True):
            card.cast(game,player,target)                   #CAST SPECIAL CARDS
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
