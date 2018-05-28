import numpy as np
import matplotlib.pyplot as plt
import sys
import os

def compute_ecdf(data):
    cdfx = np.sort(np.unique(data))
    x_values = np.linspace(start=min(cdfx),stop=max(cdfx), num=len(cdfx))
    size_data = data.size
    y_values = []
    for i in x_values:
        temp = data[data<=i]
        val = temp.size / float(size_data)
        y_values.append(val)
    
    return x_values, y_values

def plot_ECDF(data_x,data_y,sample_x,sample_y, label_data, label_sample):
    figs_path = "./Figures/"
    fig1 = plt.figure(1)
    plt.plot(data_x,data_y, marker='.', linestyle='none', label=label_data)
    plt.plot(sample_x,sample_y, marker='.', linestyle='none', label=label_sample)
    plt.title("ECDF - All RTTs vs Sample")
    plt.xlabel("RTTs (msec)")
    plt.ylabel("F(x)")
    plt.grid()
    plt.legend(loc='lower right')
    #plt.show()
    print "Saving plots in "+figs_path+" folder."
    plt.savefig(figs_path+"05."+label_data+label_sample+"_ECDF_Comparisson.png", dpi=300)
    plt.close()

print "Loading Files"
data_file = sys.argv[1]

samples_path = "./SampleFiles/"

data = np.loadtxt(data_file, dtype=float, usecols=0)
print "Computing ECDF for Data."
data_x, data_y = compute_ecdf(data)

print "Computing ECDFs for samples located in "+samples_path+" folder."

for existing_file in sorted(os.listdir(samples_path)):
    sample_file = os.path.join(samples_path,existing_file)
    sample = np.loadtxt(sample_file, dtype=float, usecols=0)

    print "Computing ECDF for sample file: "+data_file
    sample_x, sample_y = compute_ecdf(sample)
    
    print "Generating Plots - Data vs. Sample File: "+sample_file
    plot_ECDF(data_x,data_y,sample_x,sample_y,data_file,existing_file)

    print "\n"

print "End of Script."


