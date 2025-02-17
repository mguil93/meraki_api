from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# ✅ Load Meraki API Key from environment variables
MERAKI_API_KEY = os.getenv("MERAKI_API_KEY")

# ✅ Check if API key is set
if not MERAKI_API_KEY:
    raise ValueError("❌ ERROR: MERAKI_API_KEY is not set. Please add it to environment variables.")

# ✅ Headers for Meraki API requests
HEADERS = {"X-Cisco-Meraki-API-Key": MERAKI_API_KEY, "Content-Type": "application/json"}

# ✅ Replace with your actual Meraki Organization ID
MERAKI_ORG_ID = "983899"

# ✅ Fetch Meraki Network List
@app.route('/meraki/networks', methods=['GET'])
def get_networks():
    url = f"https://api.meraki.com/api/v1/organizations/{MERAKI_ORG_ID}/networks"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": f"Failed to fetch networks: {response.status_code}", "details": response.text})

# ✅ Dynamic port assignment for Render deployment
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render dynamically assigns a port
    app.run(host="0.0.0.0", port=port, debug=True)


