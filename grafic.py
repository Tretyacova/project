import matplotlib.pyplot as plt

potato_price = [25.8, 41.2, 41.1, 40.4]
salat_price = [34.1, 33.7, 33.7, 35.6]
onion_price = [51.1, 50.6, 51.7, 52.9]
honey_price = [956.6, 997.7, 975, 996]
garlic_price = [293.2, 296.5, 305.7, 311.6]
apples_price = [81.1, 83.2, 83.9, 90.1]
total = ["на 2.11", "на 10.11", "на 14.11", "на 24,11"]

plt.plot(total, potato_price, label = "Картопля")
plt.plot(total, salat_price, label = "Капуста")
plt.plot(total, onion_price, label = "Цибуля")
plt.plot(total, honey_price, label = "Мед")
plt.plot(total, garlic_price, label = "Часник")
plt.plot(total, apples_price, label = "Яблука")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)

def showplot():
    plt.show()