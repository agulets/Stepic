class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


if __name__ == '__main__':
    a = A()
    b = A()

a.bar()
a.foo()

c = A()

print(a.val)
print(b.val)
print(c.val)
