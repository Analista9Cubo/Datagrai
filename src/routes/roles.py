from flask import Blueprint, request, jsonify
from ..db_con import db
from src.models.user import User



rol_bp = Blueprint('rol', __name__)

@rol_bp.route('/updaterol', methods=['PUT'])
def asign():
    try:
        # Validar datos de entrada
        data = request.get_json()

        user =User.query.filter_by(email=data['email']).first()
        
        # Actualizar usuario
        
        user.rol_id = data['rol']
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({
            'message': 'Usuario actualizado exitosamente',
        }), 204
        
    except Exception as err:
        db.session.rollback()
        return jsonify({'error': str(err)}), 500