from sorting import sorting

def main():
    sorting = sorting()
    arr = [2,1,7,4,3,8,5]
    print("result -> ", sorting.insertion_sort(arr))


if __name__ == "__main__":
    print("main from main")
    main()
