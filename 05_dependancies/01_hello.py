# example 01 old way with helper function

# from fastapi import FastAPI, Query, Depends

# app: FastAPI = FastAPI()

# # login function

# def login(username: str, password:str):

#     if username == 'admin' and password == 'admin':

#         return { 'message': 'Login Successfully!' }
    
#     else:

#         return { 'message': 'Login Failed!' }
    
# api route

# @app.get('/login')
# def login_api(user, password):

#     result = login(user, password)

#     return result

# example 02 new way with dependancies injection

from fastapi import FastAPI, Depends, Query

from typing import Annotated

app: FastAPI = FastAPI()

# dependancy function

def dep_login(username: str = Query(None), password: str = Query(None)):

    if username == 'admin' and password == 'admin':

        return { 'message': 'Login Successfully!' }
    
    else:
        
        return { 'message': 'Login Failed!' }

    
# api route

@app.get('/signin')
def login_api(user: Annotated[dict, Depends(dep_login)]):

    return user
