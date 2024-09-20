import crud, schema, pytest
from pydantic import ValidationError

def test_crud1():
    '''
    Test de fonction crud
    :return:
    '''
    u0=schema.UserCreate(name='User creation', email='essai@free.fr')
    uc = crud.create_user(u0)
    assert uc.id > 0

    u1 = crud.get_user_by_id(uc.id)
    assert u1.id == uc.id
    assert u1.name == 'User creation'

def test_crud2():
    '''
    Test 2
    :return:
    '''

    m = schema.Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '5'])
    print(repr(m))
    assert m.dimensions[1] == 5

    external_data = {
        'id': 123,
        'signup_ts': '2019-06-01 12:22',
        'name': 'TBD',
        'email': 'test-ssésss.ttt@gmail.com',
        'tastes': {
            'wine': 9,
            b'cheese': 7,
            'cabbage': '1',
        },
    }

    user = schema.UserCreated(**external_data)
    print('user', user)
    print(user.model_dump())
    assert user.id == 123

    external_data2 = {
        'id': 123,
        'signup_ts': '2019-06-01 12:22',
        'email': 'test-ssésss...ttt@gmail.com',
    }

    with pytest.raises(ValidationError) as excinfo :
        user2 = schema.UserCreated(**external_data2)
