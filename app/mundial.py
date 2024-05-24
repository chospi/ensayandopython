from read_csv import read_csv
from charts import generate_pie



def run(path):
  data = read_csv("./app/data.csv")
  labels = list(map(lambda x: x["Country/Territory"], data))
  values = list(map(lambda x: x["World Population Percentage"], data))
  generate_pie(labels, values)
  



if __name__ == "__main__":
  run("./app/data.csv")