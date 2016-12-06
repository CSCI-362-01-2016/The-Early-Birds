# The-Early-Birds

Hardware and software requirements

While the testing will be done in the Ubuntu 16.04 LTS operating system, any system should be able to run the tests with the following software installed:

    Python 2.7, 3.4, or 3.5
    Programming language used by matplotlib.
    
    numpy 1.6 or later
    Array support for python.
    
    setuptools
    Provides extensions for python package installation.
    
    dateutil 1.1 or later
    Provides extensions to python datetime handling.
    
    pyparsing
    Required for matplotlib's mathtext math rendering support.
    
    libpng 1.2 or later
    Library for loading and saving PNG files.
    
    pytz
    Used to manipulate time-zone aware datetimes.
    
    freetype 2.3 or later
    Library for reading true type font files.
    
    cycler 0.9 or later
    Composable cycle class used for constructin style-cycles.
    



To install Matplotlib run: "sudo apt-get install python-matplotlib"

Next download a zip of it from https://github.com/matplotlib/matplotlib

Then extract it and inside run "sudo python setup.py build"

This will alert you if you are missing any dependencies. If not it will build just fine.

Then run "sudo python setup.py install"

Then return to the TestAutomation folder and do "./scripts/runAllTest.py" (you may have to do the command below)

**In order to make the runAllTests.py an executable file, please run "chmod +x runAllTests.py" in the scripts folder. This will allow the command ./scripts/runAllTests.py to work from the root folder.**
