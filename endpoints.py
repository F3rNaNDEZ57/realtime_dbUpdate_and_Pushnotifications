from flask import request, jsonify
from Database.models import TestUpdateData
from Database.db import Session
import requests

SOCKETIO_URL = 'http://localhost:5001'

def create_data():
    session = Session()
    try:
        data = request.get_json()
        new_entry = TestUpdateData(value=data['value'])
        session.add(new_entry)
        session.commit()
        response = new_entry.to_dict()
        requests.post(f'{SOCKETIO_URL}/emit_update', json=response)
        return jsonify(response), 201
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400
    finally:
        session.close()

def get_all_data():
    session = Session()
    try:
        data = session.query(TestUpdateData).all()
        return jsonify([d.to_dict() for d in data])
    except Exception as e:
        return {"error": str(e)}, 400
    finally:
        session.close()

def get_data(id):
    session = Session()
    try:
        data = session.query(TestUpdateData).get(id)
        if data:
            return jsonify(data.to_dict())
        else:
            return {"message": "Not Found"}, 404
    except Exception as e:
        return {"error": str(e)}, 400
    finally:
        session.close()

def update_data(id):
    session = Session()
    try:
        data = session.query(TestUpdateData).get(id)
        if data:
            new_data = request.get_json()
            data.value = new_data['value']
            session.commit()
            response = data.to_dict()
            requests.post(f'{SOCKETIO_URL}/emit_update', json=response)
            return jsonify(response)
        else:
            return {"message": "Not Found"}, 404
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400
    finally:
        session.close()

def delete_data(id):
    session = Session()
    try:
        data = session.query(TestUpdateData).get(id)
        if data:
            session.delete(data)
            session.commit()
            requests.post(f'{SOCKETIO_URL}/emit_update', json={'id': id, 'deleted': True})
            return {"message": "Delete successful"}, 200
        else:
            return {"message": "Not Found"}, 404
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400
    finally:
        session.close()
