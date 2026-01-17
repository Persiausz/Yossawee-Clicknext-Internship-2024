# How to Run the Project
### STEP 1
python3 -m venv venv

### STEP 2
source venv/bin/activate

### STEP 3
pip install -r requirements.txt

### STEP 4
python3 yolo_detector.py

(กด q เพื่อออกจากโปรแกรม)

# Output Features

โปรแกรมจะแสดง:

1. Bounding Box สีน้ำเงิน ตรวจจับเฉพาะแมว (Cat only)

2. Tracking Line แสดงเส้นทางการเคลื่อนที่ของแมว

3. Developer Name Overlay (มุมขวาบน)

# เพิ่มเติม

ไม่มีการบันทึกไฟล์วิดีโอออก (เพิ่ม FPS)

ใช้ YOLO สำหรับ Object Detection

Ignore classes อื่นทั้งหมด (ตรวจจับเฉพาะ Cat)



