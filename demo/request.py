from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class student(BaseModel):
    Name:str
    Roll_No:int
    school:str

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post("/student_details")
async def create_student(student1:student):#(Object_name:Class_name)
    return "The Student name is :"+ student1.Name + ", Roll No: " + str(student1.Roll_No)+ " and studied     at :" +student1.school


@app.post("/blog")
async def create_blog(blog1:Blog): #(Object_name:Class_name)
    return {'data':f"Blog is created with title as {blog1.title}"}