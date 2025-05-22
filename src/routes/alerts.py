from flask import Blueprint, request, jsonify
from ..db_con import db
from src.models.alerts import Alert
from src.models.alert_rol import Alert_rol



alert_bp = Blueprint('alert', __name__)

@alert_bp.route('/createAlert', methods=['POST'])
def create_alert():
    try:
        # Validar datos de entrada
        data = request.get_json()
        
        
        alert = Alert(
        alert_level = data['alert_level'],
        id_sensor = data['id_sensor'],
        umb_min = data['umb_min'],
        umb_max = data['umb_max']

        )

        db.session.add(alert)
        db.session.commit()

        for x in data['roles']:
            alert_rol = Alert_rol(
                id_alert = alert.id,
                id_rol = x
            )        
            db.session.add(alert_rol)
            db.session.commit()
        
        
        return jsonify({
            'message': 'Alerta creada exitosamente',
        }), 201
        
    except Exception as err:
        db.session.rollback()
        return jsonify({'error': str(err)}), 500
    



@alert_bp.route('/updateAlert', methods=['PUT'])
def edit_alert():
    try:
        # Validar datos de entrada
        data = request.get_json()

        roles = Alert_rol.query.filter_by(id_alert=data['id'])
        for r in roles:
            db.session.delete(r)
        db.session.commit()
        
        alert =Alert.query.filter_by(id=data['id']).first()
        
        # Actualizar alerta
        
        alert.alert_level = data['alert_level']
        alert.umb_min = data['umb_min']
        alert.umb_max = data['umb_max']

        db.session.commit()

        for x in data['roles']:
            alert_rol = Alert_rol(
                id_alert = data['id'],
                id_rol = x
            )        
            db.session.add(alert_rol)
        
        db.session.commit()
        
        
        return jsonify({
            'message': 'Alerta actualizada exitosamente',
        }), 204
        
    except Exception as err:
        db.session.rollback()
        return jsonify({'error': str(err)}), 500
    
@alert_bp.route('/getAlerts', methods=['GET'])
def get_alerts():
    try:
        
        alerts =Alert.query.all()
        return jsonify({'alerts': [a.to_dict() for a in alerts]}), 200
        
    except Exception as err:
        db.session.rollback()
        return jsonify({'error': str(err)}), 500
    

@alert_bp.route('/getAlert/<int:id>', methods=['GET'])
def get_alert(id):
    try:
        
        alert =Alert.query.get(id)

        roles = Alert_rol.query.filter_by(id_alert = id)

        return jsonify({'alert': alert.to_dict(),
                        'roles': [r.to_dict() for r in roles]}), 200
        
    except Exception as err:
        db.session.rollback()
        return jsonify({'error': str(err)}), 500