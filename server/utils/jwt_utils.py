import jwt
import datetime
SECRET_KEY = 'LDR_PEPS'
class Jwtutils:
    @staticmethod
    def create_token( user_id:str, admin:bool) -> str:
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30 ),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id,
                'admin': admin
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        except Exception as e:
            print(e)
            return e
        return token


    @staticmethod
    def decode_token(token):

        payload = None
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            pass
        except jwt.InvalidTokenError:
            pass


        return payload


    @staticmethod
    def is_valido( token:str) -> bool:    
        return Jwtutils.decode_token(token) is not None

    @staticmethod
    def is_admin( token:str) -> bool:
        payload = Jwtutils.decode_token(token)
        return payload['admin'] == True