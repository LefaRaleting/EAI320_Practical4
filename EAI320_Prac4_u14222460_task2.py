# -*- coding: utf-8 -*-
"""
Created on Thur May 28 17:40:05 2020

@author: Boris
"""
#Name: Lefa Raleting
#Student number: 14222460

import csv
import numpy as np


#class task1:
    #converting csv to array 
    #"""
    #Because I'm treating the past two moves by agent 1 and 2 as a single value
    #we have 81 possible combinations which 3^4. Second column we have the move that 
    #would have won that specific game. This made me select a 2d Array to represent these values

    #"""

    #""" 
    #first Id like to make DICTIONARY to compare possible 81 combinations to single value between 0
    #and 80
    #"""
movesIndex={
            "RRRR": 0,"RRRP": 1,"RRRS": 2,"RRPR": 3,"RRPP": 4,"RRPS": 5,"RRSR": 6,
            "RRSP": 7,"RRSS": 8,"RPRR":9,"RPRP": 10,"RPRS":11,"RPPR": 12,"RPPP": 13,
            "RPPS":14,"RPSR":15,"RPSP":16,"RPSS":17,"RSRR":18,"RSRP":19,"RSRS":20,
            "RSPR":21,"RSPP":22,"RSPS":23,"RSSR":24,"RSSP":25,"RSSS":26,"PRRR":27,
            "PRRP":28,"PRRS":29,"PRPR":30,"PRPP":31,"PRPS":32,"PRSR":33,"PRSP":34,
            "PRSS":35,"PPRR":36,"PPRP":37,"PPRS":38,"PPPR":39,"PPPP":40,"PPPS":41,
            "PPSR":42,"PPSP":43,"PPSS":44,"PSRR":45,"PSRP":46,"PSRS":47,"PSPR":48,
            "PSPP":49,"PSPS":50,"PSSR":51,"PSSP":52,"PSSS":53,"SRRR":54,"SRRP":55,
            "SRRS":56,"SRPR":57,"SRPP":58,"SRPS":59,"SRSR":60,"SRSP":61,"SRSS":62,
            "SPRR":63,"SPRP":64,"SPRS":65,"SPPR":66,"SPPP":67,"SPPS":68,"SPSR":69,
            "SPSP":70,"SPSS":71,"SSRR":72,"SSRP":73,"SSRS":74,"SSPR":75,"SSPP":76,
            "SSPS":77,"SSSR":78,"SSSP":79,"SSSS":80
            }
moveslist=[
        "RRRR","RRRP","RRRS","RRPR","RRPP","RRPS","RRSR",
        "RRSP","RRSS","RPRR","RPRP","RPRS","RPPR","RPPP",
        "RPPS","RPSR","RPSP","RPSS","RSRR","RSRP","RSRS",
        "RSPR","RSPP","RSPS","RSSR","RSSP","RSSS","PRRR",
        "PRRP","PRRS","PRPR","PRPP","PRPS","PRSR","PRSP",
        "PRSS","PPRR","PPRP","PPRS","PPPR","PPPP","PPPS",
        "PPSR","PPSP","PPSS","PSRR","PSRP","PSRS","PSPR",
        "PSPP","PSPS","PSSR","PSSP","PSSS","SRRR","SRRP",
        "SRRS","SRPR","SRPP","SRPS","SRSR","SRSP","SRSS",
        "SPRR","SPRP","SPRS","SPPR","SPPP","SPPS","SPSR",
        "SPSP","SPSS","SSRR","SSRP","SSRS","SSPR","SSPP",
        "SSPS","SSSR","SSSP","SSSS"
        ]
wining=["R","P", "S"] #ALL THE POSSIBLE MOVES THAT WIN

    #OPENING CSV FILE AND CREATING THE TWO ARRRAYS, ONE FOR PROIOR MOVES AND THE OTHER FOR 
    #THE MOVE THAT WOULD HAVE WON THE ROUND
prior=[] #This is for all the prior moves
target=[]# This is for all the moves that could have won

"""
with open('data.csv', 'r') as csvFile:
      reader = csv.reader(csvFile)
      
      for row in reader:
          rows=[]
          for word in row:
             if (word==row[1]):#if word is the second column it must add it to the target array
                    target.append(word)
                
             else:#else if it is the first column it must add that column to prior
                prior.append(word)
csvFile.close()
"""
#PROPABILITY letter appear at all         
def probabilityT(T):
        hits=0.0
        items=round(len(target),2)
        for k in range(0, len(target)):
            if(T==target[k]):#if the T value is equal to the target value add 1
                hits+=1.0
            else:
                continue
        return round(hits/items,10000)  #return the probability of that letter appearing 
    
#probaility that priors move appear at all
def probailityP(P):
        hits=0.0
        #L =movesIndex[P]
        items=round(len(prior),2)
        for k in range(0, len(prior)):
            if(P==prior[k]):#if the T value is equal to the target value add 1
                hits+=1.0
            else:
                continue
        return round(hits/items,100000)
#probability that prior move P give winning move T 
def probabilityPT(P,T):  
    hits=0.0
    items=0.0
    for k in range(0,len(prior)):
        if(T==target[k]):
            items+=1
            if(P==prior[k]):
                hits+=1
    return hits/items#probailityP(P)*probabilityT(T)#probailityP(P)
#probability of T given P
def probabilityTP(T,P):
    return round(probabilityPT(P,T)*probabilityT(T)/probailityP(P),100)

def change_probability(x):
    
    return 0

def probability():
    Probabilitytp=[] #This is for all the learned data
    row=[]
    for i in moveslist:
        row=[]
        for j in wining:
             row.append(probabilityTP(j,i))
        Probabilitytp.append(row)
    return Probabilitytp


#this code I use for implementation to determine which move it should select
#based on the probability of the past two moves P. the greatest probabilty move is the selected
def task1(P):
        if(probabilityTP("R",P)>(probabilityTP("P",P) and probabilityTP("S",P))):
            return 'R' 
        elif(probabilityTP("P",P)>(probabilityTP("R",P) and probabilityTP("S",P))):
            return 'P'
        else:
            return "S"
        


#______________________________task 2______________________________________________
#a=
a=[[0.1809688581314879, 0.6346020761245673, 0.1844290657439446], [0.3193931939319393, 0.29848298482984825, 0.38212382123821237], [0.27224112785610116, 0.37238697131745263, 0.35537190082644626], [0.12505125051250512, 0.7687576875768758, 0.1061910619106191], [0.5728643216080401, 0.2525125628140703, 0.1746231155778894], [0.24399260628465802, 0.3964879852125692, 0.3595194085027726], [0.08313077297034517, 0.8478366553232863, 0.0690325717063685], [0.22365988909426984, 0.6524953789279112, 0.12384473197781884], [0.21148036253776437, 0.38519637462235645, 0.4033232628398792], [0.35806132542037583, 0.26063303659742826, 0.3813056379821958], [0.07025061680301259, 0.07077002986625114, 0.8589793533307363], [0.278743961352657, 0.3449275362318841, 0.37632850241545895], [0.4162754303599374, 0.2003129890453834, 0.38341158059467917], [0.21423017107309483, 0.058709175738724716, 0.7270606531881803], [0.23975720789074353, 0.3793626707132018, 0.3808801213960546], [0.37152209492635024, 0.2520458265139116, 0.3764320785597381], [0.09478065962215818, 0.24239513288504644, 0.6628242074927952], [0.24400684931506847, 0.35787671232876705, 0.39811643835616434], [0.3702801461632156, 0.2626877791311409, 0.36703207470564353], [0.2910206718346253, 0.2929586563307493, 0.41602067183462527], [0.8091059392089534, 0.09042350247996946, 0.10047055831107718], [0.40138888888888885, 0.20694444444444446, 0.39166666666666666], [0.667910447761194, 0.22294776119402984, 0.10914179104477612], [0.8745847176079733, 0.0585548172757475, 0.06686046511627906], [0.39497041420118334, 0.21449704142011833, 0.39053254437869817], [0.22460776218001652, 0.6325350949628405, 0.14285714285714285], [0.8589853826311262, 0.07781599312123817, 0.06319862424763542], [0.0692383778437191, 0.8635014836795252, 0.06726013847675567], [0.3943661971830986, 0.38654147104851333, 0.21909233176838808], [0.14484451718494273, 0.23240589198036007, 0.6227495908346973], [0.10258407998961173, 0.8056096610829763, 0.09180625892741204], [0.35147744945567644, 0.3623639191290824, 0.28615863141524106], [0.4185078450208133, 0.29907140569964774, 0.28242074927953886], [0.06714975845410628, 0.8729468599033816, 0.05990338164251207], [0.3763277693474962, 0.39605462822458265, 0.2276176024279211], [0.13013698630136983, 0.6549657534246575, 0.21489726027397257], [0.3983333333333333, 0.21000000000000002, 0.3916666666666667], [0.06774040738986262, 0.06916153481762198, 0.8630980577925154], [0.12410714285714286, 0.21875, 0.6571428571428573], [0.35196589294173375, 0.2728564661297963, 0.3751776409284699], [0.1844155844155844, 0.17370129870129872, 0.6418831168831168], [0.40579135263784205, 0.28163427211424036, 0.3125743752479175], [0.37678571428571433, 0.26160714285714287, 0.36160714285714285], [0.1170170567235224, 0.11186037286790956, 0.771122570408568], [0.17995018679950187, 0.547945205479452, 0.27210460772104605], [0.38305709023941065, 0.26519337016574585, 0.35174953959484345], [0.3712574850299401, 0.3832335329341317, 0.24550898203592814], [0.6761790327425652, 0.08831480925202763, 0.235506158005407], [0.36886792452830186, 0.265566037735849, 0.365566037735849], [0.36703402012458075, 0.3799712505989458, 0.25299472927647343], [0.8526696606786426, 0.07497504990019958, 0.07235528942115768], [0.3848354792560801, 0.2188841201716738, 0.396280400572246], [0.41114457831325296, 0.35542168674698793, 0.23343373493975902], [0.7444055944055944, 0.20244755244755244, 0.053146853146853135], [0.06090133982947625, 0.7222898903775884, 0.21680876979293545], [0.37777777777777777, 0.3888888888888889, 0.23333333333333334], [0.2440828402366864, 0.37426035502958577, 0.38165680473372776], [0.25, 0.6540697674418604, 0.09593023255813952], [0.37873134328358204, 0.35727611940298504, 0.26399253731343286], [0.2658959537572254, 0.34929810074318746, 0.3848059454995871], [0.0793590232735597, 0.8422993768281826, 0.07834159989825765], [0.367109634551495, 0.3612956810631229, 0.27159468438538203], [0.26870163370593286, 0.3671539122957867, 0.36414445399828027], [0.22836095764272557, 0.12338858195211784, 0.6482504604051564], [0.06415094339622641, 0.06792452830188679, 0.8679245283018866], [0.2417739628040057, 0.38769670958512154, 0.37052932761087265], [0.6646706586826346, 0.11548331907613343, 0.21984602224123181], [0.07379012937230474, 0.07426928605654048, 0.8519405845711547], [0.22138554216867465, 0.4021084337349397, 0.3765060240963855], [0.3033944127365575, 0.3844998498047461, 0.31210573745869624], [0.09655688622754491, 0.11052894211576846, 0.7929141716566865], [0.2811188811188811, 0.36188811188811193, 0.356993006993007], [0.2708585247883918, 0.1807738814993954, 0.5483675937122128], [0.37234944868532655, 0.3672603901611535, 0.26039016115351993], [0.7867620751341681, 0.11234347048300536, 0.10089445438282649], [0.6598812553011026, 0.12383375742154369, 0.2162849872773537], [0.41415662650602403, 0.3629518072289157, 0.2228915662650602], [0.870803229919252, 0.06374840628984275, 0.06544836379090521], [0.3069767441860465, 0.3806797853309481, 0.31234347048300537], [0.39864003399915, 0.3501912452188695, 0.25116872078198044], [0.6345933562428407, 0.18928980526918673, 0.1761168384879725]]
#print a

prev=input
if prev=="":
    play=np.random.choice(['R', 'P', 'S'])
    prv=[]
    check=""
    history=[]
   
    #check.split[1:]
else:
    if(len(check)<4):
        play=np.random.choice(['R', 'P', 'S'])
        check+=prev
    else:
        history.append(check) #this is to store all the online information
        change_probability(history )
        
        if(a[movesIndex[check]][0]>(a[movesIndex[check]][1] and a[movesIndex[check]][2])):
            play="R"
        elif(a[movesIndex[check]][1]>(a[movesIndex[check]][0] and a[movesIndex[check]][2])):
            play ="P"
        else:
            play="S"
        check+=prev
       
        check= check[1:]
     
output= play


  