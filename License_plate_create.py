import cv2
import sys
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline
from torch.utils.data import DataLoader
device = 'cuda' if torch.cuda.is_available() else 'cpu'

ads = ['A', 'B', 'C', 'D', 'E']
CHARS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', '-']

for x in range(10000):
    image = np.ones([40,150,3], dtype=np.uint8)
    imgh,imgw,_ = image.shape
    image[:,:] = [250, 250, 0] #blue
    
    alphabets = np.random.randint(4)
    letter1 =ads[alphabets]
    alphabets = np.random.randint(4)
    letter2 =ads[alphabets]
    alphabets = np.random.randint(4)
    letter3 =ads[alphabets]

    letter4 = np.random.randint(9)
    letter5 = np.random.randint(9)
    letter6 = np.random.randint(9)
    letter7 = np.random.randint(9)

    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (10, 28)
    fontScale = 0.8
    # Blue color in BGR
    color = (0,0,0)
    # Line thickness of 2 px
    thickness = 2  
    # print(provinces[int(0)])
    List = [letter1,letter2,letter3,'-',str(letter4),str(letter5),str(letter6),str(letter7)]
    numberplate = open(f'/home/ubuntu/data/datasets/license_plate/labels/train/{letter1}{letter2}{letter3}-{letter4}{letter5}{letter6}{letter7}.txt', "w")

    image = cv2.putText(image, f'{letter1}{letter2}{letter3}-{letter4}{letter5}{letter6}{letter7}', org, font, 
                       fontScale, color, thickness, cv2.LINE_AA)
    
    cv2.imwrite(f'/home/ubuntu/data/datasets/license_plate/images/train/{letter1}{letter2}{letter3}-{letter4}{letter5}{letter6}{letter7}.jpg',image[:,:,::-1])
    
    p=0
    for i in range(8):
        l=10+p #x
        r=5 #y
        xx=27+p
        yy=35

        # img2 = cv2.rectangle(image, (l, r), (xx, yy), (0, 255, 0), 1)

        clz = CHARS.index(List[i])

        x= (l+(xx-l)/2)/imgw
        y= (r+(yy-r)/2)/imgh
        w= (xx-l)/imgw
        h= (yy-r)/imgh

        numberplate.writelines(f'{clz} {x} {y} {w} {h}')
        numberplate.writelines('\n')
        p+=17

    numberplate.close()
    
    
    
print('completed.....')
    