class BubbleSort:
    def __init__(self, A, n):
        self.A = A
        self.n = n

    def bubbleSort(self):
        for k in range(0, len(A)):
            for i in range(0, len(A)-2):
                if A[i] > A[i + 1]:
                    temp = A[i+1]
                    A[i+1] = A[i]
                    A[i] = temp

    def show(self):
        for i in  range(len(A)-1):
            print(A[i])


if __name__ == '__main__':
    A = [2, 7, 4, 1, 5, 3]
    n = 5
    blsort = BubbleSort(A,n)
    blsort.bubbleSort()
    blsort.show()
