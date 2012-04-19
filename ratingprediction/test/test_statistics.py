'''
Created on Apr 15, 2012

@author: bhatt
'''


from ratingprediction.util.readexcel import FileUtil
from ratingprediction.util.statistics import Statistics
import numpy
import unittest


class Test(unittest.TestCase):


    def testComputGenderBucket(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        genderRating = statistics.computeGenderBucket(data)
        
        for i in genderRating:
            print i
        pass
    
    def testComputeSD(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        
        mat = numpy.array(data[2:len(data)]);
        
        marksSD = statistics.computeSD(mat[:,7])
        
        for idx,val in enumerate(mat[:,7]):
            print str(val) + " " + str(marksSD[idx])
        
        
        pass
    
    def testComputeND(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        marksSD = statistics.computeNormalDistribution(mat[:,7])
        
        
        
        for idx,val in enumerate(mat[:,7]):
            print str(val) + " ** " + str(marksSD[idx])
        pass
    
    
    def testComputNameLength(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        
        averages = statistics.computeNameLengthBucket(mat);
        print "----------Average length of names-------------"
        for idx, val in enumerate(averages):
            print str(idx) + " " + str(val)


        pass
    
    
    def testComputeNDBucket(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,7])
        
        
        
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val))
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testComputGenderBucket']
    unittest.main()