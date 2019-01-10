class Relations:
    relations = {}
    classes = []
    queue = []

    def add_relation(self, input_string):
        if input_string.find(":") != -1:
            cl_, bases_cl_string = input_string.split(":")
            cl = cl_.rstrip()
            bases_cl = bases_cl_string.split()
            if Relations.classes.count(cl) == 0:
                Relations.classes.append(cl)
            Relations.classes.extend(bases_cl)
            if cl in Relations.relations.keys():
                bases_cl.extend(Relations.relations.pop(cl))
                Relations.relations[cl] = bases_cl
            else:
                Relations.relations[cl] = bases_cl
        else:
            cl, bases_cl = input_string, []
            if Relations.classes.count(cl) == 0:
                Relations.classes.append(cl)
            if cl in Relations.relations.keys():
                bases_cl.extend(Relations.relations.pop(cl))
                Relations.relations[cl] = bases_cl
            else:
                Relations.relations[cl] = bases_cl

    def relation_cycle(self):
        for i in range(int(input())):
            Relations.add_relation(self, input())
        for element in Relations.classes:
            Relations.relations.setdefault(element, [])

    def search(self, cl_1, cl_2):
        relations = Relations.relations
        cl_2_parents = relations.get(cl_2)
        if cl_2_parents.count(cl_1) != 0:
            result = True
            return result
        else:
            if len(cl_2_parents) == 0 and len(Relations.queue) == 0:
                result = False
                return result
            else:
                if len(cl_2_parents) != 0:
                    for element in cl_2_parents:
                        Relations.queue.append(element)
                return Relations.search(self, cl_1, Relations.queue.pop(0))

    def requests_cycle(self, num):
        for i in range(num):
            Relations.queue.clear()
            cl_1, cl_2 = str(input()).split()
            if cl_1 == cl_2:
                if Relations.classes.count(cl_1) > 0:
                    print("Yes")
                else:
                    print("No")
            else:
                if Relations.search(self, cl_1, cl_2):
                    print("Yes")
                else:
                    print("No")


if __name__ == '__main__':
    import sys
    sys.stdin = open("stepic_1_6_stdin", "r")
    evil = Relations()
    evil.relation_cycle()
    requests_num = int(input())
    evil.requests_cycle(requests_num)
