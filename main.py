import random


def sums():
    try:
        size = int(input('size->'))
        start = int(input('start->'))
        end = int(input('end->'))
        nums = list()
        nums2 = list()


        for i in range(size):
            nums.append(random.randint(start, end))
        print(nums)
        for i in range(size):
            nums2.append(random.randint(start, end))
        print(nums2)

        both = nums + nums2
        print(both)

        minmax = [min(nums), max(nums), min(nums2), max(nums2)]
        print(minmax)

        list2 = nums
        list3 = list()

        for i in nums2:
            if i not in nums:
                list2.append(i)

        for i in nums:
            if nums2.count(i) > 0 :
                print(i)
                list3.append(i)


        print(list2)
        print(list3)








    except Exception as ex:
        print(f'Error: {ex}')

sums()