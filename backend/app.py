from enum import unique
from fastapi.param_functions import Depends
from typing import List
import sqlalchemy
import boto3
import uuid
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

import schemas as _schemas
import services as _services

# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

app = FastAPI()

s3_client = boto3.client('s3', region_name='eu-north-1', aws_access_key_id="AKIA3A3742JYNSFBUUYE",
                         aws_secret_access_key="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")
S3_BUCKET = "kantine-it-system"

origins = [
    "http://localhost.com",
    "http://localhost",
    "http://localhost.com:8000",
    "http://localhost:8000",
    "http://localhost:8000/api/foods",
    "http://localhost:3000",
    "http://192.168.1.69:3000",
    "http://192.168.1.69:8000",
    "http://0.0.0.0:8000",
    "http://0.0.0.0:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
@app.post("/api/foods/", response_model=_schemas.Food)
async def create_food(food: _schemas.CreateFood, db: Session = Depends(_services.get_db)):
    return await _services.create_food(food=food, db=db)
"""


@app.post("/api/foods/", response_model=_schemas.Food)
async def create_food(file: UploadFile, name: str = Form(...), description: str = Form(...), price: float = Form(...), db: Session = Depends(_services.get_db)):

    # Upload image to S3 Bucket
    uniqueidentifier = str(uuid.uuid4()) + file.filename
    s3_client.upload_fileobj(file.file, S3_BUCKET, uniqueidentifier, ExtraArgs={
                             "ACL": "public-read"})

    uploaded_file_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{uniqueidentifier}"
    return await _services.create_food(name=name, description=description, price=price, file=uploaded_file_url, db=db)


@app.post("/api/upload")
async def upload(file: UploadFile):

    # Upload image to S3 Bucket
    uniqueidentifier = str(uuid.uuid4()) + file.filename
    s3_client.upload_fileobj(file.file, S3_BUCKET, uniqueidentifier, ExtraArgs={
                             "ACL": "public-read"})

    uploaded_file_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{uniqueidentifier}"

    return {"url": uploaded_file_url}


@app.get("/api/foods/", response_model=List[_schemas.Food])
async def get_all_foods(db: Session = Depends(_services.get_db)):
    return await _services.get_all_foods(db=db)


@app.get("/api/foods/{food_id}/", response_model=_schemas.Food)
async def get_food(
    food_id: int, db: Session = Depends(_services.get_db)
):
    food = await _services.get_food(db=db, food_id=food_id)

    if food is None:
        raise HTTPException(
            status_code=404,
            detail=f"Food with id {food_id}, does not exist")

    return food


@app.delete("/api/foods/{food_id}/")
async def delete_food(
    food_id: int, db: Session = Depends(_services.get_db)
):
    food = await _services.get_food(db=db, food_id=food_id)
    if food is None:
        raise HTTPException(
            status_code=404, detail=f"Food with id {food_id} does not exist")

    await _services.delete_food(food, db=db)

    return f"Deleted food, that had id {food_id}"
