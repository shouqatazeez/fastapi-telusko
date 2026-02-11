from fastapi import FastAPI
from models import product

app = FastAPI()


@app.get("/")
def intro():
    return "This is the introduction to fastapi in simple" 


products = [
    product(id = 1,name = "Mobile",description = "This is the smart mobile",price = "45", quantity =10),
    product(id=2,name = "Laptop", description="This is how we use for personal purpose", price = "20",quantity=20),
    product(id=3,name="TV", description= "This is how we watch for the purpose of Entertainment", price="30", quantity= 25)
]

@app.get("/products")
def productslist():
    return products

@app.get("/products/{id}")
def productid(id:int):
    for product in products:
        if(product.id== id):
            return product
        
    return "elements not found"
   

@app.post("/products")
def addproduct(item:product):
    products.append(item)
    return "product added in list "

    