from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    alert_type = data.get("event", "Unknown")
    timestamp = data.get("time")
    desc = data.get("description")

    filename = f"error_reports/alert_{timestamp.replace(':', '-')}.txt"
    os.makedirs("error_reports", exist_ok=True)

    with open(filename, "w") as f:
        f.write(f"Time: {timestamp}\n")
        f.write(f"Type: {alert_type}\n")
        f.write(f"Description: {desc}\n")

    return {"status": "alert saved"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
