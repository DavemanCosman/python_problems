from itertools import product

if __name__ == '__main__':
    K, M = map(int, input().split())

    input_lists = []
    for _ in range(K):
        _, *elements = map(int, input().split())
        input_lists.append(elements)

    max_mod_sum = max(
        sum(x**2 for x in combo) % M
        for combo in product(*input_lists)
    )

    print(max_mod_sum)