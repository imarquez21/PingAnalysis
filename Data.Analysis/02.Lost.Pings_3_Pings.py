import numpy as np
import re
import pingparsing
import sys
import os
import matplotlib.pyplot as plt
from decimal import Decimal

read_path = "./Source/"
save_path = "./Results/"

Losses_01 = []
Losses_02 = []
Losses_03 = []

headers = []
labels = ['Ping/TCP','1st Ping','2nd Ping','3rd Ping','Received','Sent','Loss%']

sent = []
received = []
loss_rate = []

number_of_files = 0
print ("Reading files in './Source/' folder to obtain RTTs.\n")
for data_file in sorted(os.listdir(read_path)):
    number_of_files += 1
    sent_pings = 0
    received_pings = 0
    lost_pings = 0

    #Arrays to Store the RTT Values and Seq. Numbers. for each ping in the train.
    First_Ping = []
    Second_Ping = []
    Third_Ping = []
    All_RTTs = []
    ICMP_Seq = []

    #Counters for losses
    first_missing = 0
    second_missing = 0
    third_missing = 0

    lost_percentage = 0

    #Counter to identify in which array do we store the RTT obtained.
    RTT = 0
    current_seq_num = 0

    full_file_path = os.path.join(read_path,data_file)
    with open(full_file_path) as f:
        data = f.readlines()

    print "\n=======================================================================\n"
    print ("Processing File: "+data_file+".")
    for line in data:
        if "time=" in line:
            current_seq_num = int(re.findall('icmp_seq=(\d*)',line)[0])
            RTT = float(re.findall('time=(\d*\.?\d+)',line)[0])
            ICMP_Seq.append(current_seq_num)
            All_RTTs.append(RTT)

            if current_seq_num%3 == 1:
                First_Ping.append(RTT)
            if current_seq_num%3 == 2:
                Second_Ping.append(RTT)
            if current_seq_num%3 == 0:
                Third_Ping.append(RTT)

        if "Next Batch" in line:
            sent_pings+=3

    if len(str(number_of_files)) < 2:
        str_num_files = "0"+str(number_of_files)
    else:
        str_num_files = str(number_of_files)

    received_pings = len(First_Ping)+len(Second_Ping)+len(Third_Ping)

    first_missing = (sent_pings/3)-len(First_Ping)
    second_missing = (sent_pings/3)-len(Second_Ping)
    third_missing = (sent_pings/3)-len(Third_Ping)

    total_missing = first_missing + second_missing + third_missing

    lost_percentage = round(((sent_pings-received_pings)/float(sent_pings))*100,2)

    Losses_01.append(first_missing)
    Losses_02.append(second_missing)
    Losses_03.append(third_missing)
    sent.append(sent_pings)
    received.append(received_pings)
    loss_rate.append(lost_percentage)

    headers.append(str_num_files)

losses_array = [headers,Losses_01,Losses_02,Losses_03,received,sent,loss_rate]

data_file = open(save_path+"01.RTT.Losses.dat","w")

label_cont = 0
for array in losses_array:
    data_file.write(labels[label_cont]+"\t")
    for value in array:
        data_file.write(str(value)+"\t")
    data_file.write("\n")
    label_cont+=1

data_file.close()

print ("End of the Script")


