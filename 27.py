import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Жишээ input
arr_bubble = [64, 34, 25, 12, 22, 11, 90]

# Bubble Sort гүйцэтгэлийн хугацааг илүү нарийвчлалтай хэмжих
start_time = time.perf_counter()
sorted_bubble = bubble_sort(arr_bubble.copy())
end_time = time.perf_counter()
bubble_time = end_time - start_time

print("Bubble Sort үр дүн:", sorted_bubble)
print(f"Bubble Sort хугацаа: {bubble_time:.8f} секунд")
