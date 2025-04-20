iris_setosa = iris.loc[iris['variety'] == 'setosa']
iris_versicolor = iris.loc[iris['variety'] == 'versicolor']
iris_virginica = iris.loc[iris['variety'] == 'virginica']

plt.plot(iris_setosa['petal.length'], np.zeros_like(iris_setosa['petal.length']), 'o', label='setosa')
plt.plot(iris_virginica['petal.length'], np.zeros_like(iris_virginica['petal.length']), 'o', label='virginica')
plt.plot(iris_versicolor['petal.length'], np.zeros_like(iris_versicolor['petal.length']), 'o', label='versicolor')
plt.xlabel('petal.length')
plt.grid()
plt.legend()
plt.show()