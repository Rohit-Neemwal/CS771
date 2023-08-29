import numpy as np

def twoSum(nums ,target):
        ans = []
        new = np.array(nums)
        print(new)
        new = new - (target/2)
        print(new)
        new1 = sorted(new)
        for i in range(len(new1)-1) : 
            if(new1[i]==new1[i+1]):
                for j in range(len(new)):
                    if(new1[i]==new[j]):
                        ans.append(j)
                    return ans


print(twoSum([4,7,11,2], 9))

print(list(map(abs,[1,2,-3,4])))