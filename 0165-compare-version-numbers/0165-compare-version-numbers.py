class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1=version1.split('.')
        arr2=version2.split('.')
        n = len(arr1)
        m = len(arr2)
        if n<m:
            while len(arr1)<m:
                arr1.append('0')
        if n>m:
            while len(arr2)<n:
                arr2.append('0')
        print(arr1)
        print(arr2)
        for i in range(len(arr1)):
            if int(arr1[i])>int(arr2[i]):
                return 1
            elif int(arr1[i])<int(arr2[i]):
                return -1
        return 0