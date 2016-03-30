import dataframe

import mlpy

if __debug__:
    print 'Dataframe contains', len(dataframe.df_data), 'data',
    print 'and contains', len(dataframe.df_target), 'target'

x = dataframe.df_data
y = dataframe.df_target

if __debug__:
    print x.shape, y.shape

# Here we are tyring to reduce the dimensionality by using
# Principal Component Analysis(PCA)
# Create an PCA object.

pca = mlpy.PCA()
print 'PCA component learning from the data'
pca.learn(x)
print 'PCA trained'


# embed x into k=2 dimension subspace.
z = pca.transform(x, k=5)      # z is the reduced array.

print 'After transform, data shape', z.shape
for i in range(5):
    print z[i]