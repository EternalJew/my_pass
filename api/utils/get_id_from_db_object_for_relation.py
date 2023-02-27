def get_id(model_class, name_from_json):
    obj_from_db = model_class.query.filter_by(name=name_from_json).first()
    if obj_from_db is not None:
        id = obj_from_db.id

    return id