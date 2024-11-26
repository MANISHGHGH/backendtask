import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your_secret_key'

def encode_auth_token(user_id):
    expiration = datetime.utcnow() + timedelta(days=1)
    payload = {
        'exp': expiration,
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Token expired.'
    except jwt.InvalidTokenError:
        return 'Invalid token.'
