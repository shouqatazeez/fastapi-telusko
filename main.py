from fastapi import FastAPI

 

from pydantic import BaseModel

class product(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantity:int




app = FastAPI()


@app.get("/")
def intro():
    return "This is the intrdouction to fastapi in simple" 


products = [
    product(id = 1,name = "Mobile",description = "This is the smart mobile",price = "4.5", quantity =10)
]

@app.get("/products")
def productslist():
    return products
