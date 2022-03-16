#!/usr/bin/python3

from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from model.employee import Employee
import service.employee_service as service
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/add")
async def add_employee(employee: Employee):
    return service._add_employee(employee)

@app.put("/update")
def update_employee(employee: Employee):
    return service._update_employee(employee)

@app.get("/all")
def get_employees():
    return service._get_employees()

@app.delete("/delete/{id}")
def delete_employee(id: int):
    return service._delete_employee(id)

