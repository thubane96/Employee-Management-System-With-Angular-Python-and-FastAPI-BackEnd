#!/usr/bin/python3

from typing import List 
from model.employee import Employee
import repository.repository as repo


def _add_employee(employee: Employee):
    return repo._insert_employee(employee)

def _get_employees():
    return repo._get_employees()

def _update_employee(employee: Employee):
    return repo._update_employee(employee)

def _delete_employee(id):
    return repo._delete_employee(id)