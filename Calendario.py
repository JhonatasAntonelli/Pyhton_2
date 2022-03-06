print('-*-'*5, 'Seja bom vindo à calculadora do tempo de vida', '-*-'*5)
ano = int(input('Digite o ano do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento: '))
dia = int(input('Digite o dia do seu nascimento: '))
anoa = int(input('Digite o ano atual: '))
mesa = int(input('Digite o mês atual: '))
diaa = int(input('Digite o dia de hoje: '))
bissexto = (2024 - ano)//4
if mes == 1:
    diab_mes = 0
if mes == 2:
    diab_mes = 31
if mes == 3:
    diab_mes = 59
if mes == 4:
    diab_mes = 90
if mes == 5:
    diab_mes = 120
if mes == 6:
    diab_mes = 151
if mes == 7:
    diab_mes = 181
if mes == 8:
    diab_mes = 212
if mes == 9:
    diab_mes = 243
if mes == 10:
    diab_mes = 273
if mes == 11:
    diab_mes = 304
if mes == 12:
    diab_mes = 334
if mesa < mes and diaa < dia:
    mes_vida = 12 - (mes-mesa)
    mesb_vida = ((anoa - ano - 1) * 12) + (12 - mesa + mes)
    anos_vida = anoa - ano - 1
    diab = diaa
    diab_vida = ((anoa - ano ) * 365) + bissexto - diab_mes + dia
if mesa < mes and diaa > dia:
    mes_vida = 12 - (mes-mesa)
    mesb_vida = ((anoa - ano - 1) * 12) + (12 - mesa + mes)
    anos_vida = anoa - ano - 1
    diab = diaa - dia
    diab_vida = ((anoa - ano ) * 365) + bissexto - diab_mes + diaa - dia
if mesa < mes and diaa == dia:
    mes_vida = 12 - (mes-mesa)
    mesb_vida = ((anoa - ano - 1) * 12) + (12 - mesa + mes)
    anos_vida = anoa - ano - 1
    diab = 0
    diab_vida = ((anoa - ano ) * 365) + bissexto - diab_mes
if mesa > mes and diaa > dia:
    mes_vida = mesa - mes
    mesb_vida = ((anoa - ano) * 12) + (mesa - mes)
    anos_vida = anoa - ano
    diab = diaa - dia
    diab_vida = ((anoa - ano + 1) * 365) + bissexto - diab_mes - 31 + (diaa - dia)
if mesa > mes and diaa < dia:
    mes_vida = mesa - mes
    mesb_vida = ((anoa - ano) * 12) + (mesa - mes)
    anos_vida = anoa - ano
    diab = diaa
    diab_vida = ((anoa - ano + 1) * 365) + bissexto - diab_mes - 31 + diaa
if mesa > mes and diaa == dia:
    mes_vida = mesa - mes
    mesb_vida = ((anoa - ano) * 12) + (mesa - mes)
    anos_vida = anoa - ano
    diab = 0
    diab_vida = ((anoa - ano + 1) * 365) + bissexto - 31 - diab_mes
if mesa == mes and diaa < dia:
    mes_vida = 12 - (mes-mesa)
    mesb_vida = ((anoa - ano - 1) * 12) + (12 - mesa + mes)
    anos_vida = anoa - ano - 1
    diab_vida = ((anoa - ano) * 365) + bissexto - (dia -diaa)
    diab = diaa - dia
if mesa == mes and diaa > dia:
    mes_vida = mesa - mes
    mesb_vida = ((anoa - ano) * 12) + (mesa - mes)
    anos_vida = anoa - ano
    diab_vida = ((anoa - ano) * 365) + bissexto + diaa - dia
    diab = diaa
if mesa == mes and diaa == dia:
    mes_vida = mesa - mes
    mesb_vida = ((anoa - ano) * 12)
    anos_vida = anoa - ano
    diab_vida = ((anoa - ano) * 365) + bissexto
    diab = 0
if mes_vida == 1:
    dia_mes = 0
if mes_vida == 2:
    dia_mes = 31
if mes_vida == 3:
    dia_mes = 59
if mes_vida == 4:
    dia_mes = 90
if mes_vida == 5:
    dia_mes = 120
if mes_vida == 6:
    dia_mes = 151
if mes_vida == 7:
    dia_mes = 181
if mes_vida == 8:
    dia_mes = 212
if mes_vida == 9:
    dia_mes = 243
if mes_vida == 10:
    dia_mes = 273
if mes_vida == 11:
    dia_mes = 304
if mes_vida == 12:
    dia_mes = 334
print ('Você tem {} dias de vida'.format(diab_vida))
print ('Você tem {} meses de vida'.format((anos_vida * 12) + mes_vida))
print ('Você ja passou por {} anos bissexto'.format(bissexto))
print ('Você possui {} anos'.format(anos_vida))
print ('Você tem {} anos, {} meses e {} dias de vida'.format(anos_vida, mes_vida, diab))
print('-*-'*5, 'Fim dos calculos, tenha um bom dia!', '-*-'*5)