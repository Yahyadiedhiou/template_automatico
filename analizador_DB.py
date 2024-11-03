#VAMOS A CREAR UN SCRIPT QUE ANALICE LA BASE DE DATOS Y DIGA SI HAY UN ERROR

import pandas as pd
import numpy
import os

clientes={  
           "clientes_id": ["001","002","003","004","005","006","007"],
           "Nombres": ["Jose Juan","Persival Van Voorst","Lalo Linda",
                       "Yonimu Bareo","Oksimoron","Sandro Li","Boubacar Sagna"],
            "Email": ["jose@gmail.com","persival@gmil.com","lalo@hotmail.com",
                      "yonimu@hotmail.com","oksimoron@hotmail.com","sandro@gmail.com",
                      "bouba@gmail.com"]
}

#1. Lo convertimas a Dataframe
df=pd.DataFrame(clientes)

#2.lo convertimos a csv
archivo_a_convertir="/Users/yayadiedhiousagna/Desktop/clientes.csv"
df.to_csv(archivo_a_convertir,index=False,encoding="utf-8")

#3.lo imprimes para saber como se ve el dataframe de pandas
print(df)


#Error: La base de datos usa una codificación diferente a la del sistema de 
# entrada de datos (por ejemplo, la base de datos está en UTF-8, pero los datos se 
# insertan en ISO-8859-1).


#funcion para crear el analizador de DB
def analizar_DB(df):

    #aqui definimos los caracteres especiales que queremos buscar
special_chr = {"ñ","ç","�","Ã©"}

    #y los quiero instanciar en esta variable
errores=[]
 

#recorremos las columnas y filas hasta encontrar los errores
#primero recorres la columna y dentro de la columna, los valores dentro de la misma

#enumerate(df[col]): enumerate() es una función de Python que devuelve 
# una secuencia de pares (índice, elemento). En este caso, está aplicada a df[col],
#  que es la Serie correspondiente a la columna col del DataFrame df. df[col] devuelve una 
# columna como una lista de valores, y enumerate permite obtener el índice de cada elemento junto 
# con el valor de ese elemento.
for col in df.columns:
 for i , valor in enumerate(df[col]):
  if any (char in str(valor) for char in special_chr):
    errores.append(valor)

## Verificar codificación (en este caso, asumimos UTF-8 por el archivo CSV)

try:
    with open (archivo_a_convertir,"r",encoding="utf-8") as file:
        file.read()
        print("Esta usando ua codificacion utf-8")

except: UnicodeEncodeError
print("El encoding no es utf-8")


#el archivo de errores , lo tengo que crear como txt. Ahi es donde quiero escribir lo que guarde en errores

archivo_de_errores="/Users/yayadiedhiousagna/Desktop/errores.txt"

with open(archivo_de_errores,"w",encoding="utf-8") as file:
        if errores:
         file.write("\n".join(errores))
         print("Errores guardados en el txt")

        else:
            file.write("No se han encontrado errores")
            print("No se han encontrado errores")


  
