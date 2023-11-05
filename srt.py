from random import randrange
print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")
print("==============================================================")
print(" PATI 1) MASTER STR (index, split, replace, lower, upper, title)") 
print("==============================================================")
print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")
# 1 )Nan yon chenn karaktè, mete tout karaktè yo an miniskil
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
karakte=input("1) depi w antre yn fraz ou yn mo ki gen majiskil ladanl lap konveti an miniskil :").lower()
print(karakte)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
# 2) Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas. Epi afiche yon lis ki gen chak eleman yo. Ekzanp:
karakte=input(" 2) entre yn chenn karakte pwogram nan ap koupe l tou kote l jwenn espas pou voye yo nn yn lis :").split(" ")
men_lis_la=karakte
print(men_lis_la)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
# 3) Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil
karakte=input(" 3) entre yn fraz pwogram nan ap mete tout premye let mo yo an majiskil").title()
print(karakte)
karakte=input("4) entre yn fraz pwogram nan ap rekipere chak premye let yo pou l mete yo ansann")
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
# 4) Nan yon chenn karaktè, rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo.
mt=karakte.split()
prm=[kas[0] for kas in mt ]
rezilta=''.join(prm)
print(rezilta)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
# 5) Ranplase tout karaktè "a" ki nan yon chenn pa "@"
karakte=input(" 5) entre yn fraz pwogram nan ap ranplase tout a yo pa @ ").replace("a","@").replace("A","@")
print(karakte)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
# 6) Mete yon chenn karaktè devan dèyè, answit mete l an majiskil. Ekzanp:
karakte=input(" 6) entre chenn karakte epi pwogwam nn ap mete l devan deye e an majiskil").upper()
print(f"men chenn karakte ou t antren: {karakte}")
invers=karakte[::-1]
print(f"men sa w t rantre a a lenves: {invers}")
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
# 7) Afiche endeks premye karaktè "a" ki nan yon chenn. 
karakte=input("7) entre yn chenn karakte program nan ap bay index premye let a li jwenn nan")
endeks=karakte.find('a')
if endeks != -1:
    print("endeks premye a ki gen nan karakte a se:",endeks)
else:
    print("chenn sa pa gen let a ladan l")    
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
# 8) Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil). Ekzanp:
karakte=input("entre yn chenn pwogram nan ap afiche tout total: a ")  
som = 0
for i, chenn in enumerate(karakte):
    if chenn == 'a' or chenn=='A':
        som += i
print("Somme des indices des lettres 'a' :", som)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
# 9) Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil). Ekzanp
karakte=input(" 9)entre yn chenn de karakte ki komanse pa :a pwogram nan ap detemine index premye elemen")
endeks=[]
for i in range(len(karakte)):
    if karakte[i]=='a':
        endeks.append(i) 
print(f"endeks tout karakte a ki nan chenn sa c : {endeks}")
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
# 10) Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo)
karakte=input("entre yn chenn karakte ki gen espas pwogram nan ap retire tout esps yo").replace(" ","")
print(f"men chenn karakte san espas : {karakte}")
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
   #PATI 2
print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")
print("===============================================================")
print(" PATI 2) MASTER LIST (Union & Intersection & Lis comprehension)") 
print("===============================================================")
print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")
# 1) Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
nonb=int (input("wap antre yn nonb epi pwogram nan ap kalkile tout nonb ki divizib pa 2 nan enteval la"))
lis_la=[]
for i in range(nonb+1):
    if i % 2 ==0:
        lis_la.append(i)
print(lis_la)       
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
# 2 )Ou gen yon lis antye, konvèti l an yon lis chenn
antye=[1,2,3,4,5,6,7,8,9]
print("men lis antye map chanje an chenn nan:",antye)
lis_chenn=[]
for i in antye:
    lis_chenn.append(str(i))
print(lis_chenn)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
# 3) Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
lis_chenn_miniskil=['bonjour','bonsoir','salut']
chenn_majiskil=[]
print("men lis ki an miniskil la",lis_chenn_miniskil)
for i in lis_chenn_miniskil:
    chenn_majiskil.append(i.upper())
print("men lis lan an majiskil",chenn_majiskil)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
#Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
lis_mw=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print("men lis m t gen avan",lis_mw)
lis_poum=[]
for i in range(len(lis_mw)):
    if i % 3==0:
        lis_poum.append(lis_mw[i])
print("men lis ki divisib pa 3 yo: ",lis_poum)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
#Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl. Ekzanpgit
