#reads given file
import xlrd

class FileUtil:
    
    def readFile(self,filename):
        workbook = xlrd.open_workbook(filename)
        data = [];
        sheet = workbook.sheet_by_index(0)
        line = [];
        'save all this data in a 2 dimensional structure'
        
        for row in range(sheet.nrows):
            line = []
            for col in range(sheet.ncols):
                line.append(sheet.cell(row,col).value)
            data.append(line);
                #print sheet.cell(row, col).value;
            
        return data
    
    
    
