import cv2

# 打印 OpenCV 版本号
print("OpenCV 版本:", cv2.__version__)

# 尝试读取并显示一张图片（可选，需提前准备一张图片）
try:
    # 替换为你的图片路径，例如 "test.jpg"
    img = cv2.imread("../../image/test.png")

    if img is not None:
        print("图片读取成功，尺寸:", img.shape)
        # 显示图片（会弹出一个窗口）
        cv2.imshow("Test Image", img)
        # 创建可调整大小的窗口
        cv2.namedWindow("aaa", cv2.WINDOW_NORMAL)
        cv2.waitKey(0)  # 等待任意按键关闭窗口
        cv2.destroyAllWindows()
    else:
        print("图片读取失败，请检查路径是否正确")
except Exception as e:
    print("测试过程出错:", e)