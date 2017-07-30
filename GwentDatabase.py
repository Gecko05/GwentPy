########################################################################################################
#                       GWENT-PY DATABASE        GECKO05      26/07/17                                 #
########################################################################################################
from GwentScript import *
#Unit(faction,name,special,deploy,color,doom,row,base,loyal,stub,dw,tick',vet)
#   Special(name,ability,color,doom)
#       w = weather
#       d = damage
wyvern = Card("m","wyvern",False,"d3e",'b',False,'s',6)
ancientFoglet = Card("m","ancientFoglet",False,' ','b',False,'a',7,'L',False,'','sbf1')


torrentialRain = Card(False,"torrentialRain",True,"wr",'b')
bitingFrost = Card(False,"bitingFrost",True,"wb",'b')
impenetrableFog = Card(False,"impenetrableFog",True,"wf",'b')
alzursThunder = Card(False,"alzursThunder",True,"d7e",'b')
lacerate = Card(False,"lacerate",True,"d3r",'b')
swallowPotion = Card(False,"swallowPotion",True,"b8u",'b')
mutagen = Card(False,"mutagen",True,"t3u",'b',True)
spores = Card(False,"mutagen",True,"k3u",'b',True)
mardroeme = Card(False,"mardroeme",True,['x',mutagen,spores],'b',True)
clearSkies = Card(False,"clearSkies",True,"wc",'b',True)
rally = Card(False,"rally",True,"srbu",'b',)
firstLight = Card(False,"firstLight",True,['x',clearSkies,rally],'b')



