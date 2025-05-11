import os
from dotenv import load_dotenv


load_dotenv()

class Config:
     
     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://usuario:contraseña@localhost:5432/nombre_bd')
     