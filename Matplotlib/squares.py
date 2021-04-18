import matplotlib.pyplot as plt

n = 6
input_values = [i for i in range(n)]
squares = [i**2 for i in range(n)]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel('Wartość', fontsize=14)
ax.set_ylabel('Kwadraty wartośći', fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()