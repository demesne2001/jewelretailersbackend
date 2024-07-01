import os
from fastapi import APIRouter,Body,Depends,HTTPException
from Services.jwtBearer import jwtBearer
from Entity.DTO.WsInput import Login,TokenInvoke
from Services import AuthenticationService
LoginController=APIRouter()

@LoginController.post('/login')
async def login(input:Login): 
       result=AuthenticationService.Authentication(input)
       return result

@LoginController.post('/TokenInvoke',dependencies=[Depends(jwtBearer())])
async def DbChange(input:TokenInvoke): 
       result=AuthenticationService.DbChange(input)
       return result