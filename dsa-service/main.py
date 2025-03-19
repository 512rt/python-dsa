from typing import List
from sorting import sorting
from linked_list import linked_list
from search import Search
from rough import Rough

def main():

    nums = [1,2,3,4,5]
    n = len(nums)
    for i in range(n):
        for j in range(i, i + n):
            print (f"i -> {i} = {nums[i]}")
            print (f"j -> {j} and j%n -> {j%n} => {nums[j%n]}")


    #test = Rough()
    ## val:bool = test.contains_duplicates()
    #val:bool = test.contains_dups2()
    #print(f" does it contain duplicates : {val}")
    # Sorting
    #sort = sorting()
    #arr = [2,1,7,4,3,8,5]
    #print("result -> ", sort.insertion_sort(arr))
    # print("result -> ", sort.merge_sort(arr))

    # linked list 
    # ll = linked_list()
    # ll.load_run_ll()

    # a = [1] + [2]
    # print (a)
    
    # print ("-----")
    
    # nums = [1,2,3]
    # x = subsets(nums)
    # print (x)



    # searchit = Search()
    # searchit.load_run_search()

def subsets(nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            print(res)
            res += [subset + [num] for subset in res]
        
        return res  


if __name__ == "__main__":
    print("main from main")
    main()

