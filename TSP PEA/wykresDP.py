import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5,6], [0.000216, 0.001944, 0.001804, 0.907798, 2.689878, 5.742906], 'bo')
plt.plot([1,2,3,4,5,6], [0.000216, 0.001944, 0.001804, 0.907798, 2.689878, 5.742906])

# plt.xlabel('Kolejne Pliki z Miastami[4,6,12,13,14,15]')
plt.xlabel('Ilosc Miast')
plt.ylabel('Czas')
plt.title('Wykres czasu dla kolejnych plikow z miastami DP')
plt.axis([0, 7, 0, 6])
plt.grid(True)
plt.show()