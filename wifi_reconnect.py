import subprocess
import time
import sys

# ตั้งค่าชื่อ Wi-Fi ที่ต้องการเชื่อมต่อ
TARGET_SSID = "ggg"

def toggle_wifi(ssid):
    try:
        print(f"[{time.ctime()}] Disconnecting...")
        # สั่งตัดการเชื่อมต่อ
        subprocess.run(["netsh", "wlan", "disconnect"], check=True, capture_output=True)
        
        time.sleep(5) # รอ 5 วินาทีเพื่อให้ระบบเคลียร์สถานะ
        
        print(f"[{time.ctime()}] Connecting to {ssid}...")
        # สั่งเชื่อมต่อกลับไปยัง Profile ที่ระบุ
        result = subprocess.run(
            ["netsh", "wlan", "connect", f"name={ssid}"], 
            check=True, 
            capture_output=True, 
            text=True
        )
        
        # ตรวจสอบเบื้องต้นจาก Output ของคำสั่ง
        if "successfully" in result.stdout.lower() or result.returncode == 0:
            print(f"[{time.ctime()}] Reconnection command sent.")
        else:
            print(f"[{time.ctime()}] Warning: Reconnection might have failed.")
            
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    print(f"Script started. Target: {TARGET_SSID}. Interval: 24h.")
    while True:
        toggle_wifi(TARGET_SSID)
        
        # รอ 24 ชั่วโมง (86400 วินาที)
        print(f"Waiting for 24 hours...")
        time.sleep(10)