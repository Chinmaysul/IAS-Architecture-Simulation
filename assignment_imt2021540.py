#program to find n terms of an AP
#initialising all the variables 
mar=''
mbr=''
ac=''
ir=''
ibr=''
memory=[None]*9
ap=[]
#function to convert decimal to binary of length 12
def dec_to_bin(address):
    b=bin(address)[2:]
    while(len(b)<12):
        b='0'+b
    return(b)

#function to find the opcode of the instruction
def op_code(instr):
    if instr=='LOAD':
        ir='00000001'
    elif instr=='STOR':
        ir='00100001'
    elif instr=='ADD':
        ir='00000101'
    elif instr=='SUB':
        ir='00000110'
    elif instr=='JUMP+':
        ir='00001111'
    else:
        ir='00000000'
    return ir

#function to assign the opcodes to IR and IBR        
def instr(i):
    global ir
    global ibr
    intrs=i.split(' ')
    ir=op_code(intrs[0])
    ibr=op_code(intrs[1])

#function that decodes the opcode and performs the function
def decoder(x):
    global mar
    mar=dec_to_bin(x)
    global ir
    global ac
    if ir=='00000001':
        ac=memory[x]
    elif ir=='00100001':
        memory[x]=ac
    elif ir=='00000101':
        ac=ac+memory[x]
    elif ir=='00000110':
        ac=ac-memory[x]
    elif ir=='00001111':
        if ac>0:
            return True
    else:
        return

#function to find the value of MBR
def mbr_val(add1,add2):
    global mbr
    add_bin1=dec_to_bin(add1)
    add_bin2=dec_to_bin(add2)
    mbr=ir+add_bin1+ibr+add_bin2

#function which computes the AP sum
def ap_sum(a,d,n):
    pc=1
    global ir
    global ibr
    global ac
    global mar
    global mbr
    memory[1]='LOAD ADD'
    memory[2]='STOR LOAD'
    memory[3]='SUB STOR'
    memory[4]='JUMP+ HALT'
    memory[5]=a
    memory[6]=d
    memory[7]=n
    memory[8]=1
    global ap
    while(True):
        ins=memory[pc]
        addr1=5
        instr(ins)
        decoder(addr1)
        ap.append(ac)
        print("PC:",pc)
        print("IR:",ir)
        print("IBR:",ibr)
        print("AC:",ac)
        print("MAR:",mar)
        ir=ibr
        ibr='11111111'
        addr2=6
        decoder(addr2)
        mbr_val(addr1,addr2)
        print("PC:",pc)
        print("IR:",ir)
        print("IBR:",ibr)
        print("AC:",ac)
        print("MAR:",mar)
        print("MBR:",mbr)
        pc+=1
        ins=memory[pc]
        addr1=5
        instr(ins)
        decoder(addr1)
        print("PC:",pc)
        print("IR:",ir)
        print("IBR:",ibr)
        print("AC:",ac)
        print("MAR:",mar)
        ir=ibr
        ibr='11111111'
        addr2=7
        decoder(addr2)
        mbr_val(addr1,addr2)
        print("PC:",pc)
        print("IR:",ir)
        print("IBR:",ibr)
        print("AC:",ac)
        print("MAR:",mar)
        print("MBR:",mbr)
        pc+=1
        ins=memory[pc]
        addr1=8
        instr(ins)
        decoder(addr1)
        print("PC:",pc)
        print("IR:",ir)
        print("IBR:",ibr)
        print("AC:",ac)
        print("MAR:",mar)
        ir=ibr
        ibr='11111111'
        addr2=7
        decoder(addr2)
        mbr_val(addr1,addr2)
        print("PC:",pc)
        print("IR:",ir)
        print("IBR:",ibr)
        print("AC:",ac)
        print("MAR:",mar)
        print("MBR:",mbr)
        pc+=1
        ins=memory[pc]
        instr(ins)
        if(decoder(0)):
            print("PC:",pc)
            print("IR:",ir)
            print("IBR:",ibr)
            print("AC:",ac)
            print("MAR:",mar)
            pc=1
        else:
            ir=ibr
            decoder(0)
            break

#main function
a=int(input("First term of AP:"))
d=int(input("Common difference:"))
n=int(input("No. of terms:"))
ap_sum(a,d,n)
print("Terms of AP:")
for i in ap:
    print(i,end=' ')

        








