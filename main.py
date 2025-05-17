from src import create_app
from apscheduler.schedulers.background import BackgroundScheduler
import requests

app = create_app()

@app.route("/")
def index():
    return "Aplicación en ejecución"

# Función del scheduler que llama al endpoint
def llamar_al_endpoint():
    try:
        response = requests.post("http://localhost:5000/read/results")
        
        print(f"⏱ Llamada automática respondida con {response.status_code}")
    except Exception as e:
        print(f"❌ Error al llamar al endpoint: {e}")

# Iniciar el scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=llamar_al_endpoint, trigger="interval", minutes=10)
scheduler.start()


if __name__ == '__main__':
    port = 5000
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=True)