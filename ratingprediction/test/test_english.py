'''
Created on Apr 22, 2012

@author: bhatt
'''
from ratingprediction.util.readexcel import FileUtil
from ratingprediction.util.statistics import Statistics
import numpy
import unittest



class Test(unittest.TestCase):


    def testComputeNDBucketEnglish1(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,15])
        print "-------------------ENGLISH 1--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        print "-----------------------------------------------------"
        pass
    
    def testComputeNDBucketEnglish2(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,16])
        print "-------------------ENGLISH 2--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        print "-----------------------------------------------------"
        pass
    
    def testComputeNDBucketEnglish3(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,17])
        print "-------------------ENGLISH 3--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        print "-----------------------------------------------------"
        pass
    
    def testComputeNDBucketEnglish4(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,18])
        print "-------------------ENGLISH 4--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        print "-----------------------------------------------------"
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testComputeNDBucket']
    unittest.main()