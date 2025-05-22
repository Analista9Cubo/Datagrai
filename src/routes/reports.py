
from datetime import datetime
from flask import Blueprint, request, jsonify
from ..db_con import db
from src.models.readings import Readings

report_bp = Blueprint('report', __name__)

@report_bp.route('/report', methods=['GET'])
def gen_report():
    try:
        # Validar datos de entrada
        start_date = request.args.get('start')
        end_date = request.args.get('end')

        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')

        response = Readings.query.filter(Readings.time >= start, Readings.time <= end).all()

        return jsonify({'alerts': [a.to_dict() for a in response]}), 200
        
    except Exception as err:
        db.session.rollback()
        return jsonify({'error': str(err)}), 500
    
