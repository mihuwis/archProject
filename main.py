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
# Sprawdzenie rodzaju rejestru
def checkRegister(register):
    if register in R8:
        return [8, R8.index(register)]
    elif register in R16:
        return [16, R16.index(register)]
    elif register in R32:
        return [32, R32.index(register)]
    else:
        return [1, "Nieprawidłowy rejestr"]

def decToBin(number):
    value = bin(number).replace("0b", "")
    if len(value) == 2:
        value = "0" + value
    elif len(value) == 1:
        value == "00" + value
    return value

def addBlock(reg1, reg2):
    opcodes = ["0x00", "0x01", "0x02", "0x03"]
    if reg2[0] != "[":
        returnReg1 = checkRegisters(reg1.upper())
        returnReg2 = checkRegisters(reg2.upper())

        if (returnReg1[0] == 1 or returnReg2[0] == 1):
            return "Coś poszło niezgodnie z planem"
        if (returnReg1[0] != 1 or returnReg2[0]):
            return "Argumenty musza być tego samego typu"

        BinaryValue = MOD[0] + decToBin(returnReg2[1]) + decToBin(returnReg1[1])
        DecValue = int(BinaryValue, 2)
        if (returnReg1[0] == 8):
            return [opcodes[0], hex(DecValue)]
        elif (returnReg1[0] == 16):
            return ["0x66", opcodes[1], hex(DecValue)]
        elif (returnReg1[0] == 32):
            return [opcodes[1], hex(DecValue)]
        else:
            return "Coś poszło nie tak"
    
    else: 
        returnReg1 = checkRegister(reg1.upper())
        returnReg2 = checkRegister(reg2[1:-1].upper())

        if (returnReg1[0] == 1 or returnReg2[0] == 1):
            return "Coś poszło niezgodnie z planem"
        if (returnReg1[0] != 1 or returnReg2[0]):
            return "Argumenty musza być tego samego typu"
        
        BinaryValue = MOD[1] + decToBin(returnReg1[1]) + decToBin(returnReg2[1])
        DecValue = int(BinaryValue, 2)
        if (returnReg1[0] == 8):
            return [opcodes[2], hex(DecValue)]
        elif (returnReg1[0] == 16):
            return ["0x66", opcodes[3], hex(DecValue)]
        elif(returnReg1[0] == 32):
            return [opcodes[3], hex(DecValue)]
        
        else: 
            return "Coś poszło niezgodnie z planem"
        
def subBlock(reg1, reg2):
