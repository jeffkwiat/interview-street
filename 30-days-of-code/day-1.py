
class HackerMath(object):
    def __init__(self, numbers):
        self.numbers = numbers
        
    def mean(self):
        total = 0.0
        for x in self.numbers:
            total += x
        return round(float(total / len(numbers)), 1)
        
    def median(self):
        count = len(self.numbers) - 1
        print(numbers[count], numbers[count + 1])
        
        return (numbers[count] + numbers[count]) / 2

    def mode(self):
        import pdb; pdb.set_trace()
        return max(set(self.numbers), key=self.numbers.count)
        

        
if __name__ == '__main__':
    count = int(input())
    numbers = [int(x) for x in input().split(' ')]
    hackermath = HackerMath(numbers)
    
    print(hackermath.mean())
    # print(hackermath.median())
    print(hackermath.mode())