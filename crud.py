import schema

def get_user_by_id(user_id: int):
    user = schema.User(id=user_id, name=f'goudot-{user_id}', email='EGo@gmail.com')
    return user