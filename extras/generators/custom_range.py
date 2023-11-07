class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        curr = self.start
        while curr < self.end:
            yield curr
            curr += 1


for i in Range(0, 5):
    print(i)
