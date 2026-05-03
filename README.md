# Wi-Fi Reconnect Script

สคริปต์ Python สำหรับตัดการเชื่อมต่อ Wi-Fi แล้วเชื่อมต่อกลับอัตโนมัติบน Windows โดยใช้คำสั่ง `netsh` และทำงานซ้ำทุก 24 ชั่วโมง

## English

### How It Works

- Disconnects Wi-Fi with `netsh wlan disconnect`
- Waits 5 seconds
- Reconnects with `netsh wlan connect name=<profile>`
- Repeats every 24 hours

### Requirements

- Windows only
- `netsh` must be available
- The value in `TARGET_SSID` must match an existing Wi-Fi profile name on the machine

### Usage

1. Open `wifi_reconnect.py`
2. Set `TARGET_SSID` to the Wi-Fi profile name you want to reconnect to
3. Open PowerShell or Command Prompt in the project folder
4. Run

```bash
python wifi_reconnect.py
```

### Notes

- The script runs continuously in a loop
- Press `Ctrl + C` to stop it
- If reconnect fails, check that the Wi-Fi profile exists and the name is correct

## ภาษาไทย

### การทำงาน

- ตัดการเชื่อมต่อ Wi-Fi ด้วย `netsh wlan disconnect`
- รอ 5 วินาที
- เชื่อมต่อกลับด้วย `netsh wlan connect name=<profile>`
- ทำซ้ำทุก 24 ชั่วโมง

### ข้อกำหนด

- ใช้บน Windows เท่านั้น
- ต้องมีคำสั่ง `netsh` ใช้งานได้
- ชื่อในตัวแปร `TARGET_SSID` ต้องตรงกับชื่อ Wi-Fi profile ที่มีอยู่ในเครื่อง

### วิธีใช้งาน

1. เปิดไฟล์ `wifi_reconnect.py`
2. แก้ค่า `TARGET_SSID` ให้เป็นชื่อโปรไฟล์ Wi-Fi ที่ต้องการเชื่อมต่อ
3. เปิด PowerShell หรือ Command Prompt ในโฟลเดอร์โปรเจกต์
4. รันคำสั่ง

```bash
python wifi_reconnect.py
```

### หมายเหตุ

- สคริปต์นี้จะทำงานวนลูปตลอดเวลา
- ถ้าต้องการหยุด ให้กด `Ctrl + C`
- ถ้าเชื่อมต่อไม่สำเร็จ ให้ตรวจสอบว่า Wi-Fi profile มีอยู่จริงและชื่อถูกต้อง
