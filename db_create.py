# db_create.py

from project import db
from project.models import Task, User
from datetime import date

# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()
