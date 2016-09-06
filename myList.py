// Little script to list the top-level directory contents of its containing directory in an html file displayed in a browser.

import os
import webbrowser

open("htmlDoc", "w").close() 

htmlFile = open("htmlDoc","w")

htmlFile.write("""<!DOCTYPE html>
<html>
<body>
<h1> Top Level Directory Contents </h1>""");

for name in os.listdir(os.getcwd()):
	htmlFile.write('<br>' + name + '</br>' + '\n')

htmlFile.write("""</body>
</html>""")

htmlFile.close()

webbrowser.open('file://' + os.path.realpath("htmlDoc"))
