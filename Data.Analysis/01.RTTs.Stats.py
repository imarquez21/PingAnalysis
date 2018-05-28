import numpy as np
import matplotlib.pyplot as plt
import os
from decimal import Decimal

samples_path = "./SampleFiles/"
save_path = "./Results/"

cont = 0

mins = []
avgs = []
maxs = []
variances = []
stds = []

labels = ["Min","Avg","Max","Var","Mdev"]

print "Reading files from "+samples_path+" folder."
for existing_file in sorted(os.listdir(samples_path)):
    sample_file = os.path.join(samples_path,existing_file)
    sample = np.loadtxt(sample_file, dtype=float, usecols=0)

    mins.append(np.min(sample))
    avgs.append(round(np.average(sample),2))
    maxs.append(round(np.max(sample),2))
    variances.append(round(np.var(sample),2))
    stds.append(round(np.std(sample),2))

print "Saving file to "+save_path+" folder."

stats_array = [mins,avgs,maxs,variances,stds]

data_file = open(save_path+"01.RTTs.Stats.dat","w")

cont = 0
for array in stats_array:
    data_file.write(labels[cont]+"\t")
    for value in array:
        data_file.write(str(value)+"\t")
    data_file.write("\n")
    cont+=1

data_file.close()

print "End of Script"
