from flask import Blueprint, request, jsonify
from ..db_con import db
from ..models.readings import Readings
from sqlalchemy import create_engine, text
import smtplib
from email.mime.text import MIMEText
from src.models.alerts import Alert
from src.models.alert_rol import Alert_rol
from ..models.user import User

read_bp = Blueprint('read', __name__)

external_db_url = "postgresql://usuario:password@host:5432/otra_base"
external_engine = create_engine(external_db_url)

@read_bp.route('/read', methods=['POST'])
def register():
    try:
        # Validar datos de entrada
        data = request.get_json()

        # Crear nueva lectura
        
        for x in data:
            read = Readings(
                level = x['level'],
                time = x['time'],
                sensor = x['sensor'],
            )
            
            db.session.add(read)
            db.session.commit()

            alerts = Alert.query.filter_by(id_sensor = x['sensor'])
            for y in alerts:
                if x['level'] > y['umb_max'] or x['level'] < y['umb_min']:
                    remitente = 'danielrodf29@gmail.com'
                    password = 'wata qqcq fifh vxlk'
                    roles = Alert_rol.query.filter_by(id_alert = y['id'])
                    for z in roles:
                        usuarios = User.query.filter_by(rol_id = z['id_rol'])
                        for w in usuarios:
                            msg = MIMEText('Alerta nivel caudal')
                            msg['Subject'] = 'Alerta nivel'+ y['alert_level']
                            msg['From'] = remitente
                            msg['To'] = w['email']

                            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                                server.login(remitente, password)
                                server.send_message(msg)

        
        return jsonify({
            'message': 'Lecura registrada exitosamente',
        }), 201
    except Exception as err:
        db.session.rollback()
        return jsonify({'error': str(err)}), 500
    

@read_bp.route('/results', methods=['POST'])
def consulta_externa():
    try:
        with external_engine.connect() as connection:
            result = connection.execute(text("SELECT DISTINCT (rd.devaddress) * FROM readings_raw as rd ORDER BY ASC"))
            rows = [dict(row) for row in result]
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@read_bp.route('/getRead/<string:id>', methods=['GET'])
def get_read(id):
    
    sql = text("""
    SELECT AVG(level) AS promedio_nivel
    FROM readings_raw
    WHERE DATE_TRUNC('day', time) = DATE_TRUNC('day', CURRENT_DATE)
    AND sensor = :id
    """)

    avg_day = db.session.execute(sql, {'id': id}).scalar()


    sql = text("""
    SELECT AVG(level) AS promedio_nivel
    FROM readings_raw
    WHERE DATE_TRUNC('month', time) = DATE_TRUNC('month', CURRENT_DATE) 
    AND sensor = :id
    """)

    avg_month = db.session.execute(sql, {'id': id}).scalar()

    sql = text("""
    SELECT AVG(level) AS promedio_nivel
    FROM readings_raw
    WHERE DATE_TRUNC('quarter', time) = DATE_TRUNC('quarter', CURRENT_DATE) 
    AND sensor = :id
    """)

    avg_thri = db.session.execute(sql, {'id': id}).scalar()

    sensor = Readings.query.filter_by(sensor = id).first()



    if sensor:
        return jsonify({
            "id": sensor.sensor,
            "level": sensor.level,
            "avg_day": avg_day,
            "avg_month": avg_month,
            "avg_thri": avg_thri
        })
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404