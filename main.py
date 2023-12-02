# Simple 8086 procesor symulator 
# IDE: VSCode 

import tkinter as tk

# Registers of x86 architecture 
R8 = ["AL", "CL", "DL", "BL", "AH", "CH", "DH", "BH"]
R16 = ["AX", "CX", "DX", "BX", "SP", "BP", "SI", "DI"]
R32 = ["EAX", "ECX", "EDX", "EBX", "ESP", "EBP", "ESI", "EDI"]
MOD = ["11", "00"]
LABELS = []
COUNTER = [0]
MACHINECODES = []
det checkRegister(register):
    if register in R8:
        return [8, R8.index(register)]
    elif register in R16:
        return [16, R16.index(register)]
    elif register in R32:
        return [32, R32.index(register)]
    else:
        return [1, "Nieprawidłowy rejestr"]

