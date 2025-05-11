from flask import Blueprint, request, jsonify
from werkzeug.exceptions import Conflict
from ..db_con import db
from ..models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/createUser', methods=['POST'])
def register():
    try:
        # Validar datos de entrada
        data = request.get_json()

        
        # Verificar si el usuario ya existe
        if User.query.filter_by(email=data['email']).first():
            raise Conflict('Email ya registrado')
        
        # Crear nuevo usuario
        
        user = User(
            email = data['email']
        )
        user.set_password(data['password'])

        print(user.password_hash)
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({
            'message': 'Usuario creado exitosamente',
        }), 201
        
    except Conflict as err:
        return jsonify({'error': str(err)}), 409
    except Exception as err:
        db.session.rollback()
        return jsonify({'error': str(err)}), 500
    
