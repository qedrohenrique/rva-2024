import pickle


with open('cameraMatrix.pkl', 'rb') as f:
    data = pickle.load(f)
    fx = data[0][0]
    fy = data[1][1]
    cx = data[0][2]
    cy = data[1][2]

print(fx, fy, cx, cy)
