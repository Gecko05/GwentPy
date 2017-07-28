########################################################################################################
#                       GWENT-PY DATABASE        GECKO05      26/07/17                                 #
########################################################################################################
from GwentScript import *
#Unit(name,base pwr,deploy,color,row,loyal,doom,stubborn,deathwish)
#   Special(name,ability,color,doom)
#       w = weather
#       d = damage
wyvern = Unit("wyvern",6,"d3e",'b','s')
Wyvern = Card("wyvern",wyvern)
ancientFoglet = Unit("ancientFoglet",7,'n','b','a')
AncientFoglet = Card("ancientFoglet",ancientFoglet)

torrentialRain = Special("torrentialRain","wr",'b')
TorrentialRain = Card("torrentialRain",torrentialRain,True)
bitingFrost = Special("bitingFrost","wb",'b')
BitingFrost = Card("bitingFrost",bitingFrost,True)
impenetrableFog = Special("impenetrableFog","wf",'b')
ImpenetrableFog = Card("impenetrableFog",impenetrableFog,True)

alzursThunder = Special("alzursThunder","d7e",'b')
AlzursThunder = Card("alzursThunder",alzursThunder,True)
lacerate = Special("lacerate","d3r",'b')
Lacerate = Card("lacerate",lacerate,True)

swallowPotion = Special("swallowPotion","b8u",'b')
SwallowPotion = Card("swallowPotion",swallowPotion,True)

mutagen = Special("mutagen","t3u",'b',True)
spores = Special("mutagen","w3u",'b',True)
Mutagen = Card("mutagen",mutagen,True)
Spores = Card("spores",spores,True)
mardroeme = Special("mardroeme",['x',Mutagen,Spores],'b',True)
Mardroeme = Card("mardroeme",mardroeme,True)

clearSkies = Special("clearSkies","wc",'b',True)
rally = Special("rally","srbu",'b',)
ClearSkies = Card("clearSkies",clearSkies,True)
Rally = Card("rally",rally,True)
firstLight = Special("firstLight",['x',ClearSkies,Rally],'b')
FirstLight = Card("firstLight",firstLight,True)


