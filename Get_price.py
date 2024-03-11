import cryptocompare as cc
from envio_correos import envio_notificacion

cantidades = {'ADA':63, 'HBAR':228, 'DOT':2, 'AVAX':0.40, 'RNDR':3.23, 'SOL':0.066, 'BNB':0.092, 'CRO':450, 'KUJI':4,
              'RAY':12, 'FET': 18, 'XAI':18, 'PYTH':30, 'PAAL':66, 'METAL':136, 'SAUCE':131, 'AGIX':51,
              'ALI':749, 'VR':122, 'GRT':79, 'MAN':585, '0x0':92, 'AITECH':50, 'CGPT':30}
criptos = {}

criptos.update(cc.get_price('ADA', currency='USD')) 
criptos.update(cc.get_price('HBAR', currency='USD'))
criptos.update(cc.get_price('DOT', currency='USD'))  
criptos.update(cc.get_price('AVAX', currency='USD'))
criptos.update(cc.get_price('RNDR', currency='USD'))
criptos.update(cc.get_price('SOL', currency='USD'))
criptos.update(cc.get_price('BNB', currency='USD'))
criptos.update(cc.get_price('CRO', currency='USD'))
criptos.update(cc.get_price('KUJI', currency='USD'))
criptos.update(cc.get_price('RAY', currency='USD'))
criptos.update(cc.get_price('FET', currency='USD'))
criptos.update(cc.get_price('XAI', currency='USD'))
criptos.update(cc.get_price('PYTH', currency='USD'))
criptos.update(cc.get_price('PAAL', currency='USD'))
criptos.update(cc.get_price('METAL', currency='USD'))
criptos.update(cc.get_price('SAUCE', currency='USD'))
criptos.update(cc.get_price('AGIX', currency='USD'))
criptos.update(cc.get_price('ALI', currency='USD'))
criptos.update(cc.get_price('VR', currency='USD'))
criptos.update(cc.get_price('GRT', currency='USD'))
criptos.update(cc.get_price('MAN', currency='USD'))
criptos.update(cc.get_price('0x0', currency='USD'))
criptos.update(cc.get_price('AITECH', currency='USD'))
criptos.update(cc.get_price('CGPT', currency='USD'))

# Funcion de analisis
def analisis_precio(valor_actual: int, valor_objetivo: int, moneda: str):
   if valor_actual >= valor_objetivo:

      for valor in cantidades.items():
         if valor[0] == moneda: 
            cantida_venta = valor[1]
      envio_notificacion(moneda,valor_actual,cantida_venta)
   else:
      mensaje = f"Aun hay que esperar"

# Recorrido de los precios
## ADA ###############################################################
for monedas in criptos.items():
   if monedas[0] == 'ADA':
      for valor in monedas[1].items():
         analisis_precio(valor[1],1.05,'ADA') 

## HBAR ###############################################################
   if monedas[0] == 'HBAR':
      for valor in monedas[1].items():
         analisis_precio(valor[1],0.19,'HBAR')

## DOT ###############################################################
   if monedas[0] == 'DOT':
      for valor in monedas[1].items():
         analisis_precio(valor[1],17.82,'DOT')

## AVAX ###############################################################
   if monedas[0] == 'AVAX':
      for valor in monedas[1].items():
         analisis_precio(valor[1],60.4,'AVAX')

## RNDR ###############################################################
   if monedas[0] == 'RNDR':
      for valor in monedas[1].items():
         analisis_precio(valor[1],14.47,'RNDR') 

## SOL ###############################################################
   if monedas[0] == 'SOL':
      for valor in monedas[1].items():
         analisis_precio(valor[1],258,'SOL') 

## BNB ###############################################################
   if monedas[0] == 'BNB':
      for valor in monedas[1].items():
         analisis_precio(valor[1],649,'BNB') 

## CRO ###############################################################
   if monedas[0] == 'CRO':
      for valor in monedas[1].items():
         analisis_precio(valor[1],0.95,'CRO')

## KUJI ###############################################################
   if monedas[0] == 'KUJI':
      for valor in monedas[1].items():
         analisis_precio(valor[1],14,'KUJI')

## RAY ###############################################################
   if monedas[0] == 'RAY':
      for valor in monedas[1].items():
         analisis_precio(valor[1],2.9,'RAY')

## FET ###############################################################
   if monedas[0] == 'FET':
      for valor in monedas[1].items():
         analisis_precio(valor[1],4.86,'FET')

## XAI ###############################################################
   if monedas[0] == 'XAI':
      for valor in monedas[1].items():
         analisis_precio(valor[1],2.5,'XAI')

## PYTH ###############################################################
   if monedas[0] == 'PYTH':
      for valor in monedas[1].items():
         analisis_precio(valor[1],1.4,'PYTH')

## PAAL ###############################################################
   if monedas[0] == 'PAAL':
      for valor in monedas[1].items():
         analisis_precio(valor[1],1.35,'PAAL')

## METAL ###############################################################
   if monedas[0] == 'METAL':
      for valor in monedas[1].items():
         analisis_precio(valor[1],0.28,'METAL')

## SAUCE ###############################################################
   if monedas[0] == 'SAUCE':
      for valor in monedas[1].items():
         analisis_precio(valor[1],0.39,'SAUCE')

## AGIX ###############################################################
   if monedas[0] == 'AGIX':
      for valor in monedas[1].items():
         analisis_precio(valor[1],2.1,'AGIX')

## ALI ###############################################################
   if monedas[0] == 'ALI':
      for valor in monedas[1].items():
         analisis_precio(valor[1],0.06,'ALI')

## VR ###############################################################
   if monedas[0] == 'VR':
      for valor in monedas[1].items():
         analisis_precio(valor[1],0.085,'VR')

## GRT ###############################################################
   if monedas[0] == 'GRT':
      for valor in monedas[1].items():
         analisis_precio(valor[1],0.52,'GRT')

## MAN ###############################################################
   if monedas[0] == 'MAN':
      for valor in monedas[1].items():
         analisis_precio(valor[1],0.1220,'MAN')

## 0x0 ###############################################################
   if monedas[0] == '0x0':
      for valor in monedas[1].items():
         analisis_precio(valor[1],0.5,'0x0')

## AITECH ###############################################################
   if monedas[0] == 'AITECH':
      for valor in monedas[1].items():
         analisis_precio(valor[1],0.3,'AITECH')

## CGPT ###############################################################
   if monedas[0] == 'CGPT':
      for valor in monedas[1].items():
         analisis_precio(valor[1],0.63,'CGPT')