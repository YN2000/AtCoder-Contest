# judge the size
def judge_size(a, b):
    print("? %s %s" % (a, b), flush=True)
    ans = input()
    if (ans == ">"):
        # a > b
        return True
    else:
        # a <= b
        return False


# insertion sort
def insertion_sort(s, Q):
    temp = 0
    j = 0
    for i in range(1, len(s)):
        temp = s[i]
        j = i-1
        while j>=0 and judge_size(s[j], temp) and Q>0:
            s[j+1] = s[j]
            j-=1
            Q-=1
        s[j+1] = temp
        Q-=1
    
    return s


#bubble sort
def bubble_sort(s, Q):
    for i in range(len(s)):
        for j in range(len(s) - i-1):
            if judge_size(s[j], s[j+1]) and Q>0:
                s[j], s[j+1] = s[j+1], s[j]
            Q-=1

    return s

def main():
    N, Q = map(int, input().split())

    s = []
    for i in range(N):
        s.append(chr(ord('A') + i))

    s = insertion_sort(s, Q)
    #s = bubble_sort(s, Q)

    print("! %s" % "".join(s), flush=True)


if __name__ == "__main__":
    main()