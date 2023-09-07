'''
maxMachine 클래스를 완성하세요.
'''


class maxMachine:

    def __init__(self):
        self.machine = []

    def addNumber(self, n):
        self.machine.append(n)

    def removeNumber(self, n):
        self.machine.remove(n)

    def getMax(self):
        return max(self.machine)