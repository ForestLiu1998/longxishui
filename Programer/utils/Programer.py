import serial
import json
import time

ADDH = "00"
ADDL = "01"
NETID = "02"
REG0 = "03"
REG1 = "04"
REG2 = "05"
REG3 = "06"
CRYPT_H = "07"
CRYPT_L = "08"





class Programer:
    def __init__(self,portx,bps):
        self.ser = serial.Serial(portx,bps,timeout = 5)
       

    def close(self):
        self.ser.close()


    def regInst(self,inst,baddr,length,paralist):
        s=inst + baddr + length
        for p in paralist:
            s+=p
        #print(self.ser.write(bytes.fromhex(s)))
        #print(s)
        time.sleep(3)
        return self.ser.read(1000)

    def program(self,cj):
        self.regInst("c0",ADDH,"09",[cj["addh"],cj["addl"],cj["netid"],cj["reg0"],cj["reg1"],cj["reg2"],cj["crypt_h"],cj["crypt_l"] ] )
        

    def readall(self):
        recv = self.regInst("c0","00","07",[])
        return recv
        
        
        
    
    


if __name__=="__main__":

    #use instance:
    
    
    p = Programer("COM5",115200) #COMX BPS 初始波特率为9600 见手册，这里115200为测试用
    
    #print(p.regInst("c0",ADDH,"01",["abcdefabcdef"])) #regInst 方法用于写命令，返回指令返回的值
    

    #写配置文件，根据寄存器，以字符串形式表达8位16进制，比如十六进制0x9f写作 "9f"
    config = {"addh":"f1","addl":"fd","netid":"1d","reg0" : "af","reg1":"de","reg2":"12","crypt_h":"01","crypt_l":"00"} 

    #调用该函数对该片进行烧录
    print(p.program(config))

    #TODO:调用该函数对该片的所有寄存器进行读取
    print(p.readall())



    p.close() #需要显式调用close函数来关闭com口
