import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5,6,7], [0.000217, 0.000326, 0.002838, 0.005955, 0.011058, 0.014741, 0.023051], 'bo')
plt.plot([1,2,3,4,5,6,7], [0.000217, 0.000326, 0.002838, 0.005955, 0.011058, 0.014741, 0.023051])

plt.xlabel('Kolejne Pliki z Miastami[4,6,12,13,14,15,17]')
plt.ylabel('Czas')
plt.title('Wykres czasu dla kolejnych plikow z miastami BB')
plt.axis([0, 8, 0, 0.03])
plt.grid(True)
plt.show()