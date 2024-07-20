from flask import Flask, jsonify #for making API
import os

app = Flask(__name__)
#Get API for temperature 
@app.route('/temperature', methods=['GET'])
def get_temperature():
    try:
        # Ensure the data file exists before opening
        file_path = 'temperatureData.txt'
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found"}), 404 #error code
# Open and do write opration
        with open(file_path, 'r') as file:
            lines = file.readlines()

            if lines:
                latest_entry = lines[-1].strip().split(', ')
                if len(latest_entry) != 2:
                    return jsonify({"error": "Incorrect file format"}), 400

                timestamp = latest_entry[0]
                try:
                    temperature = float(latest_entry[1])
                except ValueError:
                    return jsonify({"error": "Invalid temperature value"}), 400
# Output is temperature with timestamp
                return jsonify({"timestamp": timestamp, "temperature": temperature})

            else:
                return jsonify({"error": "No data available"}), 404

    except Exception as e:
        # Catch any other exceptions
        return jsonify({"error": str(e)}), 500 #error code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # Run on all available IP addresses on only this port 8000
