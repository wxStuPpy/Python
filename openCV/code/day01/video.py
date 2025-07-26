import cv2
import os

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)
cv2.resizeWindow('video', 600, 400)

# 打开输入视频
v = cv2.VideoCapture('D:/Download/test_video.mp4')

# 检查视频是否成功打开
if not v.isOpened():
    print("错误：无法打开输入视频文件。请检查路径或文件是否存在。")
    exit()

# 获取输入视频的参数
fps = v.get(cv2.CAP_PROP_FPS)
width = int(v.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))

# --- 重点修改这里：使用 XVID 编码器和 .avi 格式 ---
output_filename = '../../image/output_xvid.avi' # 注意：文件扩展名必须是 .avi
output_filepath = os.path.join('.', output_filename) # 保存到当前目录

print(f"尝试将视频保存到: {output_filepath}")

# 定义编码器：XVID (MPEG-4 Part 2)
# 这是 .avi 容器中一个非常常用且效果好的编码器
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 初始化输出视频
out = cv2.VideoWriter(output_filepath, fourcc, fps, (width, height))

# 检查输出视频是否成功初始化
if not out.isOpened():
    print(f"致命错误：无法创建输出视频文件 '{output_filepath}'。")
    print("可能原因：")
    print("1. 路径不存在或无写入权限。")
    print("2. 编码器 (XVID) 或其与 .avi 容器的组合在当前系统上不受支持。")
    print("3. 磁盘空间不足。")
    print("请尝试：")
    print(" - 确保目标文件夹存在且你有写入权限。")
    print(" - 检查磁盘空间。")
    exit()
else:
    print(f"成功初始化 VideoWriter，准备写入到 {output_filepath}")


while True:
    ret, frame = v.read()
    if not ret:
        print("视频读取完毕或失败。")
        break

    # 确保帧是有效的，并且尺寸与 VideoWriter 初始化时一致
    if frame is None or frame.shape[1] != width or frame.shape[0] != height:
        print(f"警告：读取到无效帧或帧尺寸不匹配。跳过此帧。帧尺寸: {frame.shape if frame is not None else 'None'}")
        continue

    out.write(frame)
    cv2.imshow('video', frame)

    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        print("用户按下 'q' 键，退出。")
        break

# 释放资源
out.release()
v.release()
cv2.destroyAllWindows()
print("所有资源已释放。")
