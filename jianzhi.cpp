//
剑指 Offer 04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
//
class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        int i = matrix.size()-1, j=0;
        while(i>=0 && j<matrix[0].size())
        {
            if (matrix[i][j] > target) i--;
            else if (matrix[i][j] < target) j++;
            else return true;
        }
        return false;

    }
};

//
请实现一个函数，把字符串 s 中的每个空格替换成"%20"
//
class Solution {
public:
    string replaceSpace(string s) {
        int n = s.size();
        int count = 0;
        for (char c:s){
            if (c == ' ') count++;
        }
        s.resize(n+2*count);
        for(int i=n-1,j=s.size()-1; i<j; i--,j--){
            if (s[i] != ' ') s[j] = s[i];
            else {
                s[j] = '0';
                s[j-1] = '2';
                s[j-2] = '%';
                j-=2;
            }
        }
        return s;
    }
};


