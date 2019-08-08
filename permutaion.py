def permute(nums):

    if len(nums) <= 1: return [nums] 
    result = []
    for i, item in enumerate(nums):
        n = nums[:i] + nums[i+1:]
        # print(n)
        for y in permute(n):
            result.append([item] + y)         

    return result
    
def main():
    max_num = 0
    s = [5, 5, 3]
    result = permute(s)
    print(result)
    
    

if __name__ == '__main__':
    main()