![GPSPhish](GPSPhish.jpg)
# GPSPhish

GPSPhish is a phishing tool designed to capture the exact GPS location of the target user.

## Installation

You can install GPSPhish by following these steps:

1. Clone the GPSPhish repository:
    ```bash
    git clone https://github.com/iamjinx/GPSPhish.git
    ```
2. Navigate to the project directory:
    ```bash
    cd GPSPhish
    ```
3. Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use GPSPhish, follow these steps:
1. Open a terminal and generate an SSH key for your local machine by running the following command:
    ```bash
    ssh-keygen
    ```
    When prompted, press "yes" to verify, and it will generate an SSH key pair.
2. Run the following command to start the GPSPhish and the Flask server:

    ```bash
    python3 gpsPhish.py
    ```
    This will start a Flask server on port 5000 on your local host.
3. Open another terminal instance and execute the following command to create an SSH tunnel:
    ```bash
    ssh srv.us -R 1:127.0.0.1:5000
    ```
    This will create a tunnel that forwards traffic from port 1 on srv.us to your local machine's port 5000.

4. You will now have a phishing URL. Send this URL to the target user.

5. When your target visits the phishing link and clicks on the "get weather info" button, they will be prompted to grant location permission.

6. Once the target allows location permission, you will receive the exact coordinates and a Google Maps link to that location, along with the target's IP address in the data.csv file.

**Please use this tool responsibly and only for ethical purposes. Unauthorized use for phishing or other malicious activities is illegal and unethical.**

## Disclaimer
This tool is provided for educational and research purposes only. The developer of GPSPhish is not responsible for any misuse or illegal activities performed using this tool.
