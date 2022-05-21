import sqlalchemy
import database as _database


class Food(_database.Base):
    __tablename__ = "food"
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String, index=True)
    description = sqlalchemy.Column(sqlalchemy.String, index=True)
    image = sqlalchemy.Column(sqlalchemy.String, index=True)
    price = sqlalchemy.Column(sqlalchemy.Float, index=True)
