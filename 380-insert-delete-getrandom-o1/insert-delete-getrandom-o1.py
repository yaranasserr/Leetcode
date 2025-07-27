import random  # Used to randomly pick an element from the list

class RandomizedSet:
    def __init__(self):
        # Initialize an empty list to store the values
        self.lst = []
        # Initialize a dictionary to map value -> index in the list
        self.idx_map = {}

    def search(self, val):
        # Check if the value exists in the set
        return val in self.idx_map

    def insert(self, val):
        # If the value already exists, return False (no duplicates allowed)
        if self.search(val):
            return False

        # Append the new value to the end of the list
        self.lst.append(val)
        # Store the index of the value in the dictionary
        self.idx_map[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        # If the value doesn't exist, return False
        if not self.search(val):
            return False

        # Get the index of the value to remove
        idx = self.idx_map[val]
        # Move the last element to the index of the element to remove
        self.lst[idx] = self.lst[-1]
        # Update the index of the moved element in the map
        self.idx_map[self.lst[-1]] = idx
        # Remove the last element from the list
        self.lst.pop()
        # Remove the value from the dictionary
        del self.idx_map[val]
        return True

    def getRandom(self):
        # Return a random element from the list
        return random.choice(self.lst)
