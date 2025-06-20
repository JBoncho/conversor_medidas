
import pandas as pd

data = {
    "Piezas:" : ["Pata", "Tablero","Puerta","Estante","Panel lateral"],
    "Centímetros:" : [40, 120, 60, 30, 180]
}

df = pd.DataFrame(data)

#Guardar el df en un archivo excel
df.to_excel("Medidas_muebles.xlsx", index = False)
