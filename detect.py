import cv2
import numpy as np

def detect_colors(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı için iki aralık (HSV renk uzayında)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    # Yeşil aralığı
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])

    # Siyah aralığı (düşük parlaklık ve düşük doygunluk)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])
    # Trackbar arayüzü için pencere oluştur
    def nothing(x):
        pass

    cv2.namedWindow("Color Adjustments", cv2.WINDOW_NORMAL)

    # Kırmızı 1
    cv2.createTrackbar("Red1 Low H", "Color Adjustments", lower_red1[0], 179, nothing)
    cv2.createTrackbar("Red1 Low S", "Color Adjustments", lower_red1[1], 255, nothing)
    cv2.createTrackbar("Red1 Low V", "Color Adjustments", lower_red1[2], 255, nothing)
    cv2.createTrackbar("Red1 High H", "Color Adjustments", upper_red1[0], 179, nothing)
    cv2.createTrackbar("Red1 High S", "Color Adjustments", upper_red1[1], 255, nothing)
    cv2.createTrackbar("Red1 High V", "Color Adjustments", upper_red1[2], 255, nothing)
    # Kırmızı 2
    cv2.createTrackbar("Red2 Low H", "Color Adjustments", lower_red2[0], 179, nothing)
    cv2.createTrackbar("Red2 Low S", "Color Adjustments", lower_red2[1], 255, nothing)
    cv2.createTrackbar("Red2 Low V", "Color Adjustments", lower_red2[2], 255, nothing)
    cv2.createTrackbar("Red2 High H", "Color Adjustments", upper_red2[0], 179, nothing)
    cv2.createTrackbar("Red2 High S", "Color Adjustments", upper_red2[1], 255, nothing)
    cv2.createTrackbar("Red2 High V", "Color Adjustments", upper_red2[2], 255, nothing)
    # Yeşil
    cv2.createTrackbar("Green Low H", "Color Adjustments", lower_green[0], 179, nothing)
    cv2.createTrackbar("Green Low S", "Color Adjustments", lower_green[1], 255, nothing)
    cv2.createTrackbar("Green Low V", "Color Adjustments", lower_green[2], 255, nothing)
    cv2.createTrackbar("Green High H", "Color Adjustments", upper_green[0], 179, nothing)
    cv2.createTrackbar("Green High S", "Color Adjustments", upper_green[1], 255, nothing)
    cv2.createTrackbar("Green High V", "Color Adjustments", upper_green[2], 255, nothing)
    # Siyah
    cv2.createTrackbar("Black Low H", "Color Adjustments", lower_black[0], 179, nothing)
    cv2.createTrackbar("Black Low S", "Color Adjustments", lower_black[1], 255, nothing)
    cv2.createTrackbar("Black Low V", "Color Adjustments", lower_black[2], 255, nothing)
    cv2.createTrackbar("Black High H", "Color Adjustments", upper_black[0], 179, nothing)
    cv2.createTrackbar("Black High S", "Color Adjustments", upper_black[1], 255, nothing)
    cv2.createTrackbar("Black High V", "Color Adjustments", upper_black[2], 255, nothing)

    # Trackbar'dan değerleri oku
    lower_red1 = np.array([
        cv2.getTrackbarPos("Red1 Low H", "Color Adjustments"),
        cv2.getTrackbarPos("Red1 Low S", "Color Adjustments"),
        cv2.getTrackbarPos("Red1 Low V", "Color Adjustments")
    ])
    upper_red1 = np.array([
        cv2.getTrackbarPos("Red1 High H", "Color Adjustments"),
        cv2.getTrackbarPos("Red1 High S", "Color Adjustments"),
        cv2.getTrackbarPos("Red1 High V", "Color Adjustments")
    ])
    lower_red2 = np.array([
        cv2.getTrackbarPos("Red2 Low H", "Color Adjustments"),
        cv2.getTrackbarPos("Red2 Low S", "Color Adjustments"),
        cv2.getTrackbarPos("Red2 Low V", "Color Adjustments")
    ])
    upper_red2 = np.array([
        cv2.getTrackbarPos("Red2 High H", "Color Adjustments"),
        cv2.getTrackbarPos("Red2 High S", "Color Adjustments"),
        cv2.getTrackbarPos("Red2 High V", "Color Adjustments")
    ])
    lower_green = np.array([
        cv2.getTrackbarPos("Green Low H", "Color Adjustments"),
        cv2.getTrackbarPos("Green Low S", "Color Adjustments"),
        cv2.getTrackbarPos("Green Low V", "Color Adjustments")
    ])
    upper_green = np.array([
        cv2.getTrackbarPos("Green High H", "Color Adjustments"),
        cv2.getTrackbarPos("Green High S", "Color Adjustments"),
        cv2.getTrackbarPos("Green High V", "Color Adjustments")
    ])
    lower_black = np.array([
        cv2.getTrackbarPos("Black Low H", "Color Adjustments"),
        cv2.getTrackbarPos("Black Low S", "Color Adjustments"),
        cv2.getTrackbarPos("Black Low V", "Color Adjustments")
    ])
    upper_black = np.array([
        cv2.getTrackbarPos("Black High H", "Color Adjustments"),
        cv2.getTrackbarPos("Black High S", "Color Adjustments"),
        cv2.getTrackbarPos("Black High V", "Color Adjustments")
    ])
    # Maskeleri oluştur
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_black = cv2.inRange(hsv, lower_black, upper_black)

    # Her maskede tespit edilen piksel sayısı
    red_count = cv2.countNonZero(mask_red)
    green_count = cv2.countNonZero(mask_green)
    black_count = cv2.countNonZero(mask_black)

    detected = []
    if red_count > 500:
        detected.append("red")
    if green_count > 500:
        detected.append("green")
    if black_count > 500:
        detected.append("black")

    return detected

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Kamera açılamadı!")
        return

    print("Kamera açıldı. Çıkmak için 'q' tuşuna basın.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Görüntü alınamadı!")
            break

        detected_colors = detect_colors(frame)
        print("Tespit edilen renkler:", detected_colors)

        # Görüntüye tespit edilen renkleri yaz
        cv2.putText(frame, f"Detected: {', '.join(detected_colors)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

        cv2.imshow('Color Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__== "__main__":
    main()