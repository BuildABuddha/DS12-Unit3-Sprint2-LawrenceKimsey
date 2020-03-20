import pandas as pd
import sqlite3
import os
import numpy as np


if __name__ == '__main__':
    # Open sqlite3 file
    FILEPATH = os.path.dirname(__file__)
    DB_FILEPATH = os.path.join(FILEPATH, "northwind_small.sqlite3")
    connection = sqlite3.connect(DB_FILEPATH)
    cursor = connection.cursor()

    print("Question: What are the ten most expensive items (per unit price) in the database?")
    query = """
    SELECT ProductName, UnitPrice FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print("ANSWER:")
    for n in result:
        print(n[0], "-", n[1])

    print("\nQuestion: What is the average age of an employee at the time of their hiring?")
    query = """
    Select AVG(HireAge) FROM (
	SELECT HireDate-Birthdate as "HireAge" FROM Employee 
	)
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print("ANSWER:", result[0][0])

    print("\nQuestion: How does the average age of employee at hire vary by city?")
    query = """
    Select City, AVG(HireAge) FROM (
	SELECT City, HireDate-Birthdate as "HireAge" 
	FROM Employee 
	)
    GROUP BY City
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print("ANSWER:")
    for n in result:
        print(n[0], "-", n[1])

    print("\n--------\n\nPART 3:")

    print("\nQuestion: What are the ten most expensive items (per unit price)",
    "in the database and their suppliers?")

    query = """
    SELECT ProductName, UnitPrice, CompanyName FROM Product 
    LEFT JOIN Supplier ON Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice 
    DESC LIMIT 10
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print("ANSWER:")
    for n in result:
        print(n[0], "-", n[1], "-", n[2])

    print("\nQuestion: What is the largest category (by number of unique products in it)?")
    query = """
    SELECT CategoryName, COUNT(CategoryId) as CategoryCount FROM Product
    LEFT JOIN Category ON Product.CategoryId = Category.Id
    GROUP BY CategoryId
    ORDER BY CategoryCount DESC
    LIMIT 1
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print("ANSWER:")
    for n in result:
        print(n[0], "-", n[1])

    print("\nQuestion: Who's the employee with the most territories?")
    query = """
    SELECT FirstName, LastName, COUNT(EmployeeId) as TerritoryCount
    FROM EmployeeTerritory
    LEFT JOIN Employee ON EmployeeTerritory.EmployeeId = Employee.Id
    GROUP BY EmployeeId
    ORDER BY TerritoryCount DESC
    LIMIT 1
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print("ANSWER:")
    for n in result:
        print(n[0], n[1], "-", n[2])
