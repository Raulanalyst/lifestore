# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:55:50 2022

@author: Familia
"""
"""
This is the LifeStore_SalesList data:
lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

import lifestore_file as files #Importamos los datos 
import sys
import matplotlib.pyplot as plt

"Se asignan los datos a variables"
searches=files.lifestore_searches
sales=files.lifestore_sales
products=files.lifestore_products
"Creación de las variables para el log in"
usuario='Administrador'
intentos=4
entrada=input('Usuario:')
"Ciclo para verificar usuario correcto"
while usuario!=entrada:
    intentos-=1
    print(f"Error, le quedan {intentos} intentos")
    if intentos==0:
        sys.exit("Usuario incorrecto, ya no hay intentos")
    entrada=input('Usuario:')
"Conteo total de las ventas, de reembolso, de puntuaciones, de ventas mensuales y el total anual"
total_producto=[[i+1,0,0,0,0] for i in range(96)] #[id_product,ventas,reembolso,score,busqueda]
meses_v=[0]*12
total_anual=0
"Cíclo que recorre todas las ventas"
for ventas in sales:
    if ventas[4]==1:
        total_producto[ventas[1]-1][2]+=1
        total_producto[ventas[1]-1][3]+=ventas[2]
        continue
    total_producto[ventas[1]-1][1]+=1
    total_producto[ventas[1]-1][3]+=ventas[2]
    meses_v[int(ventas[3][3:5])]+=products[ventas[1]-1][2]
    total_anual+=products[ventas[1]-1][2]
"Suma de las busquedas de los productos"
for busq in searches:
    total_producto[busq[1]-1][4]+=1
"Presentación de resultados"
print(f"El total de venta anual es de ${total_anual}")
print("El promedio de ventas mensuales es de:",sum(meses_v)/len(meses_v))
meses=['01','02','03','04','05','06','07','08','09','10','11','12']
plt.bar(meses,meses_v)
plt.xlabel('Meses en formato MM')
plt.ylabel('Cantidad de productos vendidos')
plt.title('Cantidad de productos vendidos mensualmente')
"Ciclo para preguntar que datos imprimir"
var_con='Y'
while var_con=='Y':
    desple=input(f"Para ver los 50 productos con más busquedas inserte '1', para los 50 productos con menos busquedas inserte '2', para los 50 productos con más ventas inserte '3', para los 50 productos con menos ventas inserte '4', para los 20 productos con mejores reseñas inserte '5', para los 20 productos con peores reseñas inserte '6', para los productos con reembolso inserte '7': ")
    "50 productos con más busquedas"
    if desple=='1':
        total_producto.sort(key=lambda cheq:cheq[4],reverse=True)
        print('Primeros 50 productos con mayores busquedas\n')
        for i in range(50):
            print(products[total_producto[i][0]-1][1][:18],'Total de busqueda:',total_producto[i][4],'Categoría: ',products[total_producto[i][0]-1][3])
    elif desple=='2':
        total_producto.sort(key=lambda cheq:cheq[4])
        print('Primeros 50 productos con menores busquedas\n')
        for i in range(50):
            print(products[total_producto[i][0]-1][1][:18],'Total de busqueda:',total_producto[i][4],'Categoría: ',products[total_producto[i][0]-1][3])
    elif desple=='3':
        total_producto.sort(key=lambda cheq:cheq[1],reverse=True)
        print('Primeros 50 productos con mayores ventas\n')
        for i in range(50):
            print(products[total_producto[i][0]-1][1][:18],'Total de piezas vendidas:',total_producto[i][1],'Categoría: ',products[total_producto[i][0]-1][3])
    elif desple=='4':
        total_producto.sort(key=lambda cheq:cheq[1])
        print('Primeros 50 productos con menores ventas\n')
        for i in range(50):
            print(products[total_producto[i][0]-1][1][:18],'Total de piezas vendidas:',total_producto[i][1],'Categoría: ',products[total_producto[i][0]-1][3])
    elif desple=='5':
        total_producto.sort(key=lambda cheq:cheq[3],reverse=True)
        print('Primeros 20 productos con mejores reseñas\n')
        for i in range(20):
            print(products[total_producto[i][0]-1][1][:18],'Total de reseñas:',total_producto[i][3])
    elif desple=='6':
        total_producto.sort(key=lambda cheq:cheq[3])
        print('Primeros 20 productos con peores reseñas\n')
        for i in range(20):
            print(products[total_producto[i][0]-1][1][:18],'Total de reseñas:',total_producto[i][3])
    elif desple=='7':
        total_producto.sort(key=lambda cheq:cheq[2],reverse=True)
        print('Productos con más reembolsos\n')
        for i in range(7):
            print(products[total_producto[i][0]-1][1][:18],'Total de reembolsos:',total_producto[i][2])
    else:
        print('Error en entrada, elija una opción de la lista')
    var_con=input('¿Desea ver otra lista? si=Y, no=N: ')