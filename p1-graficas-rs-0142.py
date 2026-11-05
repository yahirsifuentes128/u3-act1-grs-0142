import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
# crearemos nuestra tabla y la guardamos con pandas 
# tenemos 5 listas de redes sociales con 4 elementos por lista 
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# creamos una lista de listas (conformando la tabla)
lista_redes_sociales=[fb,twt,ig,wsp,tel,lkn]
# print(listaq_redes_sociales)
#utilizar panda para organizar la tabla m(dataframe o marco de datos )
# a cada columna le ponemos nombre
# Código corregido:
df_redes_sociales = pd.DataFrame(lista_redes_sociales, columns=["nombre", "cantidad", "es_fb", "años"])
print(df_redes_sociales)
# creamos el archivo csv y lo guardamos en csv
df_redes_sociales.to_csv("redessociales.csv", index=False)
# crear grafica de lineas 
# donde x es nombre en el eje horizontal 
# donde y es cantidad en el eje vertical
plt.plot(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.title("grafica redes sociales 0142")
plt.xlabel("nombre de las redes ")
plt.ylabel("cantidad de usuarios ")
plt.show()
# creamos una grafica de puntos
plt.scatter(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.show()
# grafica de barras
plt.bar(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
# etiquetas y titulo 
plt.title("redes sociales 0142")
plt.xlabel("nombre de las redes ")
plt.ylabel("cantidad de usuarios ")
# mostrar la grafica 
plt.show()
#ordenar la grafica de barras de manera descendente 
# de la mas grande a lamas pequeño 
df_rs_ordenar=df_redes_sociales.sort_values("cantidad",ascending=False)
plt.bar(df_rs_ordenar["nombre"],df_rs_ordenar["cantidad"])
plt.show()
# coloreando la grafica
plt.bar(df_rs_ordenar["nombre"],df_rs_ordenar["cantidad"],
        color=["b","g","c","m","y","r"])
plt.show()

# grafica de pastel
# plt.plot(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.pie(df_redes_sociales["cantidad"], labels=df_redes_sociales["nombre"])
plt.show()

















