from flask import Flask, render_template, jsonify
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar las variables del archivo .env

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/config')
def get_config():
    # Aquí puedes cargar las credenciales de un archivo o del entorno
    config = {
        "speechRegion": os.getenv("SPEECH_REGION"),
        "speechKey": os.getenv("SPEECH_KEY"),
        "openaiEndpoint": os.getenv("OPENAI_ENDPOINT"),
        "openaiKey": os.getenv("OPENAI_KEY"),
        "openaiDeployment": os.getenv("OPENAI_DEPLOYMENT")
    }
    return jsonify(config)

@app.route('/avatar-session')
def avatar_session():
    return render_template('avatar_session.html')  # Este es el archivo HTML para la sesión con el avatar

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
