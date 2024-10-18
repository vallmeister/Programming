class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split('-')
        return '-'.join([self.get_binary(int(d)) for d in date])

    def get_binary(self, num):
        binary = []
        while num > 0:
            binary.append(str(num % 2))
            num //= 2
        return ''.join(reversed(binary))
