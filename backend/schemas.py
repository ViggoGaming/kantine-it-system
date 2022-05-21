from pydantic import BaseModel

# Base class used for both GET,POST,PUT etc


class BaseFood(BaseModel):
    name: str
    description: str
    image: str
    price: float

    class Config:
        orm_mode = True

# When we return a food, we should return the BaseFood class plus this class containing the id aswell


class Food(BaseFood):
    id: int

# Only used for easier naming


class CreateFood(BaseFood):
    pass
#    name: str
#    description: str
#    price: float