from sorting import sorting

def main():
    sort = sorting()
    arr = [2,1,7,4,3,8,5]
    # print("result -> ", sort.insertion_sort(arr))
    print("result -> ", sort.merge_sort(arr))


if __name__ == "__main__":
    print("main from main")
    main()
