from scipy import stats
from scipy.stats import ks_2samp
import numpy as np
from math import sqrt
import os
import sys
import pandas as pd

def check_similarity(alpha, D, p, file_name):
    n = len(data)
    m = len(sample)
    c_alpha = 1.36 #value defined for sizes above 50 for alpha of .05
    inside = float(n+m)/float(n*m)
    critical_value = float(c_alpha)*float(sqrt(inside))
    critical_values.append(critical_value)

    print "Results for sample file: "+file_name

    if D > critical_value:
        print "D: "+str(D)+" is greater than Critical Value: "+str(critical_value)+"."
        print "Null Hypothesis, drawn from same distribution, is rejected at alpha level of: "+str(alpha)
        print "\n"
    else:
        print "D: "+str(D)+" is less than Critical Value: "+str(critical_value)+"."
        print "Null Hypothesis, drawn from same distribution, fails to be rejected at alpha level of: "+str(alpha)
        print "\n"


def save_ks_results(results,file_name,save_path):
    print "Saving file to "+save_path+" folder."
    stats_file = open(save_path+file_name,"w")
    stats_file.write('\tIndex\tD Value\tCritical Value\tP Value\n')
    stats_file.write(str(results))
    stats_file.close()
    np.savetxt(save_path+"KS.Test.Results.dat",results, ['%d','%f','%f','%f'])

    print "Summary of Results."
    print('\tIndex\t   D Value\tCritical Value\tP Value')
    print(results)


print "Loading Data file."
data_file = sys.argv[1]
data = np.loadtxt(data_file, dtype=float, usecols=0)
alpha = .05
read_path = "./SampleFiles/"
save_path = "./Results/"

D_values = []
p_values = []
critical_values = []

print ("Reading sample files in './SampleFiles/' folder to obtain RRTs.\n")
for existing_file in sorted(os.listdir(read_path)):
    sample_file = os.path.join(read_path,existing_file)
    sample = np.loadtxt(sample_file, dtype=float, usecols=0)
    D, p = stats.ks_2samp(data,sample)
    
    check_similarity(alpha,D,p,existing_file)

    D_values.append(D)
    p_values.append(p)

index = np.arange(1, len(D_values)+1)
results = np.column_stack([index,D_values,critical_values,p_values])

save_ks_results(results,"KS.Test.Results.txt",save_path)

print "End of Script"
