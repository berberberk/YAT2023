def more_than_neighbors(seq):
    cnt = 0
    for i in range(1, len(seq) - 1):
        if seq[i] > seq[i - 1] and seq[i] > seq[i + 1]:
            cnt += 1
    return cnt


assert more_than_neighbors([1, 2, 3, 4, 5]) == 0
assert more_than_neighbors([5, 4, 3, 2, 1]) == 0
assert more_than_neighbors([1, 5, 1, 5, 1]) == 2

def main():
    seq = list(map(int, input().split()))
    print(more_than_neighbors(seq))


if __name__ == '__main__':
    main()

