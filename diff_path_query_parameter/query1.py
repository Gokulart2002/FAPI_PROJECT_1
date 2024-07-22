from fastapi import FastAPI

app=FastAPI()

database={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
          }


@app.get("/sub")
async def subpage(sub_page:str="key1",query:int|None=5):
    return database.get(sub_page)

@app.get("/test")
async def subpage(sub_page:str|None):
    if sub_page:
        return database.get(sub_page)
    else:
         return "The value not provide "