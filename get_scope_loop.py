#Jess Valdez 7-2-2013
#Read the serial files

import visa
import sys
import shutil
import datetime
import time


sourcepathfinal = ""

#fnam = ''
sourcepath = 'C:\R2\PROJECTS\HAST\HTOL M3.0'
destpath = 'Z:\Jess\Drop Box\ScopeCapture'

cytec = visa.instrument('GPIB0::7::INSTR')
scope = visa.instrument('TCPIP0::172.16.20.113::inst0::INSTR')
print scope.ask('*IDN?')

file = open("sernum_bib.txt")
filec = open("cytec.txt")
ffnam = ""

while 1:
    line = file.readline()
    if not line:
        file.close()
        filec.close()
	break
    #print line
    
    #======================
    # switch the box here
    #======================
    cline = filec.readline()
    cline = cline[:-1]
    cytec.write(cline)
    print cline
    
    #======================
    # Command scope to save file
    #======================
    scope.write('SAVE:IMAG:FILEF PNG')
    scope.write('HARDCOPY START')
    raw_data = scope.read_raw()

    #======================
    # Build file name
    #======================
    line = line[:-1] #remove carriage return 
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    ffnam = line + '_' + st + '.png'
    
    #=====================
    fid = open(ffnam, 'wb')
    #This will save file where this python script is located
    fid.write(raw_data)
    fid.close()
    
    
    sourcepathfinal = sourcepath + '\\' + ffnam
    print ffnam
    print sourcepathfinal

    shutil.move(sourcepathfinal, destpath)
    time.sleep(0.5)


    print 'Done'