'''
Created on Apr 23, 2012

@author: bhatt
'''
from ratingprediction.util.readexcel import FileUtil
from ratingprediction.util.statistics import Statistics
import numpy


class Main(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def computeFullDataGrades(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        rmat = numpy.zeros((len(mat),18))
        
        
        tuple = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        gradingCritera = []
        gradingTuple = [0,1,2,3] #we can fit 5 values in this range
        for i in range(0,4):
            gradingCritera.insert(i, tuple)
            #for j in range(0,18):
                #gradingCritera[i].insert(j)
      
        #fetch all the values from data
        for i in range(0,18):
            bucket = statistics.computeNDBuckets(mat[:,self.atMap(i)])
            for j in range(0,3):
                gradingCritera[j][i] = max(bucket[j]) 
        
        for i in range(rmat.shape[0]):
            for j in range(rmat.shape[1]):
                print "i:" + str(i) + " j:" + str(j)
                if (mat[i][self.atMap(i)]>=gradingCritera[3][j]):
                    rmat[i][j] = 4
                elif (mat[i][self.atMap(i)]>=gradingCritera[3][j]):
                    rmat[i][j] = 3
                elif (mat[i][self.atMap(i)]>=gradingCritera[3][j]):
                    rmat[i][j] = 2
                elif (mat[i][self.atMap(i)]>=gradingCritera[3][j]):
                    rmat[i][j] = 1
                else:
                    rmat[i][j] = 0
        
        print 'x'
        
    def attributes(self, x):
        return {
            'tenth' : 7,
            'twelveth' : 8,
            'college' : 13, 
            'eng1' : 15, 
            'eng2' : 16, 
            'eng3' : 17, 
            'eng4' : 18,
            'qa1' : 19, 
            'qa2' : 20, 
            'qa3' : 21, 
            'qa4' : 22, 
            'dom1' : 23, 
            'dom2' : 24, 
            'dom3' : 25, 
            'dom4' : 26,
            'as1' : 27, 
            'as2' : 28, 
            'as3' : 29,
            'rating': 30    
            }.get(x,1)
            
    def atMap(self, x):
        return {
            0 : 7,
            1 : 8,
            2 : 13, 
            3 : 15, 
            4 : 16, 
            5 : 17, 
            6 : 18,
            7 : 19, 
            8 : 20, 
            9 : 21, 
            10 : 22, 
            11 : 23, 
            12 : 24, 
            13 : 25, 
            14 : 26,
            15 : 27, 
            16 : 28, 
            17 : 29,
            18: 30    
            }.get(x,1)
        