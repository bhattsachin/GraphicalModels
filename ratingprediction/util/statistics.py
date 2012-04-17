'''
Created on Apr 15, 2012

@author: bhatt
'''
import math
import decimal

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