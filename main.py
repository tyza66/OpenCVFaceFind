import cv2

'''img = cv2.imread(r'lenna.png')
cv2.imshow('Original Image',img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

cv2.waitKey(0)
'''
# 1表示彩色图像，0表示灰阶图像，-1表示带阿尔法通道的图像
img = cv2.imread(r'lenna.png', 0)
print(img)
print(img.shape)
cv2.imshow('Lenna', img)
# 按下esc时，关闭窗口，按下s保存图片
k = cv2.waitKey(0)
''' 这里本身esc退出按钮已经内置了
if k == 27:
    cv2.destroyWindow("Grey")
'''
if k == 115:
    cv2.imwrite(r'Lenna_grey.png', img)

# 改变图像比例
resized_img = cv2.resize(img, (200, 500))
cv2.imshow("Lenna_small", resized_img)
k = cv2.waitKey(0)
if k == 115:
    cv2.imwrite(r'Lenna_grey_silm.png', img)

# 不使用改变图像比例
resized_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
cv2.imshow("Lenna_small", resized_img)
k = cv2.waitKey(0)
if k == 115:
    cv2.imwrite(r'Lenna_grey_silm_good.png', img)

#
img = cv2.imread(r"lenna.png")
gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("lenna_grey", gary)
k = cv2.waitKey(0)
if k == 115:
    cv2.imwrite(r'Lenna_grey_silm_good_good.png', img)
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
# 第一个是传入想要检测的图像，第二个是指定每次图像缩小的比例 第三个是每个目标至少要比较几次
faces = face_cascade.detectMultiScale(gary, scaleFactor=1.05, minNeighbors=5)
for x,y,w,h in faces:
    img2 = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("Lenna_find",img2)
k = cv2.waitKey(0)
if k == 115:
    cv2.imwrite(r'Lenna_grey_silm_good_good.png', img)
