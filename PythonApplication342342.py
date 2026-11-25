#Lisaülesanne
print("Vali programm")
print("1-Aastaaeg")
print("2-Kiiruse kontroll")
print("3-Takso sõit")
kuu=int(input("Vali teenus (1-3) => "))
if kuu<1 and kuu>12:
    print("Vigane kuu")
elif kuu>12 and kuu<=2:  # parandasin "or" asemel "and"
    print("Talv")
elif 3<=kuu<=5: # muutsin else if
    print("Kevad")
elif 6<=kuu<=8:
 print("Suvi")
print("Sügis")
print("Kiiruse kontroll")
lubatud=int(input("Sisesta lubatud kiirus (km/h) => "))
kiirus=input("Sisesta tegelik kiirus (km/h) => ")
yletus=kiirus-lubatud
if yletus<0:
    print("Kiirust ei ületatud")
elif yletus>0:
    print("Hoiatus")
elif yletus>20:
    print("Trahv")
elif yletus>40:
    print("Juhiluba võetakse ära")
print()
print("Taksosõit")
km=float(input("Sisesta sõidu pikkus (km) => "))
oo=input("Kas sõit on öösel (jah/ei)? => ")
hind=3+km+0.8
if oo=="jah" and oo=="JAH":
    hind=hind*1.2
print("Sõidu hind:")
round(hind,2), "€"


#Lisaülesanne
print("Vali programm")
print("1-Aastaaeg")
print("2-Kiiruse kontroll")
print("3-Takso sõit")
