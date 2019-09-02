import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib.patches as mpatches

style.use('ggplot')

fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.figure(dpi=300)
x, y = np.loadtxt(
    '/Users/zebakhalil/Desktop/30sec_folder/3threads/3threads_c.csv',
    unpack=True,
    delimiter=',')

plt.plot(x, y,
         color='green', linestyle='-', linewidth=2, marker='o',
         markeredgecolor='green', markerfacecolor='yellow', markersize=2.0, label='Local 3 Threads')

x, y = np.loadtxt(
    '/Users/zebakhalil/Desktop/30sec_torm/3threads/3threads_c.csv',
    unpack=True,
    delimiter=',')

plt.plot(x, y,
         color='green', linestyle='-.', linewidth=3, marker='o',
         markeredgecolor='green', markerfacecolor='yellow', markersize=2.0, label='Torm 3 Threads')

x, y = np.loadtxt(
    '/Users/zebakhalil/Desktop/30sec_folder/6threads/6threads_c.csv',
    unpack=True,
    delimiter=',')

plt.plot(x, y,
         color='orange', linestyle='-', linewidth=2, marker='o',
         markeredgecolor='orange', markerfacecolor='yellow', markersize=2.0, label='Local 6 Threads')

x, y = np.loadtxt(
    '/Users/zebakhalil/Desktop/30sec_torm/6threads/6threads_c.csv',
    unpack=True,
    delimiter=',')

plt.plot(x, y,
         color='orange', linestyle='-.', linewidth=3, marker='o',
         markeredgecolor='orange', markerfacecolor='yellow', markersize=2.0, label='Torm 6 Threads')

x, y = np.loadtxt(
    '/Users/zebakhalil/Desktop/30sec_folder/9threads/9threads_c.csv',
    unpack=True,
    delimiter=',')
plt.plot(x, y,
         color='purple', linestyle='-', linewidth=2, marker='o',
         markeredgecolor='purple', markerfacecolor='yellow', markersize=2.0, label='Local 9 Threads')

x, y = np.loadtxt(
    '/Users/zebakhalil/Desktop/30sec_torm/9threads/9threads_c.csv',
    unpack=True,
    delimiter=',')
plt.plot(x, y,
         color='purple', linestyle='-.', linewidth=3, marker='o',
         markeredgecolor='purple', markerfacecolor='yellow', markersize=2.0, label='Torm 9 Threads')

plt.plot([0.0, 30], [0.0, 1500], linewidth=0.0, markersize=0.0)

plt.legend(bbox_to_anchor=(0.32, 1))
plt.xlabel('Time elapsed in secs')
plt.ylabel('Transactions per secs')
plt.title('Runtime = 30 secs')
# plt.show()
plt.savefig("/Users/zebakhalil/Desktop/30sec_folder/30sec_TPS.png",dpi=300)