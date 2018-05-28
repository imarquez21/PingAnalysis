import numpy as np
import matplotlib.pyplot as plt
import sys
import os

def compute_CDF(RTTs_array):
    xvals = np.sort(RTTs_array)
    yvals = np.arange(len(xvals)) / float(len(xvals) - 1)

    return xvals,yvals


samples_path = "./SampleFiles/"

print "Computing CDFs for samples located in "+samples_path+" folder."

NUM_COLORS=0

for existing_file in sorted(os.listdir(samples_path)):
    NUM_COLORS+=1

figs_path = "./Figures/"
cm = plt.get_cmap('gist_rainbow')
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])

cont = 0
for existing_file in sorted(os.listdir(samples_path)):
    sample_file = os.path.join(samples_path,existing_file)
    sample = np.loadtxt(sample_file, dtype=float, usecols=0)

    print "Computing CDF for file: "+existing_file
    sample_x, sample_y = compute_CDF(sample)
    
    print "Generating Plots"
    ax.plot(sample_x,sample_y, label=existing_file)
    print "\n"
    cont+=1

plt.title("CDFs Plot")
plt.xlabel("RTTs (msec)")
plt.ylabel("F(x)")
plt.grid()
plt.legend(loc='lower right')
print "Saving plots in "+figs_path+" folder."
plt.savefig(figs_path+"03.CDFs.png", dpi=300)
plt.show()
plt.close()

print "End of Script."


