
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

fig = plt.gcf()
fig.set_size_inches(8, 5)
plt.figure(dpi=300)

# data to plot
n_groups = 3
means_frank = (42113, 48537, 50130)
means_guido = (13885, 20309, 21903)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.3
opacity = 1

rects1 = plt.bar(index, means_frank, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Total')

rects2 = plt.bar(index + bar_width, means_guido, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Error')

plt.xlabel('Number of threads')
plt.ylabel('Number of transactions')
plt.title('Errors in Transactions - 60 secs')
plt.xticks(index + bar_width, ('3T', '6T', '9T'))
plt.legend()

plt.tight_layout()
# plt.show()
plt.savefig("/Users/zebakhalil/Desktop/error_per_transaction.png",dpi=500)