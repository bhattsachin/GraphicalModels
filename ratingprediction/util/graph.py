'''
Created on Apr 24, 2012

@author: bhatt
'''
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from numpy.core.numeric import zeros
from pylab import *


class Graph(object):
    '''
    classdocs
    '''
    def plotAverage(self, data):
        
        averageTuple = zeros((3,19))
        total = zeros((3,1))
        
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                averageTuple[data[i][18]] = averageTuple[data[i][18]] + data[i]
                total[data[i][18]] = total[data[i][18]] + 1
                
        for i in range(3):
            averageTuple[i] =  averageTuple[i] / total[i]
            
        ax = subplot(111)
        plot(range(19), averageTuple[0])
        plot(range(19), averageTuple[1])
        plot(range(19), averageTuple[2])

        show()
        
            
        print 'x'
        

    def __init__(self):
        '''
        Constructor
        '''
        