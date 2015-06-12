from django.utils import timezone

def get_todays_report(cls):
    today = timezone.now()
    bills = cls.objects.filter(bill__when__day = today.day)
    items_info = {}
    for b in bills:
        if b.item.name in items_info:
            items_info[b.item.name] += 1
        else:
            items_info[b.item.name] = 1
    return items_info

def get_itemsinfo_bw_dates(cls, start_date, end_date):
    bills = cls.objects.filter(bill__when__range=[start_date, end_date])
    items_info = {}
    for b in bills:
        if b.item.name in items_info:
            items_info[b.item.name] += 1
        else:
            items_info[b.item.name] = 1
    return items_info

class MinHeap(object):
    def __init__(self, n_items):
        self.item_map = {}
        self.heap_map = {}
        self.item_list = []
        self.max_items = n_items

    def _parent(self, idx):
        if idx <= 0:
            return -1
        return (idx // 2)

    def _left(self, idx):
        l = (2 * idx) + 1
        if l >= self.max_items:
            return -1
        return l

    def _right(self, idx):
        r = (2 * idx) + 2
        if r >= self.max_items:
            return -1
        return r

    def _swap(self, l, r):
        self.heap_map[self.item_list[l][0]] = r
        self.heap_map[self.item_list[r][0]] = l
        tmp = self.item_list[l]
        self.item_list[l] = self.item_list[r]
        self.item_list[r] = tmp

    def heapify(self, idx):
        if idx >= self.max_items:
            return
        smallest = idx;
        l = self._left(idx)
        r = self._right(idx)
        if (l != -1) and (self.item_list[smallest][1] > self.item_list[l][1]):
            smallest = l
        if (r != -1) and (self.item_list[smallest][1] > self.item_list[r][1]):
            smallest = r
        if smallest != idx:
            self._swap(smallest, idx)
            self.heapify(smallest)
        return

    def add(self, item, count):
        entry = [item, count]
        if item in self.item_map:
            self.item_map[item] = self.item_map[item] + count
            entry[1] = self.item_map[item]
        else:
            self.item_map[item] = entry[1]
        if len(self.item_list) < self.max_items:
            if item in self.heap_map:
                idx = self.heap_map[item]
                self.item_list[idx][1] = entry[1]
            else:
                self.heap_map[item] = len(self.item_list)
                self.item_list.append(entry)
            if len(self.item_list) == self.max_items:
                i = (self.max_items-1)//2
                while i >= 0:
                    self.heapify(i) 
                    i = i - 1
        elif entry[1] > self.item_list[0][1]:
            if item in self.heap_map:
                idx = self.heap_map[item]
                self.item_list[idx][1] = entry[1]
                self.heapify(idx)
            else:
                del self.heap_map[self.item_list[0][0]]
                self.item_list[0] = entry
                self.heap_map[item] = 0
                self.heapify(0)
    
    def get(self):
         print(self.item_map)
         return self.item_list

#main
if __name__ == '__main__':
    h = MinHeap(7)
    items = ['Masala Dosa', 'Masala Dosa', 'Vada', 'Kal Dosa', 'Veg Kothu',\
            'Chicken Kothu', 'Chicken Pallipalayam', 'Idly', 'Plain Dosa', \
            'Chicken Maharani', 'Veg Kothu', 'Onion Dosa', 'Omlet', \
            'Plain Dosa', 'Kal Dosa', 'Chicken Kothu', 'Chicken Maharani', \
            'Omlet', 'Idly', 'Onion Dosa', 'Kal Dosa', 'Omlet', 'Plain Dosa',\
            'Onion Dosa', 'Ghee Dosa', 'Chicken Pallipalayam', 'Egg Kothu', \
            'Masala Dosa', 'Kal Dosa', 'Egg Kothu', 'NaN', 'Egg Kothu',\
            'NaN', 'Masala Dosa', 'NaN', 'Omlet', 'Chicken Kothu', 'Idly',\
            'Masala Dosa', 'Kal Dosa']
    for i in items:
        h.add(i)
    top_5 = h.get()
    for i in top_5:
        print(i)
