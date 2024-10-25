import time

def insertion_sort(arr):
    # Эхний элементийг орхиж, 2 дахь элементийг эхэлж шалгана
    for i in range(1, len(arr)):
        key = arr[i]  # Одоогийн элемент
        j = i - 1     # Одоогийн элементийн өмнөх элемент

        # Одоогийн элементээс том элементүүдийг баруун тийш шилжүүлнэ
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Одоогийн элементийг өөрийн зөв байранд оруулна
        arr[j + 1] = key

    return arr

# Жишээ input
arr_insertion = [64, 34, 25, 12, 22, 11, 90]

# Insertion Sort гүйцэтгэлийн хугацааг нарийвчлалтай хэмжих
start_time = time.perf_counter()
sorted_insertion = insertion_sort(arr_insertion.copy())
end_time = time.perf_counter()
insertion_time = end_time - start_time

print("Insertion Sort үр дүн:", sorted_insertion)
print(f"Insertion Sort хугацаа: {insertion_time:.8f} секунд")
