1. Cat Detection Using YOLO

ใช้โมเดล YOLO (You Only Look Once) สำหรับตรวจจับวัตถุแบบ Real-time

จำกัดการตรวจจับเฉพาะ แมว (Cat class) เพื่อให้เหมาะกับโจทย์

แสดง Bounding Box และ Confidence Score บนวิดีโอ

2. Improve Real-Time Performance

ปรับโครงสร้างโค้ดให้เหมาะกับการประมวลผลแบบ Real-time

ลดขั้นตอนที่ไม่จำเป็นใน Loop การตรวจจับ

ทำให้ FPS สูงขึ้นและการแสดงผลลื่นขึ้น

3. Remove Video Writer Function to Increase FPS

ลบฟังก์ชัน VideoWriter (การบันทึกวิดีโอผลลัพธ์ลงไฟล์)

ลดภาระการเขียนไฟล์ระหว่างรัน

ส่งผลให้ระบบสามารถตรวจจับแมวได้เร็วขึ้น (FPS เพิ่มขึ้น)

4. Modify Bounding Box Color

ปรับสี Bounding Box ของแมวที่ตรวจจับได้เป็น สีน้ำเงิน (Blue)

ช่วยให้แยกแยะวัตถุที่ตรวจจับได้ชัดเจนขึ้นบนหน้าจอ

5. Draw Tracking Line for the Detected Cat

เพิ่มฟังก์ชัน Object Tracking

บันทึกตำแหน่งศูนย์กลาง (centroid) ของแมวในแต่ละเฟรม

วาดเส้นทางการเคลื่อนที่ (Tracking Line) เพื่อแสดงพฤติกรรมการเคลื่อนไหวของแมว

6. Code Organization and Cleanup

จัดระเบียบโครงสร้างไฟล์ในโปรเจกต์

ลบไฟล์ที่ไม่ควรอยู่ใน Repository เช่น:

venv/

ไฟล์วิดีโอ .avi

ใช้ .gitignore เพื่อป้องกันการ push ไฟล์ที่ไม่จำเป็น

7. Version Control with Git & GitHub

ใช้ Git ในการจัดการเวอร์ชันของซอร์สโค้ด

Commit การเปลี่ยนแปลงอย่างเป็นขั้นตอน

Push โปรเจกต์ขึ้น GitHub (Public Repository) เพื่อให้สามารถตรวจสอบและใช้งานได้
