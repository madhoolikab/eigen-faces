import os
import numpy as np
import matplotlib.pyplot as plt

# Read images
path='D:\Sem_1\DIP\yale-face-database\data'
image_paths = [os.path.join(path, f) for f in os.listdir(path)]
images = [plt.imread(image_path, 0) for image_path in image_paths]
A = np.array([face.flatten() for face in images]).T

M, N = images[0].shape
  
mean = A.sum(axis=1)/len(images)
A_mean = np.transpose(np.transpose(A) - mean)

u, s, vh = np.linalg.svd(A_mean, full_matrices=False)

# choosing the top-k principal components, and shaping them as images again
k = 8
u = u[:, :k]
y = np.transpose(u) @ A_mean[:, :k]
z = u @ y
z = np.reshape(z, (M, N, k))

# plotting the top-k eigen faces for the given data
a = 0
fig, axs = plt.subplots(2, int(k/2))
for i in range(2):
    for j in range(k//2):
        axs[i, j].imshow(z[:, :, a], cmap='gray')
        axs[i, j].set_title('EigenFace : % 2d'%(a+1))
        a += 1