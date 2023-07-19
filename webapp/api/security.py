```python
from flask import request, g, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .exceptions import UnauthorizedError

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        g.user = user
        return True
    raise UnauthorizedError()

@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'}), 403

def hash_password(password):
    return generate_password_hash(password)

def check_password(password_hash, password):
    return check_password_hash(password_hash, password)
```