from flask import request, jsonify
from sqlalchemy.orm import sessionmaker
from Database.models import TestUpdateData
from Database.db import engine
from events import broadcast_update

Session = sessionmaker(bind=engine)
session = Session()

def add_data():
    value = request.json.get('value')
    new_data = TestUpdateData(value=value)
    session.add(new_data)
    session.commit()

    broadcast_update({'id': new_data.id, 'value': new_data.value})
    return jsonify({'id': new_data.id, 'value': new_data.value})

def get_data():
    data = session.query(TestUpdateData).all()
    result = [{'id': d.id, 'value': d.value} for d in data]
    return jsonify(result)
