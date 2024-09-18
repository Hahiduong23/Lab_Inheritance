import random
class RandomList(list):
    def get_random_element(self):
        if not self:
            raise IndexError ("Danh sach rong")
        random_index = random.randint(0 , len(self)-1)
        return self.pop(random_index)

rl = RandomList ([1,2,3,4,5,6])
print(rl.get_random_element())
print(rl)