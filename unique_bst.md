
### 96. Unique Binary Search Trees

$$ C_0 = 1 $$
$$C_{n+1} = \sum^n_{i=0} C_iC_{n-i}$$

```
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n == 1:
            return 1
        c = [0 for i in range(n+1)]
        print(c)
        c[0] = 1
        
        for i in range(1,n+1):
            for j in range(n):
                c[i] = c[i] + c[j]*c[i-1-j]
        return c[n]
```
