import cv2
import numpy as np

# 1. 创建一个空白图像作为画布
# 初始为黑色图像，尺寸 400x600 (高x宽)，3通道 (BGR)
img = np.zeros((400, 600, 3), np.uint8)

# 2. 创建窗口
window_name = 'Trackbar Demo'
cv2.namedWindow(window_name)

# 3. 定义一个回调函数
# Trackbar 的回调函数必须接受一个参数，即滑动条的当前位置。
# 在这个简单的例子中，我们不需要在回调函数中做任何事情，
# 因为我们会在主循环中实时获取滑动条的位置。
def on_trackbar_change(val):
    pass # 啥也不做，只是满足函数签名要求

# 4. 创建滑动条
# 参数：
# - 'Brightness': 滑动条的名称
# - window_name: 滑动条所属的窗口名称
# - 0: 滑动条的初始位置
# - 255: 滑动条的最大值
# - on_trackbar_change: 回调函数
cv2.createTrackbar('Brightness', window_name, 0, 255, on_trackbar_change)

# 5. 主循环：实时获取滑动条位置并更新图像
while True:
    # 获取滑动条的当前位置
    # 参数：
    # - 'Brightness': 滑动条的名称
    # - window_name: 滑动条所属的窗口名称
    brightness_value = cv2.getTrackbarPos('Brightness', window_name)

    # 根据滑动条的值改变图像亮度
    # 这里我们让图像的所有像素值都等于 brightness_value
    # 这样图像会从全黑 (0) 变为全白 (255)
    img[:] = brightness_value

    # 显示图像
    cv2.imshow(window_name, img)

    # 等待按键，如果按下 'q' 键则退出循环
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# 6. 释放资源
cv2.destroyAllWindows()
