import jwt
import datetime
SECRET_KEY = 'LDR_PEPS'
class Jwtutils:
    def create_token(self, user_id, admin):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id,
                'rol': admin
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        except Exception as e:
            print(e)
            return e
        return token
