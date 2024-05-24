import matplotlib.pyplot as plt

#Se descarga la libreria y se pone alias de plt

#creamos funcion para generar grafica
def generate_bar_chart(labels, values):
  fig, ax = plt.subplots() #son dos valores que nos da la librería, fig es como la figura y ax se refire a las coordenadas donde  vamos a empezar a graficar
  ax.bar(labels,values)
  plt.savefig("bar.png")
  plt.close() 


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis("equal")#Necesario para que el grafico sea circular y centrada
  plt.savefig("pie.png")
  plt.close()



if __name__ == "__main__":
  labels = ["a","b","c"]
  values = [100,300,200]
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
