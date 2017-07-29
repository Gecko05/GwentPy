########################################################################################################
#                       GWENT-PY DATABASE        GECKO05      26/07/17                                 #
########################################################################################################
from GwentScript import *
#Unit(name,special,deploy,color,doom,row,base,loyal,stub,dw,tick',vet)
#   Special(name,ability,color,doom)
#       w = weather
#       d = damage
wyvern = Card("wyvern",False,"d3e",'b',False,'s',6)
ancientFoglet = Card("ancientFoglet",False,' ','b',False,'a',7)


torrentialRain = Card("torrentialRain",True,"wr",'b')
bitingFrost = Card("bitingFrost",True,"wb",'b')
impenetrableFog = Card("impenetrableFog",True,"wf",'b')
alzursThunder = Card("alzursThunder",True,"d7e",'b')
lacerate = Card("lacerate",True,"d3r",'b')
swallowPotion = Card("swallowPotion",True,"b8u",'b')
mutagen = Card("mutagen",True,"t3u",'b',True)
spores = Card("mutagen",True,"w3u",'b',True)
mardroeme = Card("mardroeme",True,['x',mutagen,spores],'b',True)
clearSkies = Card("clearSkies",True,"wc",'b',True)
rally = Card("rally",True,"srbu",'b',)
firstLight = Card("firstLight",True,['x',clearSkies,rally],'b')



