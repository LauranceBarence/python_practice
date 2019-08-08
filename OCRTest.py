from PIL import Image
import pytesseract
import requests


def convert_img(img, threshold):
    img = img.convert('L')
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img


def de_noise(img):
    data = img.getdata()
    w, h = img.size
    count = 0
    for x in range(1, h - 1):
        for y in range(1, h - 1):
            mid_pixel = data[w * y + x]
            if mid_pixel == 0:
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                right_pixel = data[w * y + (x + 1)]
                bottom_pixel = data[w * (y + - 1) + x]
                if top_pixel == 0:
                    count += 1
                if left_pixel == 0:
                    count += 1
                if right_pixel == 0:
                    count += 1
                if bottom_pixel == 0:
                    count += 1
                if count > 4:
                    img.putpixel((x, y), 0)
    return img


res = requests.get('http://49.4.7.76:8081/financial/getVerifyCode')
with open('./file/OCR/test.jpg','wb') as file:
    content = res.content
    file.write(content)
file.close()
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
captcha = Image.open('./file/OCR/test.jpg')
result = convert_img(captcha, 150)
result = de_noise(result)
result.show()
result = pytesseract.image_to_string(result)
print(result)
