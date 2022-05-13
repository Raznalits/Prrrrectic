import numpy as np
import cv2 as cv

print("Координаты точки A(x1;y1):")
x1 = int(input("\tx1 = "))
y1 = int(input("\ty1 = "))
print("Координаты точки B(x2;y2):")
x2 = int(input("\tx2 = "))
y2 = int(input("\ty2 = "))

print("Координаты точки A(x10;y10):")
x10 = int(input("\tx1 = "))
y10 = int(input("\ty1 = "))
print("Координаты точки B(x20;y20):")
x20 = int(input("\tx2 = "))
y20 = int(input("\ty2 = "))
print("Уравнение прямой, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
print(" y = %.2f*x + %.2f" % (k, b))
y = k*x20 + b
if y10 < y < y20:
    print("Вход")
elif y20 < y < y10:
    print("Выход")
else:
    print("Не пересекает")

img = np.zeros((512, 512, 3), np.uint8)

cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2, cv.LINE_8)
cv.imshow('line', img)
cv.waitKey(0)
cv.destroyAllWindow()
