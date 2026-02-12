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
# This is all about the list of products that we want to show on the page
@app.get("/products")
def productslist():
    return products

# This is how we search products with the id 
@app.get("/products/{id}")
def productid(id:int):
    for product in products:
        if(product.id== id):
            return product
        
    return "elements not found"
   
# This is how we add the product in to the list of products
@app.post("/products")
def addproduct(item:product):
    products.append(item)
    return "product added in list "


# This is how we edit the product we want to edit
@app.put("/products")
def editproducts(id:int, editproduct:product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = editproduct
        return "product added successfully"

    return "not added product"
    
