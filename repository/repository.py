#!/usr/bin/python3
from typing import List
from model.employee import Employee
import mysql.connector
import random
import base64

employees: List[Employee] = []

def _db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="emsdb"
    )

    return connection


def _insert_employee(employee: Employee):

    sql = "INSERT INTO employees (name, email, job_title, phone, image, employee_code) VALUES (%s, %s, %s, %s, %s, %s)"
    employee_code = random.randint(0, 1000)
    val = (employee.name, employee.email, employee.job_title, employee.phone, employee.image , employee_code)
    
    try: 
        connection = _db_connection()
        mycursor = connection.cursor()

        result = mycursor.execute(sql, val)
        connection.commit()
        return {"result": "employee inserted successfully"}
        
    except mysql.connector.Error as error:
        print("error with inserting employee in db: ", error)

    finally:
        if connection.is_connected():
            mycursor.close()
            connection.close()
            print("MySQL connection is closed")


def _get_employees():

    try:
        connection = _db_connection()
        mycursor = connection.cursor()

        mycursor.execute("SELECT * FROM employees")

        records = mycursor.fetchall()
        employees.clear()
        for row in records:
            employees.append(Employee(
                id = row[0],
                name = row[1],
                email = row[2],
                job_title = row[3],
                phone = row[4],
                image = row[5],
                employee_code = row[6],
            ))
       
        return employees
    
    except mysql.connector.Error as error:
        print("error with fetching employees in db: ", error)

    finally:
        if connection.is_connected():
            mycursor.close()
            connection.close()
            print("MySQL connection is closed")
    

def _update_employee(employee: Employee):

    try:
        connection = _db_connection()
        mycursor = connection.cursor()

        sql = "UPDATE employees SET name = %s, email = %s, job_title = %s, phone = %s, image = %s WHERE id = %s"
        val = (employee.name, employee.email, employee.job_title, employee.phone, employee.image, employee.id)
        mycursor.execute(sql, val)
        connection.commit()
        return {"result": "employee updated successfully"}

    except mysql.connector.Error as error:
        print("error with updating employee in db: ", error)

    finally:
        if connection.is_connected():
            mycursor.close()
            connection.close()
            print("MySQL connection is closed")
    
            
def _delete_employee(id):

    try:
        connection = _db_connection()
        mycursor = connection.cursor()

        sql = "DELETE FROM employees WHERE id = %s"
        val = (id,)

        mycursor.execute(sql, val)
        connection.commit()
        return {"result": "employee deleted successfully"}

    except mysql.connector.Error as error:
        print("error with deleting employee in db: ", error)

    finally:
        if connection.is_connected():
            mycursor.close()
            connection.close()
            print("MySQL connection is closed")