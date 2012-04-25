'''
Created on Apr 24, 2012

@author: bhatt
'''
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import unittest



class Test(unittest.TestCase):


    def testName(self):
        
        majorLocator = MultipleLocator(20)
        majorFormatter = FormatStrFormatter('%d')
        minorLocator = MultipleLocator(5)


        t = arange(0.0, 100.0, 0.1)
        s = sin(0.1 * pi * t) * exp(-t * 0.01)

        ax = subplot(111)
        plot(t, s)

        ax.xaxis.set_major_locator(majorLocator)
        ax.xaxis.set_major_formatter(majorFormatter)

    #for the minor ticks, use no labels; default NullFormatter
        ax.xaxis.set_minor_locator(minorLocator)

        show()
        
        
        
        
        
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
