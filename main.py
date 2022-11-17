import random


def sums():
    try:
        size = int(input('size->'))
        start = int(input('start->'))
        end = int(input('end->'))
        nums = list()
        nums2 = list()
        list2 = nums
        list3 = list()
        list4 = list()


        for i in range(size):
            nums.append(random.randint(start, end))
        print(f'Перший список: {nums}')
        for i in range(size):
            nums2.append(random.randint(start, end))
        print(f'Другий список: {nums2}')

        #елементи обох cписків (both)
        both = nums + nums2


        # елементи обох списків без повторень (list2)
        list2 = list(dict.fromkeys(both))


        # елементи, спільні для двох списків (list3)
        list3=[nums[i] for i in range(len(nums)) if nums[i] in nums2]


        # тільки унікальні елементи кожного зі списків (list4)
        def list4(both):
            biba = {}
            for i in both:
                biba[i] = biba[i] + 1 if i in biba else 1
            return [i for i in biba.keys() if biba[i] == 1]


        # тільки мінімальне та максимальне значення кожного зі списків (minmax)
        minmax = [min(nums), max(nums), min(nums2), max(nums2)]

        final_list = both, list2, list3, list4, minmax

        print(f'Елементи обох cписків: {both}')
        print(f'Елементи обох списків без повторень: {list2}')
        print(f'Елементи, спільні для двох списків: {list3}')
        print(f'Тільки унікальні елементи кожного зі списків: {list4(both)}')
        print(f'Тільки мінімальне та максимальне значення кожного зі списків: {minmax}')
        print(f'Список з усіма вищепереліченими списками: {final_list}')


    except Exception as ex:
        print(f'Error: {ex}')

sums()