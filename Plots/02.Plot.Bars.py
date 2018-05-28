import matplotlib.pyplot as plt
import numpy as np
import sys

data_file = sys.argv[1]

RTTs = np.loadtxt(data_file, dtype=np.float_)

plt.bar(RTTs)
plt.xlabel('Ping Number', fontsize=10)
plt.ylabel('RTT (msec)', fontsize=10)
#plt.xticks(index, label, fontsize=10, rotation=30)
plt.title('Minimu RTT')
plt.savefig('Min_RTT.png', bbox_inches=None)

#plt.show()
