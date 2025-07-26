from flask import Flask, jsonify
from datetime import datetime, timedelta
import random
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    ✅ Flask API is running.<br>
    Go to <a href="/data">/data</a> to view real-time sensor data.
    '''

@app.route('/data')
def get_data():
    all_data = []
    current_time = datetime.now()

    for t in range(50):  # 50 past timestamps
        timestamp = (current_time - timedelta(seconds=5 * t)).strftime("%Y-%m-%d %H:%M:%S")
        for i in range(1, 6):  # 5 sensors
            all_data.append({
                "DeviceID": f"Sensor-{i}",
                "Temperature": round(random.uniform(20, 35), 2),
                "Humidity": round(random.uniform(30, 80), 2),
                "Timestamp": timestamp
            })
    return jsonify(all_data)

# Function to launch browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/data")

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()  # open after server starts
    app.run(port=5000)
