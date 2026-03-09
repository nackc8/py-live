from pathlib import Path

from peewee import *

PROJECT_DIRECTORY = Path(__file__).parent()

# An in-memory SQLite database. Or use PostgresqlDatabase or MySQLDatabase.
db = SqliteDatabase(":memory:")


class BaseModel(Model):
    """All models inherit this to share the database connection."""

    class Meta:
        database = db


class User(BaseModel):
    username = TextField(unique=True)


class Tweet(BaseModel):
    user = ForeignKeyField(User, backref="tweets")
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now, index=True)
