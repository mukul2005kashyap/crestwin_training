# Background task

"""
background task in fast api is a built way to handle the background task by uslng the background task modeule in python 

it is a wahy to handle the task and useful when ypu want to perform the task or work after returning the resposne like sending emails 
or logging or prosessing the file s

"""

from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@app.post("/send-notification/")
async def send_notification(background_tasks: BackgroundTasks, email: str):
    # Add a background task
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": "Notification will be sent in the background"}



# there is also a another way to perform the background tsk like 
"""
you can create the specific tsk by using the async def function and perform that task by background task 

"""

import asyncio
async def async_task(email: str):
    await asyncio.sleep(5)  # simulate long running task
    print(f"Email sent to {email}")

@app.post("/send-email/")
async def send_email(background_tasks: BackgroundTasks, email: str):
    background_tasks.add_task(async_task, email)
    return {"message": "Email sending started in background"}

"""so in simple words 
     in the fastapi when you calling the normal endpoint theen the server gives you the immidiate resposnse but 
     when the tsk is very heavy then it conusme the time pt process it 
     so in that case the backgrounf task helps to get the immideate response from  the server and the user not have to wait for while 
     
     """


# postgress sql::

"""
"PostgreSQL is an open-source, object-relational database management system (ORDBMS) that uses and extends SQL to
store, manage, and retrieve structured data. It is known for its reliability, scalability, and advanced features such as:

     Support for complex queries
        Transactions
        JSONB storage
        Custom data types
        High concurrency through Multi-Version Concurrency Control (MVCC).

Nowadays, many big tech companies including Apple, Instagram, Netflix and Uber have also adopted PostgreSQL
for their certain workloads.

While MySQL is simpler and efficient for read-heavy, lightweight web applications, PostgreSQL excels in 
enterprise-grade environments where scalability, complex data modeling, and reliability are critical.
 Its support for multiple index types, advanced query planner, and extensibility through custom functions
and extensions (like PostGIS for geospatial data) make it far more versatile.

so in sql provides you a way to manage the database through various platforms by creating the database 

sql commands catagories ::
    DDL : data defination language 
        for creating or modifing the structure 
        create 
        rename 
        alter 
        truncate 
    DML (Data Manipulation Language)
        for manupulating the data
        update 
        delete 
        insert 

    DQL (Data Query Language)
        for reading or retriving the data 
            select 
            select * from table_name 

    
Queries::
    SELECT * FROM employees;

    SELECT name, salary FROM employees;

    DELETE FROM employees WHERE id = 1;

    SELECT AVG(salary) FROM employees;
"""

# Indexing 
"""
so basically indeixng is data structure that makes the database queriers more faster 

    indexing would be perform on the particullar column of the table in the database ..
    the indexing creates the lookup table and the pointer to memory location for the row containing that column 

    in simple words indexing creates the anohter column for that particular column in sorted manner for which you performing 
    the insexing and allocate the seperate memory location where each element in that column are associate with tha row 
    containing that column 

    for example we have data in which we have to find the name of the employee whose salary is 4000 so wihtout 
    indexing it iteretvily trsverse the whole databases one by one and find that name --- for that the time time complexity is O(n)

                    SELECT * FROM employee
                    WHERE salary = 4000;

    inested of that if we usr the indexing on that column so it will create the sorted column for that field and find 
    that matching record easily and now the ------ time complexity is the O(log n)

                create index idx_slry
                on employee(salary)
        
    """