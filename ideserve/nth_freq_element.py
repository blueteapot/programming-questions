import heapq

class Item:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq

    def __lt__(self, other):
        return self.freq > other.freq

    def __str__(self):
        return "val " + str(self.val) + ", freq = " + str(self.freq)

def nth_frequent_element(lst, n):
    freq_dict = {}
    for i in range(len(lst)):
        val = lst[i]
        if val in freq_dict:
            freq_dict[val] += 1
        else:
            freq_dict[val] = 1

    items = []
    for key, value in freq_dict.items():
        item = Item(key, value)
        items.append(item)

    heapq.heapify(items)
    for i in range(n-1):
        heapq.heappop(items)

    return heapq.heappop(items)

print(nth_frequent_element([1,2,3,1,2, 2, 2, 2, 5, 5, 5, 5], 1))
print(nth_frequent_element([1,2,3,1,2, 2, 2, 2, 5, 5, 5, 5], 2))
print(nth_frequent_element([1,2,3,1,2, 2, 2, 2, 5, 5, 5, 5], 3))
print(nth_frequent_element([1,2,3,1,2, 2, 2, 2, 5, 5, 5, 5], 4))
