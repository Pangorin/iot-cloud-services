import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

# 1. Kết nối Firebase
cred = credentials.Certificate("/Users/pangorin/Documents/GitHub/iot-cloud-services/iot-cloud-services-firebase-adminsdk-fbsvc-81e3555c5f.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-cloud-services-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# 2. Dữ liệu mẫu
data = {
    "ID": "ENV001",
    "Name": "Station A",
    "Time": datetime.utcnow().isoformat(),
    "Temperature": 29.5,
    "Humidity": 70.2,
    "Wind": 12.3,
    "Pressure": 1008.5
}

# 3. Gửi dữ liệu
ref = db.reference("environment_data")
ref.push(data)

print("✅ Dữ liệu đã được gửi lên Firebase!")
