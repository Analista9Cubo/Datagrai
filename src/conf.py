import os
from dotenv import load_dotenv
from datetime import timedelta


load_dotenv()

class Config:
     
     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://usuario:contraseña@localhost:5432/nombre_bd')

     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-key-change-me')
     JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
     JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
     JWT_TOKEN_LOCATION = ['headers']
     JWT_HEADER_NAME = 'Authorization'
     JWT_HEADER_TYPE = 'Bearer'
     