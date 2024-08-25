import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


current_dir = os.path.dirname(os.path.abspath(__file__))
IMAGE_SAMPLE = cv2.imread(os.path.join(current_dir, "assets", "img2.png"))


def get_input_image():
    img_name = input("Escreva o nome da sua imagem: ")
    return cv2.imread(os.path.join(current_dir, "User", img_name))

def main():
    try:
        img = get_input_image()
        segment_image(img)
    except Exception as e:
        print("Imagem não encontrada! Usando imagem de teste.")
        segment_image(IMAGE_SAMPLE)
    exit()


def segment_image(image = IMAGE_SAMPLE):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5,5), np.uint8)
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    segmented_image = image.copy()
    cv2.drawContours(segmented_image, contours, -1, (0,255,0), 3)

    plt.figure(figsize=(10, 10))
    plt.subplot(1, 3, 1)
    plt.title('Imagem Original')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.subplot(1, 3, 2)
    plt.title('Imagem Binária')
    plt.imshow(binary, cmap='gray')

    plt.subplot(1, 3, 3)
    plt.title('Imagem Segmentada')
    plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))

    plt.show()


if __name__ == '__main__':
    main()
