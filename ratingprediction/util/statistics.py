'''
Created on Apr 15, 2012

@author: bhatt
'''
import math
import decimal
from decimal import InvalidOperation

class Statistics(object):
    '''
    classdocs
    '''
    def computeGenderBucket(self, data):
        line = []
        genderRating = []
        genderRating.insert(0, [0,0,0])
        genderRating.insert(1, [0,0,0])
        
        for idx,row in enumerate(data):
            line = row
            for idy, col in enumerate(line):
                if idy == 5:
                    #print data[idx][idy]
                    #if this col val is A select 0 else 1
                    rating = data[idx][30]
                    if col == 'A':
                       
                        if rating == 'MP':
                            genderRating[0][0] = genderRating[0][0] + 1
                        elif rating == 'BP':
                            genderRating[0][1] = genderRating[0][1] + 1
                        elif rating == 'LP':
                            genderRating[0][2] = genderRating[0][2] + 1
                   
                    elif col == 'B':
                        if rating == 'MP':
                            genderRating[1][0] = genderRating[1][0] + 1
                        elif rating == 'BP':
                            genderRating[1][1] = genderRating[1][1] + 1
                        elif rating == 'LP':
                            genderRating[1][2] = genderRating[1][2] + 1
                        
                    #print col

        return genderRating
    
    
    'computes standard deviation for given column vector'
    
    def computeSD(self, data):
        result = []
        total = 0
        for idx,val in enumerate(data):
            total = total + math.floor(decimal.Decimal(val))
            
        expectation = total / len(data)
        
        #computing sd
        for idx, val in enumerate(data):
            result.append(math.sqrt((math.floor(decimal.Decimal(val)) - expectation)**2))
        
        return result
    
    
    def computeNormalDistribution(self,data):
        result = []
        total = 0
        for idx,val in enumerate(data):
            total = total + math.floor(decimal.Decimal(val))
          
        expectation = total / len(data)  
        deviation = 0
         
        #computing sd
        for idx, val in enumerate(data):
            deviation = deviation + math.sqrt((math.floor(decimal.Decimal(val)) - expectation)**2)
        
        deviation = deviation / (len(data) - 1)
        deviation = math.sqrt(deviation)
        
        for val in data:
            result.append((1/(deviation * math.sqrt( 2 * math.pi ))) * math.e**((-(float(decimal.Decimal(val))-expectation)**2)/(2*deviation**2)))
        
        
        return result
    
    'Returns result in a bucket of 3. bucket[0] = mean-SD<-1, bucket[1] = |mean-SD| < 1 and bucket[2] = |mean-SD| > 1'
    def computeNDBuckets(self, data):
        result = [0,1,2,3,4]
        #initializing 
        result[0]=[]
        result[1]=[]
        result[2]=[]
        result[3]=[]
        result[4]=[]
        
        total = 0
        for idx,val in enumerate(data):
            try:
                total = total + math.floor(decimal.Decimal(val))
            except InvalidOperation, ex:
                print val + " encountered when numeric expected during mean calculation"
        expectation = total / len(data)  
        deviation = 0
        
         
        #computing sd
        for val in data:
            try:
                deviation = deviation + math.sqrt((math.floor(decimal.Decimal(val)) - expectation)**2)
            except InvalidOperation, ex:
                print val + " encountered when numeric expected during deviation calculation"
        deviation = deviation / (len(data) - 1)
        deviation = math.sqrt(deviation)
        
        for val in data:
            try:
                x = decimal.Decimal(val)
            except InvalidOperation, ex:
                print val + " creating buckets. assigned mean value"
            if(x < (expectation - 2*deviation)):
                result[0].append(val)
            elif(x < (expectation - deviation)):
                result[1].append(val)
            elif(x > (expectation + 2*deviation)):
                result[4].append(val)
            elif(x > (expectation + deviation)):
                result[3].append(val)
            else:
                result[2].append(val)    
        
        return result
    
    'Returns results sliced by output buckets'
    def computeNDBucketsWrtPrediction(self, data, mat):
        result = [0,1,2,3,4]
        outputBucket = []
        outputBucket.insert(0, [0,1,2,3,4]) #low performer
        outputBucket.insert(1, [0,1,2,3,4]) #mid performer
        outputBucket.insert(2, [0,1,2,3,4]) #best performer
        #initializing 
        for i in [0,1,2]:
            for k in [0,1,2,3,4]:
                outputBucket[i][k] = []
                
        result[0]=[]
        result[1]=[]
        result[2]=[]
        result[3]=[]
        result[4]=[]
        
        total = 0
        for idx,val in enumerate(data):
            try:
                total = total + math.floor(decimal.Decimal(val))
            except InvalidOperation, ex:
                print val + " encountered when numeric expected during mean calculation"
        expectation = total / len(data)  
        deviation = 0
        
         
        #computing sd
        for val in data:
            try:
                deviation = deviation + math.sqrt((math.floor(decimal.Decimal(val)) - expectation)**2)
            except InvalidOperation, ex:
                print val + " encountered when numeric expected during deviation calculation"
        deviation = deviation / (len(data) - 1)
        deviation = math.sqrt(deviation)
        
        for idx,val in enumerate(data):
            
            perf = self.performer(mat[idx])
            
            
            try:
                x = decimal.Decimal(val)
            except InvalidOperation, ex:
                print val + " creating buckets. assigned mean value"
            if(x < (expectation - 2*deviation)):
                outputBucket[perf][0].append(val)
            elif(x < (expectation - deviation)):
                outputBucket[perf][1].append(val)
            elif(x > (expectation + 2*deviation)):
                outputBucket[perf][4].append(val)
            elif(x > (expectation + deviation)):
                outputBucket[perf][3].append(val)
            else:
                outputBucket[perf][2].append(val)    
        
        return outputBucket
        
    
    
    def computeNameLengthBucket(self,data):
        result = [0,0,0]
        average = [0,0,0]
        count = [0,0,0]
        
        for idx,val in enumerate(data[:,30]):
            x = decimal.Decimal(data[idx,2])
            if val == 'MP':
                result[0] = result[0] + x
                count [0] = count[0] + 1
            elif val == 'BP':
                result[1] = result[1] + x
                count[1] = count[1] + 1;
            else:
                result[2] = result[2] + x
                count[2] = count[2] + 1
                
        for idx,val in enumerate(result):
            average[idx] = val / count[idx]        
        return average
    
    def performer(self,x):
        return {
            'LP' : 0,
            'MP' : 1,
            'BP' : 2,    
            }.get(x,1)
        