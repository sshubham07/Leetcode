class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        print(num)
        for i in range(len(num)):
            if num[i]=='6':
                num[i]='9'
                break
        num = ''.join(num)
        return int(num)