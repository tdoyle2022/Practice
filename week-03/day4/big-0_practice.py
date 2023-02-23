def largest(array, value):
  for item in array:
    if item > value:
      return False
  return True 

# Above is O(n)

def info_dump(customers):
  
  print('Customer Names:')
  for customer in customers: 
    print(customer['name'])
  
  print('Customer Locations:')
  for customer in customers: 
    print(customer['country'])

# Above is O(n)

def first_element_is_red(array):
  return array[0] == 'red' 
# O(1)

def duplicates(array):
  for index1, item1 in enumerate(array):
    for index2, item2 in enumerate(array):
      if index1 == index2:
        continue
      if item1 == item2:
        return True
  return False
# O(n^2)

words = ['chocolate', 'coconut', 'rainbow']
endings = ['cookie', 'pie', 'waffle']

for word in words:
  for ending in endings:
    print(word + ending)
# O(n^2)

numbers = [1,2,3,4,5,6,7,8,9,10]

def print_array(array):
  for item in array:
    print(item)

# O(n)

def insertionSort(arr): 
  for i in range(1, len(arr)): 
    key = arr[i] 
    j = i-1
    while j >=0 and key < arr[j] : 
      arr[j+1] = arr[j] 
      j -= 1
    arr[j+1] = key 
# O(n^2)

for i in range(len(my_list)):
  min_idx = i
  for j in range(i+1, len(my_list)):
      if my_list[min_idx] > my_list[j]:
          min_idx = j

  my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]

# O(n^2)


