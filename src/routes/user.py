from flask import Blueprint, request, jsonify
from werkzeug.exceptions import Conflict, Unauthorized
from ..db_con import db
from ..models.user import User
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)

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
            email = data['email'],
            rol = 'visitante'
        )
        user.set_password(data['password'])
        
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
    

@user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        # Validación básica
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Email y contraseña requeridos'}), 400
        
        # Buscar usuario
        user = User.query.filter_by(email=data['email']).first()
        
        # Verificar credenciales
        if not user or not user.check_password(data['password']):
            raise Unauthorized('Credenciales inválidas')
        
        # Generar tokens
        access_token = create_access_token(identity=str(user.id))
        refresh_token = create_refresh_token(identity=str(user.id))
        
        return jsonify({
            'message': 'Inicio de sesión exitoso',
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': user.email,
            'rol': user.rol
        })
        
    except Unauthorized as e:
        return jsonify({'error': str(e)}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    try:
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user)
        
        return jsonify({
            'access_token': new_token
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 401

@user_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    return jsonify({
        'message': f'Bienvenido {user.email}',
    })