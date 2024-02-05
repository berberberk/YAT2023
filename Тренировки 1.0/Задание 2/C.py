def find_closest_element(seq, num):
    defect = [abs(x - num) for x in seq]
    return seq[defect.index(min(defect))]


assert find_closest_element([1, 2, 3, 4, 5], 5) == 5
assert find_closest_element([1, 2, 6, 7, 8], 5) == 6
assert find_closest_element([1, 2, 3, 4, 5], -1) == 1

def main():
    length = int(input())
    seq = list(map(int, input().split()))
    num = int(input())
    print(find_closest_element(seq, num))


if __name__ == '__main__':
    main()

