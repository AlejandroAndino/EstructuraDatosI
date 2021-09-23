def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

random_list_of_nums = [5, 2, 1, 8, 4]
print(random_list_of_nums)
bubble_sort(random_list_of_nums)
print('Ordenamiento Burbuja')
print(random_list_of_nums)

