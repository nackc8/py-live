from pathlib import Path

from peewee import Model, SqliteDatabase, TextField

PROJECT_DIRECTORY = Path(__file__).parent
DATABASE_FILE = PROJECT_DIRECTORY / "db.sqlite"

print(DATABASE_FILE)
db = SqliteDatabase(DATABASE_FILE)


class BaseModel(Model):
    """All models inherit this to share the database connection."""

    class Meta:
        database = db


class Url(BaseModel):
    short = TextField(unique=True)
    original = TextField()


db.connect()
db.create_tables([Url])
