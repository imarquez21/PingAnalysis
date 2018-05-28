import numpy as np
import re
import sys
import os
from datetime import datetime

#Counter to identify in which array do we store the obtained RTT.
cont=0

#file_name = sys.argv[1]
read_path = "./Source/"
save_path = "./Results/Arrays/"

number_of_files = 0
print ("Reading files in './Source/' folder to obtain RRTs.\n")
for data_file in sorted(os.listdir(read_path)):
    number_of_files += 1
    All_Pings = []

    full_file_path = os.path.join(read_path,data_file)
    with open(full_file_path) as f:
        data = f.readlines()

    print ("Processing File "+data_file+".")
    for line in data:
        if "time=" in line:
            RTT = float(re.findall('time=(\d*\.?\d+)',line)[0])
            All_Pings.append(RTT)
        else:
            cont = 0

    #We create a column pair, 1st column is the index, 2nd column the RTT for the ping
    All_Pings_Column = np.column_stack([All_Pings])

    #We save the data files in ./Results/ folder in case they are needed for further processing.
    print "Saving file with stats in folder ./Results/Arrays/\n"

    stats_file = open(save_path+"0"+str(number_of_files)+".RTTs_Stats.dat","w")

    stats_file.write("Stats from File:\t"+data_file+"\n")
    stats_file.write("Min:\t"+str(np.min(All_Pings))+" msec.\n")
    stats_file.write("Max:\t"+str(np.max(All_Pings))+" msec.\n")
    stats_file.write("Avg:\t"+str(np.average(All_Pings))+" msec.\n")
    stats_file.write("Variance:\t"+str(np.var(All_Pings))+" msec.\n")
    stats_file.write("Standard Deviation:\t"+str(np.std(All_Pings))+" msec.\n")

    stats_file.close()

    print "Saving file with plot data in folder ./Results/Arrays/\n"
    np.savetxt(save_path+"0"+str(number_of_files)+".RTTs_Array.dat", All_Pings_Column, ['%f'])

print ("Script end time: "+str(datetime.now())+".\n")
print ("End of the Script.\n")
