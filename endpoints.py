from flask import request, jsonify
from Database.models import TestUpdateData
from Database.db import Session

def create_data():
    session = Session()
    try:
        data = request.get_json()
        new_entry = TestUpdateData(value=data['value'])
        session.add(new_entry)
        session.commit()
        return jsonify(new_entry.to_dict()), 201
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
            return jsonify(data.to_dict())
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
            return {"message": "Delete successful"}, 200
        else:
            return {"message": "Not Found"}, 404
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400
    finally:
        session.close()
