from fastapi import FastAPI

app=FastAPI()

database={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
          }


@app.get("/sub/{sub_page}/{query}")
async def subpage(sub_page:str,query:int):
    return database.get(sub_page)
