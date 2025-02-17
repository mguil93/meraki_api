from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Get API key from Render environment variables
MERAKI_API_KEY = os.getenv("66543d94de5e4baf371c5bc2b7f6a3d4166e1b9d")
HEADERS = {"X-Cisco-Meraki-API-Key": MERAKI_API_KEY, "Content-Type": "application/json"}

# Replace with your Meraki Organization ID
MERAKI_ORG_ID = "983899"

# Fetch Meraki Network List
@app.route('/meraki/networks', methods=['GET'])
def get_networks():
    url = f"https://api.meraki.com/api/v1/organizations/{MERAKI_ORG_ID}/networks"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Failed to fetch networks", "status": response.status_code})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
