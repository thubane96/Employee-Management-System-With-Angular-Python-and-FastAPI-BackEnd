from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from fastapi import UploadFile, File

class Employee(BaseModel):
    id: Optional[int]
    name: str
    email: str
    job_title: str
    phone: str
    image: str
    employee_code: Optional[str]

