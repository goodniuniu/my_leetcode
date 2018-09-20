class Solution:
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''
        lenth = len(nums)
        result = []
        for x in range(0,lenth):
            for y in range(x, lenth):
                if nums[x]+ nums[y] == target:
                    result = [x] +[y]

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums,len_of_list=None):
        if not len_of_list:
            len_of_list = len(nums)
        return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.trip('\n')
    lines = readlines()
    
if __name__ == '__main__':
    main()
