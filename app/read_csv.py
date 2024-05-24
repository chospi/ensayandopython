#Importamos modulo NATIVO de python para leer CSV
import csv

#Definimos funcion para leer 
def read_csv(path):
  with open(path, "r") as csvfile: #Abrir y cerrar el archivo, con solo lectura
    reader = csv.reader(csvfile, delimiter=",")
    """
    Aca llamamos el modulo CSV y le decimos que lea el archivo que tenemos que hemos llamado csvfile
    """
    header = next(reader)#Leemos la primera linea del archivo y la guardamos en header
    data = [] #Creamos una lista vacia para llenarla de diccionarios
    for row in reader:#Iteracion para leer fila por fila
      #print("****"*5)ME indique cada row que escriba
      iterable = zip(header, row)#Unzip para unir los dos arrays en tuplas, el header y el row
      #Creamos un diccionario con dict comprehension
      country_dic = {key:value for key, value in iterable}
      data.append(country_dic)#Agregamos el diccionario a la lista
    return data  
      
      
#Quiero que se ejecute como script desde la terminal
if __name__ == "__main__":
  data = read_csv("data.csv")
  print(data)
  #Se ejecutara como array pero para leer mejor debe ser diccionario
  
      
