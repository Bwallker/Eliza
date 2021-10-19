# loggning.py
# A simple logging utility that uses a standard function log()
# to log information to a log file.
# the name of the log file is defined by logName and logFileName.
# The log is cleared every time this module is called
#

import logging

#--- define the log file name ---
logName = "eliza"
logFileName = logName+'.log'

#--- create a logging object called logger ---
logger = logging.getLogger( logName )
hdlr = logging.FileHandler( logFileName )

#--- set the format to be just the message ---
#formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
formatter = logging.Formatter('%(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 

#--- log all levels above and including info messages ---
logger.setLevel(logging.INFO)

#--- clear the log file when starting ---
logFile = open( logFileName, "w" )
logFile.write( "" )
logFile.close()

#--- the main log function. Appends the string s to the log ---
def log( s ):
     logger.info( s )

