# export function info to a file that can be used as a x64dbg script for labeling all function addresses. Replace path in filename with your own file path.
#@author dingusxmcgee
#@category Other
#@keybinding
#@menupath
#@toolbar

import sys
from time import gmtime, strftime

#get current program name in Ghidra
programname = currentProgram.getName()

#get current time
time= strftime("%Y-%m-%d_%H-%M-%S")

#set file path for output
filename = 'PATH_TO_FILE' + programname + "_" + time + ".txt"

#set loop count variable
i = 0

print("Exporting functions")

#loop through each function and output address and function name, prefixed with 'lblset' for importing into x64dbg.
with open(filename, 'a') as file:
    for func in currentProgram.getListing().getFunctions(True):
        funcaddr = str(func.getEntryPoint())
        funcname = str(func.getName())

        text = str("lblset " + funcaddr + ",\"" + funcname + "\"")
        file.write(text + '\n')
        i = i + 1
        
i = str(i)
print(i + " functions saved to " + filename)

