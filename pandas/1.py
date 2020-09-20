import seaborn

planets = seaborn.load_dataset('planets')
print(planets.head(n=3))
print(planets.mean())
print(planets.describe())













































# import pandas as pd
# import numpy as np
#
#
# area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'lllinois': 149995}
# area = pd.Series(area_dict)
#
# population_dict = {'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida': 19552860,
#                    'lllinois': 12882135}
# population = pd.Series(population_dict)
#
# demo = pd.DataFrame({'population' : population, 'area' : area})
# demo['density'] = demo['population'] / demo['area']
#
# demo.loc[demo.density>100, ['density']] = 10
# # print(demo)
#
# A = pd.DataFrame([{'A' : 17, 'B' : 3}, {'A' : 17, 'B' : 11}])
# B = pd.DataFrame([{'B' : 0, 'A' : 1, 'C' : 2}, {'B' : 5, 'A' : 8, 'C' : 7}, {'B' : 3, 'A' : 0, 'C' : 3}])
# print(A)
# print(A-2)
# print(A-np.array([2, 3]))
# print(A-A.iloc[0])
# print(A+B)
# print(A/B)

# print(demo.iloc[:3, :2])
#
# print(demo)

# print(demo['area']
# print(pd.DataFrame([{'a' : 1, 'b' : 2}, {'b' : 3, 'c' : 4}]))
# print(pd.DataFrame(population, columns={'population'}))

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print(data[['b', 'c']])
# print(data['b':'d'])
#
# print(data)

# states = pd.DataFrame({'population': population, 'area': area})
# print(states)
#
# sample1 = pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'], index=['a', 'b', 'c'])
# print(sample1)
#
# sample2 = pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])




