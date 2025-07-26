import cv2

# 打开默认摄像头（0表示默认摄像头，多个摄像头可尝试1、2等）
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
else:
    # 获取分辨率（宽和高）
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"摄像头默认分辨率：{width} x {height}")

    # 可选：尝试获取摄像头支持的最大分辨率（部分摄像头支持）
    # 注意：并非所有摄像头都支持修改分辨率，需根据硬件能力
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    max_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    max_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if (max_width, max_height) != (width, height):
        print(f"摄像头支持的最大分辨率：{max_width} x {max_height}")

# 释放资源
cap.release()
