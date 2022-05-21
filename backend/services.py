from sqlalchemy import desc
import database as _database
from sqlalchemy.orm import Session
from typing import List

import schemas as _schemas
import models as _models
import database as _database


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
async def create_food(food: _schemas.CreateFood, db: "Session") -> _schemas.Food:
    food = _models.Food(**food.dict())
    db.add(food)
    db.commit()
    db.refresh(food)
    return _schemas.Food.from_orm(food)
"""

async def create_food(name, description, price, file, db: "Session") -> _schemas.Food:
    data = {
        "name": name,
        "description": description,
        "image": file,
        "price": price
    }
    food = _models.Food(**data)

    db.add(food)
    db.commit()
    db.refresh(food)
    return _schemas.Food.from_orm(food)

async def get_all_foods(db: "Session") -> List[_schemas.Food]:
    foods = db.query(_models.Food).all()
    return list(map(_schemas.Food.from_orm, foods))


async def get_food(food_id: int, db: "Session"):
    food = db.query(_models.Food).filter(_models.Food.id == food_id).first()
    return food


async def delete_food(food: _models.Food, db: "Session"):
    db.delete(food)
    db.commit()
