#!/usr/bin/python

import os
import sys
import subprocess
import commands
import webbrowser

#sys.path.append(os.path.join(os.path.dirname(__file__), "../scripts"))
#sys.path.append(os.path.join(os.path.dirname(__file__), "../testCasesExecutables"))
cur_path = os.path.dirname(__file__)

importListTextFiles = os.listdir('testCases')
importList = os.listdir('testCasesExecutables')
exportFilePath = os.path.join("reports/testReport.txt")
htmlFilePath = os.path.join("reports/testReport.html")
oldstdout = sys.stdout
#print importListTextFiles

#print importList
print "Running tests please wait...\n"
importListTextFiles.sort()
importList.sort()

#print importList

new = 2
htmlArrayData = []
htmlSingleData = []
passed_failed = "Failed"



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


	tempString = "python testCasesExecutables/"+lineList[2]+" "+lineList[4]+" "+lineList[5]
	

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

	if stringOutput.endswith("OK") == True:
		passed = "Passed"

	htmlSingleData.append(lineList[0])
	htmlSingleData.append(lineList[1])
	htmlSingleData.append(lineList[2])
	htmlSingleData.append(lineList[3])
	htmlSingleData.append(lineList[4])
	htmlSingleData.append(lineList[5])
	htmlSingleData.append(passed)
	htmlArrayData.append(htmlSingleData)
	htmlSingleData = []
	passed = "Failed"
	

#os.system("python ../testCasesExecutables/testCaseExecutable1.py blue blue")
#os.system("python ../testCasesExecutables/test_line_color.py 3 5")

#print sys.exc_info()
sys.stdout = oldstdout

print "Tests complete."

output.close()



open(htmlFilePath, 'w').close()

output = open(htmlFilePath, 'w')
sys.stdout = output

print """<html><head></head><body><table border="1">
<th>Test Case</th><th>Description</th><th>File</th><th>Method</th><th>Expected Output</th><th>Input</th><th>Result</th>"""

for i in range(0,len(htmlArrayData)):
	print "<tr>"
	for j in range (0,len(htmlArrayData[i])):
		if htmlArrayData[i][j] == "Failed":
			print """<td bgcolor="#ff0000">"""
			print htmlArrayData[i][j]
			print "</td>"
		if htmlArrayData[i][j] == "Passed":
			print """<td bgcolor="#00ff00">"""
			print htmlArrayData[i][j]
			print "</td>"
		if htmlArrayData[i][j] != "Passed" and htmlArrayData[i][j] != "Failed":
			print "<td>"
			print htmlArrayData[i][j]
			print "</td>"
		
	
	print "</tr>"


print "</table></body></html>"


output.close()

url = htmlFilePath
webbrowser.open(url,new=new)

