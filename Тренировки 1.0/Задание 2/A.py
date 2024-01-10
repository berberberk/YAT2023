def is_monotonic_asc(seq):
    for i in range(1, len(seq)):
        if seq[i - 1] >= seq[i]:
            return "NO"
    return "YES"


assert is_monotonic_asc([1, 7, 9]) == 'YES'
assert is_monotonic_asc([1, 9, 7]) == 'NO'
assert is_monotonic_asc([2, 2, 2]) == 'NO'


def main():
    seq = list(map(int, input().split()))
    print(is_monotonic_asc(seq))


if __name__ == '__main__':
    main()

