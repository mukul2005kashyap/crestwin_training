"""
'''what is fast api : -    FastAPI is a modern and high-performance Python web framework used to build APIs quickly and efficiently.
                         Designed with simplicity it allows developers to create RESTful APIs using Python's type hints which also 
                         enable automatic validation and error handling.

feature of fastapi: -
                        1) Automatic Documentation: FastAPI auto-generates interactive API docs using OpenAPI standard
                        2)Data Validation: FastAPI uses Pydantic models to validate and serialize/deserialize request data automatically.
                        3)Asynchronous Support: Supports async and await allowing non-blocking code for better performance in I/O-heavy apps.


installation of fast api : - 

setup venv : python -m venv venv 
             venv/Scripts/Activate 


Python version should be great than >= 3.7

1)  pip install fastapi 

pip  show fastapi 

check :- Version: 0.116.1

install uvicorn 
2) pip install unicorn 

create a main.py file root!
? uvicorn is a Asgi web server that is used to run fast api --
        ASGI means:it can run FastAPI and handle multiple requests fast.
        FastAPI needs a server to run, and that server is usually uvicorn.


? Pydantic -- pydantic is a data validation tool that is used to valdite the data means it checks that the data comes the fast api is in 
    the correct format or not

    asyn await--its like a asyncronous task means while one api request is perform or take a time to get execute so during that task 
    it will perform the other task or it would run other request

"""


from fastapi import FastAPI , Path , HTTPException
from pydantic import BaseModel   #type:ignore
import json

app = FastAPI()

def load():
    with open('data.json','r') as f:
        data=json.load(f)
    return data


@app.get("/")
def add():
    return {"message": "welcome to the crestwin"} 


@app.get("/view")
def show():
    data = load()
    return data

"""
path parameters --
            path parametrs are the parametrs that you pass with or inside the urls paths
            they are used to send dynamic data like name id age pid etc......


    """

@app.get("/employee/{id}")
def display(id:str = Path(..., description="here you enter the employee id ", example="P002")):           #--it is used to enhance the readibility
                                                                                                        # validation metadata and documentation  
                                                                                                        # at your api end point 
    data=load()
    if id in data:
        return data[id]
    
#       return "details not found"
    raise HTTPException(status_code=404, detail="Employee of this id is not found...")
#?    HTTP Exception -- is a special built in exception in fastapi that is used to return the custom http error while something got wrong
        #?  while inested of writting the json or crashing the server , you can gracefully raise the error


"""
?  query parameter are the special optional key value parameter that are append at the end of the url used to pass the additional data
            eith http url that are typicaly used for operations like pagging sorting alteration filltering searchinng etc...

"""

