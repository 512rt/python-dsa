from typing import List

class sorting:

    def __init__(self):
        pass
    
    def insertion_sort(self, arr: List[int]) -> List[int]:

        n = len(arr)
        print("array -> ", arr)
        for i in range(1, n):
            j = i - 1
            if arr[j+1] < arr[j]:
                print(f"{arr[j+1]} < {arr[j]}")

            while j>=0 and arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                j -= 1
                print(arr)

        return arr
    
    def merge_sort(self, arr: List[int]) -> List[int]:

        return self.merge_sort_helper(arr, 0, len(arr)-1)
        
        

    def merge_sort_helper(self, arr: List[int], s: int, e: int) -> List[int]:

        if e - s + 1 <=1:
            return arr
        
        m = (e + s) // 2

        self.merge_sort_helper(arr, s, m)
        self.merge_sort_helper(arr, m+1, e)

        self.merge(arr, s, m, e)
        
        return arr
    
    def merge(self, arr: List[int], s: int, m: int, e: int):

        L = arr[s:m+1]
        R = arr[m+1:e+1]

        i = 0 # L index
        j = 0 # R index
        k = s # arr staring index

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            



# if __name__ == "__main__":
#     print("main from Sorting")

# sorting = Sorting()
# arr = [2,1,7,4,3,8,5]
# print("result -> ", sorting.insertion_sort(arr))


    