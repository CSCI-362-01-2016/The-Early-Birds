#!/usr/bin/python

import os
import sys
import subprocess
import commands

#sys.path.append(os.path.join(os.path.dirname(__file__), "../scripts"))
#sys.path.append(os.path.join(os.path.dirname(__file__), "../testCasesExecutables"))
cur_path = os.path.dirname(__file__)

importListTextFiles = os.listdir('testCases')
importList = os.listdir('testCasesExecutables')
exportFilePath = os.path.join("reports/testReport.txt")
oldstdout = sys.stdout
#print importListTextFiles

#print importList
print "Running tests please wait...\n"
importListTextFiles.sort()
importList.sort()

#print importList

open(exportFilePath, 'w').close()

output = open(exportFilePath, 'w')
sys.stdout = output



for i in range(0,len(importList)):
	new_path = ('testCases/'+importListTextFiles[i])
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
	tempString = "python testCasesExecutables/"+importList[i]+" "+lineList[4]+" "+lineList[5]
	

	print tempString + "\n"	
	print "Method being tested: "+ lineList[3] +"\n"
	#print "python ../testCasesExecutables/testCaseExecutable1.py blue blue"
	#os.system(tempString)
	#subprocess.Popen([exportFilePath], stdout=subprocess.PIPE)
	#p = subprocess.Popen(tempString, stdout=subprocess.PIPE)
	#out = p.stdout.read()
	#print out
	cmdoutput =  commands.getstatusoutput(tempString) 
	stringOutput = cmdoutput[1].replace("\n", " ")
	#stringOutput = cmdoutput
	print stringOutput
	

#os.system("python ../testCasesExecutables/testCaseExecutable1.py blue blue")
#os.system("python ../testCasesExecutables/test_line_color.py 3 5")

#print sys.exc_info()
sys.stdout = oldstdout

print "Tests complete."

output.close()
