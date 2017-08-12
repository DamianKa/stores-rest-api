from werkzeug.security import safe_str_cmp
from models.user import UserModel

# users = [
#     User(1, 'bob', 'asdf')
# ]
#
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    # could be also username_mapping['username'] but .get give us option to include also the default value - None
    if user and  safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
