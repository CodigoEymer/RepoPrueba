import re
import pandas as pd

codigo = """ """

with open("_Conversor.qvs", "r", encoding="utf-8") as file:
    codigo = file.read()

# Extraer texto entre "FROM [" y "]"
#Archivo = re.findall(r'FROM\[(.*?)\]', codigo)
#Archivo = re.findall(r'FROM\s*\[(.*?)\]', codigo)                              #Indiferente a los espacios
Archivo = re.findall(r'FROM\s*\[(.*?)\]', codigo, re.IGNORECASE)                # Indiferente a las mayusculas

# Extraer texto entre "table is" y ");"
#Hoja = re.findall(r'table is (.*?);', codigo)
#Hoja = re.findall(r'table\s*is\s*(.*?))', codigo)
Hoja = re.findall(r'table\s*is\s*(.*?)\)', codigo)

Archivo = [a.split('/')[-1] for a in Archivo]

#matches = re.findall(r'Sh_([^.qvd]*)', codigo)
#matches = re.findall(r'(Sh_[^.qvd]*)', codigo)
NameShare = re.findall(r'(Sh_.*?).qvd', codigo)

#for i in range(len(Archivo)):
    #print("Archivo:"+Archivo[i]+"   Hoja: "+ Hoja[i])
    
# Asegurarse de que las listas tengan la misma longitud
if len(Archivo) > len(Hoja):
    Hoja += [None] * (len(Archivo) - len(Hoja))
elif len(Hoja) > len(Archivo):
    Archivo += [None] * (len(Hoja) - len(Archivo))

# Crear un DataFrame de pandas con las dos listas
df = pd.DataFrame({
    'Archivo': Archivo,
    'Hoja': Hoja,
    'NameShare': NameShare
})

# Guardar el DataFrame en un archivo Excel
df.to_excel('output.xlsx', index=False)