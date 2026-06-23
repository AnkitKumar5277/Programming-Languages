import cv2
source = "ankit.png"
destination = 'new_image.jpg'
scale_percent = 50
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

nayi_width = int(src.shape[1] * scale_percent / 100)
nayi_height = int(src.shape[0] * scale_percent / 100)

output = cv2.resize(src, (nayi_width, nayi_height))
cv2.imwrite(destination, output)  
