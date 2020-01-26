#!/usr/bin/env python
# coding: utf-8

# In[47]:


# Carga los usuarios que estan en el archivo users.csv
import easygui
import pandas as pd


# In[50]:


##Ventana para seleccionar archivo CSV
easygui.msgbox(msg="Aplicacion de configuracion de telefonos GrandStream", title="Julio Saldivar GS Config", ok_button="Adelante")
FileName = easygui.fileopenbox(title = "Seleccion su archivo", filetypes=["*.csv"])
### Leemos el archivo con pandas
df = pd.read_csv(FileName, skiprows=1)


# In[55]:


###
# Esta funcion crea un archivo XML en base la informacion de dataframe
# como punto importante la primera columna la toma como la direccion mac del dispositivo
###
def func(row):
    xml = ['<?xml version="1.0" ?>']
    xml.append('<gs_provision version="1">')
    i=0
    for field in row.index:
        if i == 0:
            xml.append('<mac>{1}</mac>'.format(field, row[field]))
            mac = "xml/" + str(row[field]) + ".xml"
            xml.append('<config version="1">')
            i = i + 1
        else:
            xml.append('<{0}>{1}</{0}>'.format(field, row[field]))
            i = i + 1
    xml.append('</config>')
    xml.append('</gs_provision>')
    archivo = '\n'.join(xml)
    with open(mac, "w") as f:
        f.write(archivo)
    return print("Archivo para " + str(mac) + " creado exitosamente")


# In[56]:


df.apply(func, axis=1)


# In[ ]:




