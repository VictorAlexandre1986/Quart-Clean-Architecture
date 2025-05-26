from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.core.config import SECRET_KEY, ALGORITHM
from quart import request, g, jsonify
from functools import wraps

def create_access_token(data: dict, expires_delta=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None

def jwt_required(f):
    @wraps(f)
    async def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            return jsonify({"msg": "Token ausente ou inválido"}), 401
        payload = verify_token(token.split(" ")[1])
        if not payload:
            return jsonify({"msg": "Token inválido"}), 401
        g.user_email = payload.get("sub")
        return await f(*args, **kwargs)
    return decorated_function
