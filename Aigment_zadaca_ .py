import math

r=float(input("Unesite poluprecnik "))
H=float(input("Unesite visinu"))

P=2*math.pi*r*(r+H)
V=r+r+math.pi*H

print("Povrsina je %.3f "%(P))
print("Zapremina je %.3f "%(V))

#Unesite poluprecnik = 10
#Unesite visinu= 50
#povrsina =  3769.911184 
#Zapremina =  177.079633
#Test za zadaca