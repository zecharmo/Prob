import collections
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats

test_list = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]


# Objective: output frequencies, create and save a boxplot, a histogram, and a QQ-plot of the data

c = collections.Counter(test_list)

# calculate the number of instances in the list
count_sum = sum(c.values())

# output frequencies
for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

# create a boxplot
plt.boxplot(test_list)

# save boxplot
plt.savefig("boxplot.png")
plt.show()

# create histogram
plt.hist(x, histtype='bar')

# save histogram
plt.savefig("histogram.png")
plt.show()

# create QQ-plot
stats.probplot(test_list, dist="norm", plot=plt)

# save QQ-plot
plt.savefig("qqplot.png")
plt.show()


