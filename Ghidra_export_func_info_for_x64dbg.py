# export function info to a file that can be used as a x64dbg script for labeling all function addresses. Replace path in filename with your own file path.
#@author dingusxmcgee
#@category Other
#@keybinding
#@menupath
#@toolbar

import sys
from time import gmtime, strftime

programname = currentProgram.getName()
time= strftime("%Y-%m-%d_%H-%M-%S")

filename = 'PATH_TO_FILE' + programname + "_" + time + ".txt"

with open(filename, 'a') as file:
    for func in currentProgram.getListing().getFunctions(True):
        funcaddr = str(func.getEntryPoint())
        funcname = str(func.getName())

        text = str("lblset " + funcaddr + ",\"" + funcname + "\"")
        file.write(text + '\n')