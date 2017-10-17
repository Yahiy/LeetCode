def int2bin(n, count=24):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])
    
def hammingDistance(x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        str_x = int2bin(x, 32)
        str_y = int2bin(y, 32)
        hd = 0
        print str_x
        print str_y
        
        for i in range(max(len(str_x), len(str_y))):
            if str_x[i] != str_y[i]:
                hd = hd+1
        return hd

print hammingDistance(1,19)