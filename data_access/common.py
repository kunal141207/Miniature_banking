from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from app import db


def add_object_details(obj, commit=True):
    try:
        db.session.add(obj)
        if commit is True:
            db.session.commit()
        else:
            db.session.flush()
        return True
    except:
        db.session.rollback()
        return False
