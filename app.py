from flask import Flask, jsonify, request
import pandas as pd
import io

app = Flask(__name__) # Este es el 'app' que el servidor busca

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "ML Skill lista."
        "author": "Juanjo"
    })
@app.route('/test')
def test():
    return jsonify({"info": "Aquí irá el análisis de datos"})
    
@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    df = pd.read_csv(io.StringIO(file.stream.read().decode("UTF8")))
    
    report = {
        "rows": int(df.shape[0]),
        "cols": int(df.shape[1]),
        "columns": list(df.columns)
    }
    return jsonify(report)

# Importante: para que funcione el entrypoint app:app
main = app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

