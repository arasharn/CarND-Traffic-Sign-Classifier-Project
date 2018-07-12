# %% Loading data
new_signs = []
new_signs.append(\
"/Users/Arash/GitHub/CarND-Traffic-Sign-Classifier-Project/yield13.jpg"\
)
new_signs.append(\
"/Users/Arash/GitHub/CarND-Traffic-Sign-Classifier-Project/stop14.png"\
)
new_signs.append(\
"/Users/Arash/GitHub/CarND-Traffic-Sign-Classifier-Project/slipperyrd23.png"\
)
new_signs.append(\
"/Users/Arash/GitHub/CarND-Traffic-Sign-Classifier-Project/Priorityroad12.jpg"\
)
new_signs.append(\
 "/Users/Arash/GitHub/CarND-Traffic-Sign-Classifier-Project/nopassing9.jpg"\
)

import numpy as np
y_sign = np.array( [ 13, 25, 14, 11, 12 ] )

# %% Resizing new images
import cv2
import matplotlib.pylab as plt
tst_sgns = []
for i in new_signs:
    img = cv2.imread( i )
    img_re = cv2.resize( img, ( 32, 32 ) )
    img_re = cv2.cvtColor( img_re, cv2.COLOR_BGR2RGB )
    img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
    tst_sgns.append( img_re )
    '''plt.figure()
    plt.subplot(2,1,1)
    plt.imshow( img )
    plt.subplot(2,1,2)
    plt.imshow( img_re )
    plt.show()'''

# %% Functions fro Pre-processing
def rgb2gry(x):
    x_gray=cv2.cvtColor(x, cv2.COLOR_RGB2GRAY)
    x_gray=np.reshape(x_gray, (32, 32, 1))
    return(x_gray)
    
def normalize(x):
    x_norm = x / 128 - 1
    return x_norm
    
# %% Pre-Processing new images
tst_sgns = [rgb2gry(x) for x in tst_sgns]

for i in range(0,5):
    print(i)
    plt.figure(figsize=(13,8))
    plt.imshow(np.squeeze(tst_sgns[i]),cmap='gray')
    plt.show()

tst_sgns = [normalize(x) for x in tst_sgns]

for i in range(0,5):
    print(i)
    plt.figure(figsize=(13,8))
    plt.imshow(np.squeeze(tst_sgns[i]),cmap='gray')
    plt.show()
    

    
