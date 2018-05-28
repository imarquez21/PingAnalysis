import numpy as np
import re
import pingparsing
import sys
import os
import matplotlib.pyplot as plt


def compute_stats(RTTs_array,file_name,save_path):
    min_RTT = np.min(RTTs_array)
    max_RTT = np.max(RTTs_array)
    average_RTT = np.average(RTTs_array)
    variance_RTT = np.var(RTTs_array)
    std_dev_RTT = np.std(RTTs_array)

    print "Saving file with stats of "+file_name+" in folder ./Results/Arrays/\n"

    stats_file = open(save_path+file_name+".RTTs_Stats.dat","w")

    stats_file.write("Stats from File:\t"+file_name+"\n")
    stats_file.write("Min:\t"+str(min_RTT)+" msec.\n")
    stats_file.write("Max:\t"+str(max_RTT)+" msec.\n")
    stats_file.write("Avg:\t"+str(average_RTT)+" msec.\n")
    stats_file.write("Variance:\t"+str(variance_RTT)+" msec.\n")
    stats_file.write("Standard Deviation:\t"+str(std_dev_RTT)+" msec.\n")

    RTTs_column = np.column_stack([RTTs_array])

    print "Saving file with plot data of "+file_name+" in folder ./Results/Arrays/\n"
    np.savetxt(save_path+str(file_name)+".RTTs_Array.dat", RTTs_column, ['%f'])

read_path = "./Source/"
save_path = "./Results/Arrays/"
source_file = sys.argv[1]

#Arrays to Store the RRT Values for each ping in the train.
First_Ping = []
Second_Ping = []
Third_Ping = []

#Counter to identify in which array do we store the RTT obtained.
cont =0

print ("Reading File to obtain RRTs")
with open(read_path+source_file) as f:
    data = f.readlines()

print ("Processing File.")
for line in data:
    if "time=" in line:
        cont+=1
        RTT = float(re.findall('time=(\d*\.?\d+)',line)[0])
        if cont == 1:
            First_Ping.append(RTT)
        if cont == 2:
            Second_Ping.append(RTT)
        if cont == 3:
            Third_Ping.append(RTT)
    if ("Batch" in line or "unreachable" in line) and cont==1:
        Second_Ping.append(RTT)
    if ("Batch" in line or "unreachable" in line) and (cont==1 or cont==2):
        Third_Ping.append(RTT)
    if "Batch" in line or "unreachable" in line:
        cont = 0

compute_stats(First_Ping,"01_Ping",save_path)
compute_stats(Second_Ping,"02_Ping",save_path)
compute_stats(Third_Ping,"03_Ping",save_path)


print ("End of the Script")


