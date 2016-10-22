import os
import sys

#sys.path.append(os.path.join(os.path.dirname(__file__), "../scripts"))
#sys.path.append(os.path.join(os.path.dirname(__file__), "../testCasesExecutables"))
cur_path = os.path.dirname(__file__)

importListTextFiles = os.listdir('../testCases')
importList = os.listdir('../testCasesExecutables')

print importListTextFiles

print importList

importListTextFiles.sort()
importList.sort()

print importList



for i in range(0,len(importList)):
	new_path = os.path.relpath('../testCases/'+importListTextFiles[i], cur_path)
	#tempPath = '../testCasesExecutables/'+importListTextFiles[i]
	f = open(new_path,'r')
	#lineList = list()
	#count = 0
	lineList = f.read().splitlines() 
	#for line in f:
		#lineList.append(line)
		#print line
		#print count
		#count = count + 1
		
	#print "blue\n 5"
	#print lineList[5]+" "+str(len(lineList[5]))
	tempString = "python ../testCasesExecutables/"+importList[i]+" "+lineList[4]+" "+lineList[5]
	print tempString	
	#print "python ../testCasesExecutables/testCaseExecutable1.py blue blue"
	os.system(tempString)
	

#os.system("python ../testCasesExecutables/testCaseExecutable1.py blue blue")
#os.system("python ../testCasesExecutables/test_line_color.py 3 5")

#print sys.exc_info()
