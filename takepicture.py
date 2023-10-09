import cv2

def take_picture(file_name="img.jpg"):
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open camera.")
            return False
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(file_name, frame)
            print(f"Picture saved as {file_name}")
            return True
        else:
            print("Error: Could not capture a frame.")
            return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
    finally:
        if cap.isOpened():
            cap.release()
