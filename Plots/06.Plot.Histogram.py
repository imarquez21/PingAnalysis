import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import sys

#data_files_folder = "./Source/"
#source_file = sys.argv[1]
#file_name = data_files_folder+source_file
file_name = sys.argv[1]

figures_folder = "./Figures/"

RTT = np.loadtxt(file_name, dtype=np.float_, usecols=0)

def bins_labels(bins, **kwargs):
    bin_w = (max(bins) - min(bins)) / (len(bins) - 1)
    plt.xticks(np.arange(min(bins)+bin_w/2, max(bins), bin_w), bins, **kwargs)
    plt.xlim(bins[0], bins[-1])

bins = range(52)

#Histogram
histrogram = plt.figure(1)
plt.hist(RTT, align='left', log=True)
plt.title("RTT Histogram "+file_name)
plt.xlabel("RTT (msec)")
plt.ylabel("Number of Events")
print "Saving Histogram plot in 'Figures' folder."
#bins_labels(bins, fontsize = 5)
histrogram.savefig(figures_folder+'06.'+file_name+'.Histogram.png',dpi = 300)
plt.close()


fig, ax = plt.subplots(1,1)
ax.hist(RTT, bins=bins, align='left', log=True)
ax.set_xticks(bins[:-1])
plt.title("RTT Histogram "+file_name)
plt.xlabel("RTT (msec)")
plt.ylabel("Number of Events")
plt.savefig(figures_folder+'06.'+file_name+'.Histogram2.png',dpi = 300)
plt.close()

print "End of Script"
