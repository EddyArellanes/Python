# Step 1: Compare Elements in Adjacents
# Step 2: Check element against all rest of elements, if is greater than next, swap
def bubbleSort(array):
  size = len(array) 

  for element in range(size):

    for subelement in range(0, size-element-1):
      if array[subelement] > array[element + 1]:
        array[subelement], array[element + 1] = array[element + 1], array[subelement]


array = [190, 999, 1, 5, 4, 44, 749]

bubbleSort(array)

print("Array Ordered Asc is:")
for i in range(len(array)):
  print("%d"%array[i])