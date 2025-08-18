import firebase_admin
from firebase_admin import credentials, db

# 1. Kết nối Firebase
cred = credentials.Certificate("/Users/pangorin/Documents/GitHub/iot-cloud-services/iot-cloud-services-firebase-adminsdk-fbsvc-81e3555c5f.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-cloud-services-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Lấy toàn bộ dữ liệu
ref = db.reference("environment_data")
data = ref.get()

if data:
    print("📊 Dữ liệu môi trường:")
    temps = []
    for key, entry in data.items():
        print(entry)
        temps.append(entry["Temperature"])
    
    avg_temp = sum(temps) / len(temps)
    print(f"🌡 Nhiệt độ trung bình: {avg_temp:.2f}°C")
else:
    print("Không có dữ liệu.")
