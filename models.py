from peewee import Model, SqliteDatabase, CharField, DateField, ForeignKeyField, BooleanField

db = SqliteDatabase('bot.sqlite3')


class User(Model):
    chat_id = CharField()

    class Meta:
        database = db

