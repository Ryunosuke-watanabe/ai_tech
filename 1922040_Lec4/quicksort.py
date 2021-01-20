import random
N = 10

def input_data(data):
    for i in range(N):
        data.append(random.randint(0, N))
    return data

def quicksort(left, right):
    if left >= right:
        return
    else:
        pivot = data[right]
        partition = division(left, right, pivot)
        quicksort(left, partition - 1)
        quicksort(partition + 1, right)

def division(left, right, pivot):
    data_right = []
    data_left = []
    pivot_num = 0
    for i in range(left, right):
        if data[i] < pivot:
            data_left.append(data[i])
        elif data[i] > pivot:
            data_right.append(data[i])
        else:
            pivot_num += 1
    data[left:right+1] = data_left + [pivot] * (pivot_num+1) + data_right
    p = data.index(pivot) + pivot_num
    return p

if __name__ == "__main__":
    data = []
    data = input_data(data)
    print(data)
    quicksort(0, N - 1)
    print(data)
    # print("正しい配列", sorted(data))