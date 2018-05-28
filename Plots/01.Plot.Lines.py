import matplotlib.pyplot as plt
import numpy as np
import sys

source_file = sys.argv[1]

figures_folder = "./Figures/"

RTT = np.loadtxt(source_file, dtype=np.float_)


lines = plt.figure(1)
plt.xlabel('Ping Number')
plt.ylabel('RTT (msec)')
plt.title('RTT for Pings: '+source_file)
plt.plot(RTT, label='RTT')
plt.grid()
plt.legend()
print "Saving plot in "+figures_folder+" folder."
lines.savefig(figures_folder+"01."+source_file+'_Lines.png', bbox_inches=None,dpi = 300)
#plt.show()
plt.close()

