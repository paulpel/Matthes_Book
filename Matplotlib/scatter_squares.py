import matplotlib.pyplot as plt

n = 1000
x_val = [i for i in range(n)]
y_val = [i**2 for i in range(n)]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Blues, s=10)

ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel('Wartość', fontsize=14)
ax.set_ylabel('Kwadraty wartośći', fontsize=14)

ax.axis([0, n+100, 0, n**2+n*100])

plt.show()