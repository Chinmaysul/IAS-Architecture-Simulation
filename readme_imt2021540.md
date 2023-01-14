The program is an IAS machine which executes the function of returning n elements of an AP where the first term of the AP, the common difference and n are given by the user.
The program prints the values of IR,MAR,PC,IBR,AC,MBR after each instruction.
The 'memory' variable is an array that has the memory of the machine
The 'ap' variable is an array that stores each term of the AP
Function to convert decimal to binary of length 12:def dec_to_bin(address)
Function to find the opcode of the instruction:def op_code(instr)
Function to assign the opcodes to IR and IBR:def instr(i)
Function that decodes the opcode and performs the function:def decoder(x)
Function to find the value of MBR:def mbr_val(add1,add2)
Function which computes the AP sum:def ap_sum(a,d,n)