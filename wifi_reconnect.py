import subprocess
import time
import random

# ตั้งค่าชื่อ Wi-Fi ที่ต้องการเชื่อมต่อ
TARGET_SSID = "IOT-RMUTI"
# TARGET_SSID = "ggg"

MIN_INTERVAL_HOURS = 12
MAX_INTERVAL_HOURS = 24


def get_random_interval_seconds(min_hours, max_hours):
    return random.randint(min_hours * 3600, max_hours * 3600)

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
    print(
        f"Script started. Target: {TARGET_SSID}. "
        f"Random interval: {MIN_INTERVAL_HOURS}-{MAX_INTERVAL_HOURS}h."
    )

    while True:
        toggle_wifi(TARGET_SSID)

        wait_seconds = get_random_interval_seconds(MIN_INTERVAL_HOURS, MAX_INTERVAL_HOURS)
        wait_hours = wait_seconds / 3600

        # รอแบบสุ่มระหว่าง 6 ถึง 24 ชั่วโมง
        print(f"Waiting for {wait_hours:.2f} hours ({wait_seconds} seconds)...")
        time.sleep(wait_seconds)