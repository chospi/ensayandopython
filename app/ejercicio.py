import csv
import matplotlib.pyplot as plt




def population_country(data, country):
  result = list(filter(lambda i: i["Country/Territory"]==country,     data))[0]
  population_dic = {k:v for k,v in result.items() if k.endswith("Population")}
  labels = population_dic.keys()
  values = population_dic.values()
  return labels, values

def generate(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  return plt.show()


data = []
def read(path):
  country = input("¿Qué pais quiere ver la población?")
  with open(path,"r") as csvfile:
    reader = csv.DictReader(csvfile)<
    for row in reader:
        data.append(row)
    
    labels, values = population_country(data, country)
    generate(labels,values)


if __name__ == "__main__":
  read("./app/data.csv")




