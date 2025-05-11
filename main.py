from src import create_app

app = create_app()

@app.route("/")
def index():
    return "Aplicación en ejecución"


if __name__ == '__main__':
    port = 5000
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=True)