from datetime import date

data_nasc = [int(x) for x in input("Digite a data do seu nascimento: ").split()]
YourDays = 0




AnoAtual = date.today().year
MesAtual = date.today().month
DiaAtual = date.today().day
Idade = (AnoAtual - 1) - data_nasc[2]

Bissexto = 0

if data_nasc[1] in [3,5,7,8,10,12]:
    YourDays = 31 - data_nasc[0]
else:
    YourDays = 30 - data_nasc[0]
   


for x in range(data_nasc[2], AnoAtual):
    if x%4==0:
        Bissexto += 1

for a in range(data_nasc[1] + 1 ,13):
    for b in range(1):
        if a in (3,5,7,8,10,12):
            YourDays += 31
        elif a == 2 and AnoAtual%4==0:
            YourDays += 29
        elif a == 2:
         YourDays += 28
        else:
            YourDays +=30
    
    
    
for i in range(1, MesAtual):
    
    
    if i in (3,5,7,8,10,12):
        YourDays += 31
    elif i == 2 and AnoAtual%4==0:
        YourDays += 29
    elif i == 2:
        YourDays += 28
    else:
        YourDays +=30
for y in range(1,DiaAtual+1):
    YourDays += 1

YourDays = (Idade*365) + YourDays + Bissexto 
print(YourDays)

