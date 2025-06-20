#Los planos están en unidades métricas (cm) y las máquinas de medidas en unidades imperiales (pulgadas)
#Realizar un programa que convierta todas las unidades métricas a imperiales para evitar problemas de cálculo
#Este programa conversor leerá el excel y agregará la columna de pulgadas


import pandas as pd

def cm_to_inch(cm):
    return cm/2.54

#Consultar el excel
df = pd.read_excel("Medidas_muebles.xlsx")

#Añadir la columna de pulgas en el df donde estará el cálculo de pulgadas

df["Pulgadas"] = df["Centímetros:"].apply(cm_to_inch)

df.to_excel("muebles_medidas_convertidas.xlsx", index = False)

print(
    "Conversión completada y guardada en el excel 'muebles_medidas_convertidas.xlsx'"
    )
