from fastapi import APIRouter, HTTPException,Depends,Query
from schema.die_schema import FormData

router=APIRouter()

@router.post("/die_push")
async def die_push(data:FormData):
    return {"message": "Form submitted!", "data": data}