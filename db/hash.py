from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes="bcrypt", deprecated="auto")

class Hash():
    def bcrypt(password : str):
        return pwd_cxt.hash(password[:72])

    def verify(hashed_password : str, plain_password : str):
        return pwd_cxt.verify(plain_password,hashed_password[:72])