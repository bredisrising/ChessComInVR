
from PIL.Image import new
import numpy as np
import matplotlib.pyplot as plt
import cv2, os, random, pickle
#plt.style.use('fivethirtyeight')

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

IMG_SIZE = 50
DATADIR = "../ChessComConnection/PieceDataSet"
CATEGORIES = ["BlackPawn",
            'BlackQueen',
            'BlackKing',
            'BlackBishop',
            'BlackKnight',
            'BlackRook',
            'WhitePawn',
            'WhiteQueen',
            'WhiteKing',
            'WhiteBishop',
            'WhiteKnight',
            'WhiteRook']


training_data = []

def createTrainingData():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in listdir_nohidden(path):
            imgArray = cv2.imread(os.path.join(path,img), cv2.IMREAD_UNCHANGED)
            newArray = cv2.resize(imgArray, (IMG_SIZE, IMG_SIZE))
            training_data.append([newArray, class_num])


createTrainingData()
print(len(training_data))

random.shuffle(training_data)

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
#y = np.array(y).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

print(len(X))
print(X)
print(len(y))

pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()




