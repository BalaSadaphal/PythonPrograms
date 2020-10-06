pos = -1
list = [1, 3, 5, 9, 12]

ele = 1
lower = 0
upper = len(list) - 1


def search(list, ele, lower=0, upper=len(list)):
    mid = (lower + upper) // 2
    if ele > list[upper - 1] or ele < list[lower]:
        return False

    if ele == list[mid]:
        globals()['pos'] = mid
        return True
    elif ele < list[mid]:
        upper = mid
        return search(list, ele, lower, upper)
    elif ele > list[mid]:
        lower = mid
        return search(list, ele, lower, upper)


found = search(list, ele)

if found:
    print(f'ele found at index {pos + 1}')
else:
    print("ele not found")
