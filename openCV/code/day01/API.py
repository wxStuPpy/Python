import cv2

cv2.namedWindow('new',cv2.WINDOW_NORMAL)
cv2.resizeWindow('new',666,300)
cv2.imshow('new',0)

import cv2

# 读取图片（确保路径正确）
img = cv2.imread("D:/code/Python/openCV/image/test.png")

key=cv2.waitKey(0)

if key==ord('q'):
    exit(0)
elif key==ord('s'):
    if img is not None:
        save_path = "D:/code/Python/openCV/image/saved_image.png"  # 带.png扩展名
        success = cv2.imwrite(save_path, img)
        if success:
            print(f"图片已成功保存到：{save_path}")
        else:
            print("保存失败，请检查路径是否存在或权限是否足够")
    else:
        print("无法读取原图，请检查图片路径是否正确")

cv2.destroyAllWindows()