from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import cv2

CAT_CLASS_ID = 15

# Load YOLO model
model = YOLO("yolov8n.pt")
cat_tracks = []  # เก็บตำแหน่งการเคลื่อนที่ของแมว


def draw_boxes(frame, boxes):
    annotator = Annotator(frame)

    if boxes is None or len(boxes) == 0:
        return frame

    for box in boxes:
        class_id = int(box.cls[0])

        # detect only cat
        if class_id != CAT_CLASS_ID:
            continue

        coord = box.xyxy[0]

        # คำนวณจุดกึ่งกลางของ bounding box
        x_center = int((coord[0] + coord[2]) / 2)
        y_center = int((coord[1] + coord[3]) / 2)

        # เก็บตำแหน่ง
        cat_tracks.append((x_center, y_center))

        # จำกัดจำนวนจุด (กัน memory บวม)
        if len(cat_tracks) > 50:
            cat_tracks.pop(0)

        # วาด bounding box (สีน้ำเงิน)
        annotator.box_label(
            coord,
            "cat",
            color=(255, 0, 0)  # blue
        )

    # 🔵 วาดเส้น tracking
    for i in range(1, len(cat_tracks)):
        cv2.line(
            frame,
            cat_tracks[i - 1],
            cat_tracks[i],
            (0, 255, 0),  # green
            2
        )

    return annotator.result()

def detect_object(frame):
    """Detect object from image frame"""

    # Detect object from image frame
    results = model(frame)

    for result in results:
        frame = draw_boxes(frame, result.boxes)

     #  ข้อความมุมขวาบน (ชื่อผู้ทำ)
    text = "Yossawee-Clicknext-Internship-2024"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.9
    thickness = 2
    color = (0, 0, 255)  # สีแดง (BGR)
    #color= (255, 0, 0)  # สีฟ้า (BGR)
    # คำนวณตำแหน่งให้ชิดขวา
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    text_x = frame.shape[1] - text_size[0] - 20
    text_y = 40

    cv2.putText(
        frame,
        text,
        (text_x, text_y),
        font,
        font_scale,
        color,
        thickness,
        cv2.LINE_AA
    )
    return frame


if __name__ == "__main__":
    video_path = "CatZoomies.mp4"
    cap = cv2.VideoCapture(video_path)

   
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
          break

        frame_result = detect_object(frame)

        cv2.imshow("Video", frame_result)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


    # Release the VideoCapture object and close the window
    #video_writer.release()
    cap.release()
    cv2.destroyAllWindows()
