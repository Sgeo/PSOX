from domain import Domain, argtypes, rettypes
from psoxtypes import FNUM, FNUM1, FBYTES, STRING, STRINGNL, LNUM, LBYTES

PSOX_VERSION = (0, 0, 0)
MY_VERSION = 1

class MyDomain(Domain):
    
    @argtypes()
    @rettypes()
    def f00(self):
        from time import sleep
        print "E A S!"
        print "T E R!"
        sleep(2)
        print "M O U S E!"
        sleep(2)
        print "No wait!"
        print "I was not thinking of Mickey Mouse! I hate Mickey Mouse!"
        print "No wait, I mean I never heard of Mickey Mouse! Who's this Mickey Mouse?"
        print "***watches a black helicopter arrive at his house***"
        print "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
        
    @argtypes(FNUM1, STRINGNL)
    @rettypes(LNUM)
    def f01(self, base, string):
        return int(string, base)
        
    @argtypes(FNUM1, FNUM1)
    @rettypes(STRING)
    def f02(self, base, num):
        if(base==8):
            return oct(num)
        elif(base==10):
            return str(num)
        elif(base==16):
            return hex(num)
        else:
            raise NotImplementedError
    
    @argtypes(FNUM1, LNUM)
    @rettypes(STRING)
    def f03(self, base, num):
        if(base==8):
            return oct(num)
        elif(base==10):
            return str(num)
        elif(base==16):
            return hex(num)
        else:
            raise NotImplementedError  
            
    @argtypes(FNUM1)
    @rettypes(FNUM1)
    def f04(self, byte):
        return int(not byte)
        
    @argtypes(FNUM1)
    @rettypes(FNUM1)
    def f05(self, byte):
        return (byte ^ 0xFF)
     
    @argtypes(FNUM1, FNUM1)
    @rettypes(FNUM1)
    def f06(self, b1, b2):
        return int(b1 & b2)
       
    @argtypes(FNUM1, FNUM1)
    @rettypes(FNUM1)
    def f07(self, b1, b2):
        return int(b1 | b2)
    
    @argtypes(FNUM1, FNUM1)
    @rettypes(FNUM1)
    def f08(self, b1, b2):
        return int(b1 ^ b2)
        
    @argtypes(FNUM1, FNUM1)
    @rettypes(FNUM1)
    def f09(self, n1, n2):
        return n1 + n2
    
    @argtypes(LNUM, LNUM)
    @rettypes(LNUM)
    def f0A(self, n1, n2):
        return n1 + n2

    @argtypes(FNUM1, FNUM1)
    @rettypes(FNUM1)
    def f0B(self, n1, n2):
        return n1 - n2
    
    @argtypes(LNUM, LNUM)
    @rettypes(LNUM)
    def f0C(self, n1, n2):
        return n1 - n2
        
    @argtypes(FNUM1, FNUM1)
    @rettypes(FNUM1)
    def f0D(self, n1, n2):
        return n1 * n2
    
    @argtypes(LNUM, LNUM)
    @rettypes(LNUM)
    def f0E(self, n1, n2):
        return n1 * n2
        
    @argtypes(FNUM1, FNUM1)
    @rettypes(FNUM1)
    def f0F(self, n1, n2):
        return n1 / n2
    
    @argtypes(LNUM, LNUM)
    @rettypes(LNUM)
    def f10(self, n1, n2):
        return n1 / n2
        
    @argtypes(FNUM1, FNUM1)
    @rettypes(FNUM1)
    def f11(self, n1, n2):
        return n1 % n2
    
    @argtypes(LNUM, LNUM)
    @rettypes(LNUM)
    def f12(self, n1, n2):
        return n1 % n2
        
    @argtypes(FBYTES(1))
    @rettypes(FBYTES(1))
    def f13(self, b):
        return b
        
the_domain = MyDomain
