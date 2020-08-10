class conv:
    '''A simple base converter
    program.'''
    def __init__(self, string, numBase, reqBase):
        if type(string) != str:
            raise ValueError('Cannot convert non-string type numbers')
        self.ibase = numBase
        self.fbase = reqBase
        self.input = string
        self.final = self.conv()
        
    def __str__(self):
        return '%s'%self.final
    
    def __repr__(self):
        return 'Converted(%s to %s, bases %s to %s)'%(self.input,self.final,self.ibase,self.fbase)

    def conv(self):
        '''The main method that takes care of
        the conversion.'''
        s = int(self.input, self.ibase)
        n = self.fbase
        if n == 10:
            return s
        else:
            res = []
            p = ''
            d = s 
            while d > 0:
                e = d%n
                d //= n
                if e > 9:
                    e += 55
                    e = chr(e)
                    res.append(e)
                else:
                    res.append(e)
            res.reverse()
            for j in res:
                p += str(j)
            return p