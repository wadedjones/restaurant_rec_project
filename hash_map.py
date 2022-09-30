# Hash map for restaurant rec

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.array = [None for x in range(self.size)]

    def __repr__(self):
        return f"{self.array}"

    def hash(self, key, count_collisions=0):
        return sum(key.encode()) + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.size

    def set_value(self, key, value):
        index = self.compressor(self.hash(key))
        current_value = self.array[index]
        if current_value == None:
            self.array[index] = [key, [value]]
            return
        elif current_value[0] == key:
            self.array[index].append([value])
            return
        else:
            num_collision = 1
            while current_value[0] != key:
                new_index = self.compressor(self.hash(key, num_collision))
                new_value = self.array[new_index]
                if new_value == None:
                    self.array[index] = [key, [value]]
                    return
                elif new_value[0] == key:
                    self.array[new_index].append([value])
                else:
                    num_collision += 1

    def get_value(self, key):
        index = self.compressor(self.hash(key))
        current_value = self.array[index]
        if current_value == []:
            return None
        elif current_value[0] == key:
            return current_value[0][1]
        else:
            num_collision = 1
            while current_value[0] != key:
                new_index = self.compressor(self.hash(key, num_collision))
                new_value = self.array[new_index]
                if new_value == []:
                    return None
                elif new_value[0] == key:
                    return new_value[0][1]
                else:
                    num_collision += 1