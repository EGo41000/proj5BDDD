import schema

def get_user_by_id(user_id: int):
    '''
    get_user_by_id : récupère un User à partir de son id
    :param user_id: l'ID du user
    :return: User
    '''
    user = schema.User(id=user_id, name=f'goudot-{user_id}', email='EGo@gmail.com')
    return user