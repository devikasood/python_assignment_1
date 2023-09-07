def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    input_string = input("Enter a string of numbers separated by spaces: ")

    num_strings = input_string.split()

    num_list = [int(num) for num in num_strings]

    selection_sort(num_list)

    print("Sorted list:", num_list)

if __name__ == "__main__":
    main()
