########################################################################################################
#                       GWENT-PY DATABASE        GECKO05      26/07/17                                 #
########################################################################################################
from GwentScript import *
#Unit(name,base pwr,deploy,color,row,loyal,doom,stubborn,deathwish)
#       w = weather
#       d = damage
wyvern = Unit("wyvern",6,"d3e",'b','s')
Wyvern = Card("wyvern",wyvern)
ancientFoglet = Unit("ancientFoglet",7,'n','b','a')
AncientFoglet = Card("ancientFoglet",ancientFoglet)

torrentialRain = Special("torrentialRain","wr")
TorrentialRain = Card("torrentialRain",torrentialRain,True)
bitingFrost = Special("bitingFrost","wb")
BitingFrost = Card("bitingFrost",bitingFrost,True)
impenetrableFog = Special("impenetrableFog","wf")
ImpenetrableFog = Card("impenetrableFog",impenetrableFog,True)

alzursThunder = Special("alzursThunder","d7e")
AlzursThunder = Card("alzursThunder",alzursThunder,True)
lacerate = Special("lacerate","d3r")
Lacerate = Card("lacerate",lacerate,True)

swallowPotion = Special("swallowPotion","b8u")
SwallowPotion = Card("swallowPotion",swallowPotion,True)

