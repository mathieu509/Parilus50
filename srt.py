print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")
print(" PATI 1) MASTER STR (index, split, replace, lower, upper, title)") 
print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
karakte=input("1) depi w antre yn fraz ou yn mo ki gen majiskil ladanl lap konveti an miniskil :").lower()
print(karakte)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
karakte=input(" 2) entre yn chenn karakte pwogram nan ap koupe l tou kote l jwenn espas pou voye yo nn yn lis :").split(" ")
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
men_lis_la=karakte
print(men_lis_la)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
karakte=input(" 3) entre yn fraz pwogram nan ap mete tout premye let mo yo an majiskil").title()
print(karakte)
karakte=input("4) entre yn fraz pwogram nan ap rekipere chak premye let yo pou l mete yo ansann")
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
mt=karakte.split()
prm=[kas[0] for kas in mt ]
rezilta=''.join(prm)
print(rezilta)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
karakte=input(" 5) entre yn fraz pwogram nan ap ranplase tout a yo pa @ ").replace("a","@").replace("A","@")
print(karakte)
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
karakte=input(" 6) entre chenn karakte epi pwogwam nn ap mete l devan deye e an majiskil").upper()
print(f"men chenn karakte ou t antren: {karakte}")
invers=karakte[::-1]
print(f"men sa w t rantre a a lenves: {invers}")
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
karakte=input("entre yn chenn de karakte ki komanse pa :a pwogram nan ap detemine index premye elemen")
endeks=[]
for i in range(len(karakte)):
    if karakte[i]=='a':
        endeks.append(i)
print(f"endeks tout karakte a ki nan chenn sa c : {endeks}")
print("🛫🛫🛫🛫🛫🛫🛫🛬🛬🛫🛫🛬🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛬🛬🛬🛬🛫🛬🛬🛫🛫🛬🛬🛫🛬🛫🛫🛫🛫🛫")
karakte=input("entre yn chenn karakte ki gen espas pwogram nan ap retire tout esps yo").replace(" ","")
print(f"men chenn karakte san espas : {karakte}")
print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")
print(" PATI 2) MASTER LIST (Union & Intersection & Lis comprehension)") 
print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")




