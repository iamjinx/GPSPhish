from flask import Flask, render_template, request, jsonify
import csv, os, requests
from datetime import datetime

app = Flask(__name__)
CSV_FILE = 'data.csv'

# Function to create the CSV file if it doesn't exist
def create_csv_if_not_exists():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as csv_file:
            fieldnames = ['Sl No.', 'Date and Time', 'Googlemap-Links', 'Ip Address']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

# Function to get the next available serial number
def get_sn():
    with open(CSV_FILE, mode='r', newline='') as csv_file:
        return str(sum(1 for _ in csv.DictReader(csv_file)) + 1)

# Function to get the user's IP address
def get_user_ip():
    try:
        response = requests.get("https://ident.me/")
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    create_csv_if_not_exists()
    return render_template('index.html')

@app.route('/save_coordinates', methods=['POST'])
def save_coordinates():
    create_csv_if_not_exists()

    data = request.get_json()
    lat, lon = data['lat'], data['lon']
    ip_address = get_user_ip()
    sn_no = get_sn()
    current_datetime = datetime.now().strftime('%d-%M-%Y %H:%M %p')

    with open(CSV_FILE, mode='a', newline='') as csv_file:
        fieldnames = ['Sl No.', 'Date and Time', 'Googlemap-Links', 'Ip Address']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'Sl No.': sn_no, 'Date and Time': current_datetime, 'Googlemap-Links': f'https://maps.google.com/?q={lat},{lon}', 'Ip Address': ip_address})
    return ('', 204, {'Content-Type': 'application/json'})

if __name__ == '__main__':
    app.run(debug=True)
