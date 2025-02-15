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

# if __name__ == "__main__":
#     print("main from Sorting")

# sorting = Sorting()
# arr = [2,1,7,4,3,8,5]
# print("result -> ", sorting.insertion_sort(arr))


    