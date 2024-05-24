from utils import population_by_country
from read_csv import read_csv
from charts import generate_bar_chart





def run():
  data = read_csv("data.csv")
  country = input("¿Que pais quiere ver la población?")
  labels, values = population_by_country(data, country)
  population_by_country(data, country)
  generate_bar_chart(labels, values)
  

  

if __name__ == "__main__":
  run()
  




































"""

items = [
  {"country" : "Col",
   "population":100   
  },
  {"country" : "Bol",
    "population":1030    
  },
  {"country" : "Arg",
    "population":140

  }
]


def run():
  keys, values = utils.get_population()
  print(keys, values)
  
  print(utils.a)#LLamando modulo propiamente diseñado
  
  items = [
    {"country" : "Col",
     "population":100   
    },
    {"country" : "Bol",
      "population":1030    
    },
    {"country" : "Arg",
      "population":140
  
    }
  ]
  
  x = utils.population_by_country(items, "Col")
  print(x)

if __name__ == "__main__":
  run()
  """