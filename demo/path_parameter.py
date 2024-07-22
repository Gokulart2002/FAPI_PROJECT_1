from fastapi import FastAPI

app=FastAPI()

# one path we are passing 
@app.get("/{Name}")
async def show(Name):
     msg="Hi My Self "+Name
     return msg

# if you need to pass two path_parameter
@app.get("/{Name}/{Age}")
async def show(Name:str,Age:int):
     msg="Hi My Self "+Name + ", My Age is :"+ str(Age)
     return msg

#if you want to spesify type of data in your function 
@app.get("/{Name}/{Age}/{Number}")
async def show(Name:str,Age:int,Number:int):
     msg="Hi My Self "+Name + ", My Age is :"+ str(Age) + ",My number is :"+str(Number)
     return msg
