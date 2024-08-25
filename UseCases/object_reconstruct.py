import os
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


current_dir = os.path.dirname(os.path.abspath(__file__))
IMAGE_SAMPLE_1 = cv2.imread(os.path.join(current_dir, "assets", "ceb1.jpg"))
IMAGE_SAMPLE_2 = cv2.imread(os.path.join(current_dir, "assets", "ceb2.jpg"))


def get_input_images():
    img_name1 = input("Escreva o nome da sua imagem 1: ")
    img_name2 = input("Escreva o nome da sua imagem 1: ")
    return (cv2.imread(os.path.join(current_dir, "User", img_name1)),
        cv2.imread(os.path.join(current_dir, "User", img_name2)))

def main():
    matplotlib.use('TkAgg')
    try:
        img1, img2 = get_input_images()
        reconstruct(img1, img2)
    except Exception as e:
        print("Imagem não encontrada! Usando imagem de teste.")
        reconstruct(IMAGE_SAMPLE_1, IMAGE_SAMPLE_2)
    exit()


def reconstruct(img1, img2):
    fx = 1244.7577973309199
    fy = 1240.3033413061512
    cx = 283.38906943038273
    cy = 196.9571744688903

    K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])  # Camera intrinsic matrix

    orb = cv2.ORB_create()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    pts1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    pts2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    E, mask = cv2.findEssentialMat(pts1, pts2, K, method=cv2.RANSAC, prob=0.999, threshold=1.0)

    _, R, t, _ = cv2.recoverPose(E, pts1, pts2, K, mask=mask)

    P1 = np.hstack((np.eye(3), np.zeros((3, 1))))
    P2 = np.hstack((R, t))

    P1 = K @ P1
    P2 = K @ P2

    # Triangulate the 3D points
    points_4D = cv2.triangulatePoints(P1, P2, pts1, pts2)
    points_3D = points_4D / points_4D[3]
    points_3D = points_3D[:3, :].T


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(points_3D[:, 0], points_3D[:, 1], points_3D[:, 2], marker='o', s=5, c='r', alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


if __name__ == "__main__":
    main()
