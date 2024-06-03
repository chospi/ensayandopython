import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3]


@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head><h1> ciro es un mamavergas
            </h1>

        </head>
        <body>Cacorro de mal gusto
        </body>
    
    
    
    </html>
    """



   

    


def run():
    store.get_categories()


if __name__ == "__main__":
    run()    