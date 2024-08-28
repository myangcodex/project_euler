class Problem1:
    def __init__(self):
        self.final_sum = 0
        self.multiples = set()

    def find_multiples_of_m_less_than_n(self, m, n):
        x = m
        while x < n:
            if x % m == 0:
                if x not in self.multiples:
                    self.final_sum += x
                    self.multiples.add(x)
            x += m

    def solve(self):
        self.find_multiples_of_m_less_than_n(3, 1000)
        self.find_multiples_of_m_less_than_n(5, 1000)
        print(self.final_sum)


if __name__ == '__main__':
    problem = Problem1()
    problem.solve()
