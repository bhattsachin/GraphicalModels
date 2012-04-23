'''
Created on Apr 22, 2012

@author: bhatt
'''
from ratingprediction.util.readexcel import FileUtil
from ratingprediction.util.statistics import Statistics
import numpy
import unittest


class Test(unittest.TestCase):


    
    def testComputeNDBucketQuant1(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,19])
        print "-------------------QUANT 1--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        print "-----------------------------------------------------"
        pass
    
    def testComputeNDBucketQuant2(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,20])
        print "-------------------QUANT 2--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        print "-----------------------------------------------------"
        pass
    
    def testComputeNDBucketQuant3(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,21])
        print "-------------------QUANT 3--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        print "-----------------------------------------------------"
        pass
    
    def testComputeNDBucketQuant4(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,22])
        print "-------------------QUANT 4--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        print "-----------------------------------------------------"
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()