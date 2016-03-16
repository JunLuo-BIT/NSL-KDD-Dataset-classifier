import numpy as np
import mlpy

import matplotlib.pyplot as plt

iris = np.loadtxt('iris.csv', delimiter=',')

# print iris

# print iris[:, 4], len(iris[:, 4])

x, y = iris[:, :4], iris[:, 4].astype(np.int)

# print x, y

print x.shape, y.shape

# create a new PCA instant.
pca = mlpy.PCA()

pca.learn(x)

z = pca.transform(x, k=None)

print z

print z.shape

# plot them all
# plt.set_cmap(plt.cm.Paired)
# fig1 = plt.figure(1)
# title = plt.title("PCA on iris dataset")
# plot = plt.scatter(z[:, 0], z[:, 1], c=y)
# labx = plt.xlabel("First component")
# laby = plt.ylabel("Second component")
# plt.show()
