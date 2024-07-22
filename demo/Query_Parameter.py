from fastapi import FastAPI

app=FastAPI()


@ app.get("/basic")
async def basic_fun(count:int):
    lst=[1,2,3,4,5,6,7,8,9]
    return lst[:count]


@ app.get("/book")
async def book(limit:int):
    # duplikete database
    books=[
        {"1001":"python book"},
        {"1002":"java book"},
        {"1003":"html book"},
        {"1004":"css book"},
        {"1005":"javaScripit book"}
        ]
    return " book data is :{}".format(books[:limit])

@ app.get("/blogs")
async def blogs_cheak(count:int,unpulished:bool):
    if unpulished:
        return str(count)+" blogs are unpulished"
    else:
        return str(count)+" blogs are pulished"

