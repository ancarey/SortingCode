class Sorting:
    def __init__(self, arr = []):
        self.array = arr
        self.n = len(self.array)

    #Bubble Sort
    def bubbleSort(self):
        print("Welcome to Bubble Sort!\n")
        for i in range(self.n):
            print("Sort: ",i, self.array)
            for j in range(0, self.n-i-1):
                if (self.array[j] > self.array[j+1]):
                    temp = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = temp
        return self.array