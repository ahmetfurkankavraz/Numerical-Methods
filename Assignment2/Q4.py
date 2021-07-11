# Ahmet Furkan Kavraz
# 150190024
# This contains only the code of the program.
# For the result of part-b please look pdf.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('clown.bmp', 0)

# decomposition of the image
U, S, V = np.linalg.svd(img)
# for a better matrix multipilication
S = np.diag(S)

# priting the size of original matrix
print("Original image ", "shapes of (U,S,V): ", U.shape, S.shape, V.shape)

# creating the output image table 
fig = plt.figure()
rows = 3
cols = 2

# the initial rank value
r = 2
i = 0
while r != 128:
    # applying truncation
    img_r = np.matmul(U[:,:r], S[:r,:r])
    img_r = np.matmul(img_r, V[:r,:])
    
    # printing the needed storage value
    print("Rank =", r ,"image ", "shapes of (U,S,V): ", U[:,:r].shape, S[:r,:r].shape, V[:r,:].shape)

    # some operations for priting image
    fig.add_subplot(rows, cols, i+1)
    plt.imshow(img_r, cmap = "gray")
    plt.axis('off')
    plt.title("Truncated with "+ str(r))
    
    # updating the values
    r *= 2
    i+=1

# output of the image
plt.show()
plt.close()

