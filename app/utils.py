

""""
def get_population():
  keys = ["col", "bol"]
  values = [300,400]
  return keys, values  

a = "Hola"
"""



def population_by_country(data, country):
  result = list(filter(lambda i: i["Country/Territory"] == country, data))
  population_country = {k:v for k,v in result[0].items() if k.endswith("Population")}
  labels = population_country.keys()
  #Para traer los valores de la clave en #entero y no salga en string
  values = [int(values) for values in population_country.values()]
  return labels, values




def populationww(data):
  result = list(filter(lambda i: i, data))
  population_world = {k:v for k,v in result[0].items() if k.endswith("Percentage")}
  values = [int(values) for values in population_world.values()]
 # labels1 = {k:v for k,v in data[0].items() if k.endswith("Territory")}
  #Para traer los valores de la clave en #entero y no salga en string
    #values = [int(value) for value in population_country.values()]
  #labels = labesl1.keys()
  return values




def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values
