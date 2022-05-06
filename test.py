import time

import cv2
t1 = time.time()
print(t1)
# 参数0表示默认为笔记本的内置第一个摄像头，如果需要读取已有的视频则参数改为视频所在路径，
# 例如：cap = cv2.VideoCapture('video.mp4'),或者参数填视频的url也是可以的
cap = cv2.VideoCapture(0)

# 判断视频对象是否成功读取，成功读取视频对象返回true
# 判断载入的视频是否可以打开
# 按帧读取视频，返回值ret是布尔型，正确读取则返回true，读取失败或未读取到视频结尾返回false
# frame 为每一帧的图像，这里图像是三维矩阵，即frame.shape = (640,480,3)，
# 读取的图像为BGR格式
# ret,frame = cap.read()
# t2 = time.time()
# print(t2)
# print(t2-t1)
#
# ret,frame = cap.read()
# t3 = time.time()
# print(t3)
# print(t3-t2)
# print(cv2.CAP_PROP_AUTO_EXPOSURE)
# cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,0.25)
# cap.set(cv2.CAP_PROP_EXPOSURE,-14)
# print(cv2.CAP_PROP_AUTO_EXPOSURE)
# cv2.imshow("1",frame)

for i in range(20):
    t1 = time.time()
    ret, frame = cap.read()
    t2 = time.time()
    print(t2 - t1)
    # cv2.imshow("1", frame)
# 等待键盘输入，参数1表示延时1ms切换到下一帧，参数为0表示显示当前帧，相当于暂停
key = cv2.waitKey(0)
