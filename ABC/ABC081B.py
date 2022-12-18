def main():
    N = int(input())

    A = [int(a) for a in input().split()]

    min_count = 5*10e8
    for x in A:
        count = 0
        while x%2 == 0 and x>0:
            x/=2
            count+=1
        if min_count > count:
            min_count = count

    print(min_count)

if __name__ == "__main__":
    main()