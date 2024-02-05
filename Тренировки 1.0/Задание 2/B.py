def define_seq_type(seq):
    seq_types = {'CONSTANT': True,
                 'ASCENDING': True,
                 'WEAKLY ASCENDING': True,
                 'DESCENDING': True,
                 'WEAKLY DESCENDING': True,
                 'RANDOM': True}
    for i in range(1, len(seq)):
        if seq[i - 1] == seq[i]:
            seq_types['ASCENDING'] = False
            seq_types['DESCENDING'] = False
        if seq[i - 1] < seq[i]:
            seq_types['WEAKLY DESCENDING'] = False
            seq_types['DESCENDING'] = False
            seq_types['CONSTANT'] = False
        if seq[i - 1] > seq[i]:
            seq_types['WEAKLY ASCENDING'] = False
            seq_types['ASCENDING'] = False
            seq_types['CONSTANT'] = False
    ans = 'RANDOM'
    for k, v in seq_types.items():
        if k != 'RANDOM':
            if v:
                if k == 'CONSTANT':
                    ans = k
                    break
                if k == 'ASCENDING':
                    seq_types['WEAKLY ASCENDING'] = False
                    ans = k
                elif k == 'DESCENDING':
                    seq_types['WEAKLY DESCENDING'] = False
                    ans = k
                else:
                    ans = k
    return ans


assert define_seq_type([5, 5, 5, 5, 5]) == 'CONSTANT'
assert define_seq_type([1, 2, 3, 4, 5]) == 'ASCENDING'
assert define_seq_type([1, 2, 2, 4, 5]) == 'WEAKLY ASCENDING'
assert define_seq_type([5, 4, 3, 2, 1]) == 'DESCENDING'
assert define_seq_type([5, 4, 4, 2, 1]) == 'WEAKLY DESCENDING'
assert define_seq_type([1, 3, 2, 4, 4]) == 'RANDOM'


def main():
    seq = []
    a = int(input())
    while a != -2000000000:
        seq.append(a)
        a = int(input())
    print(define_seq_type(seq))


if __name__ == '__main__':
    main()
