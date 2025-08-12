# IoT Environment Data with Firebase

This project demonstrates a simple IoT setup where environmental data is sent to a **Firebase Realtime Database** and displayed on a web page in real time.

## Overview
- **App 1:** Sends environment data (ID, Name, Time, Temperature, Humidity, Wind, Pressure) to Firebase in JSON format.
- **App 2:** Reads the data from Firebase and shows it on a web page in a table.

## Technologies
- Firebase Realtime Database
- HTML, CSS, JavaScript
- Python (for data sending)

## How It Works
1. **Python script** generates or reads environment data and sends it to Firebase.
2. **Web page** listens to changes in Firebase and updates the table instantly.

## Usage
1. Create a Firebase project and enable Realtime Database.
2. Add your Firebase config to `index.html` and your Python script.
3. Run the Python script to send data.
4. Open `index.html` in a browser to view live updates.

## Results
![Page](https://github.com/Pangorin/iot-cloud-services/blob/main/images/3.png)

## Notes
- Make sure your Firebase rules allow read/write for testing.
- Use authentication and secure rules for production.

## License
MIT License

