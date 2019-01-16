'''
Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass

Антон написал код, который выглядит следующим образом.

try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...

Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде будет пойман их предок.
Но Антон не помнит какие исключения наследуются от каких.
Помогите ему выйти из неловкого положения и напишите программу, которая будет определять обработку каких исключений можно удалить из кода.

Важное примечание:
В отличие от предыдущей задачи, типы исключений не созданы.
Создавать классы исключений также не требуется
Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее где-то поймали их предка.

Формат входных данных
В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс.
Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.

Формат выходных данных
Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом поведение программы.
Имена следует выводить в том же порядке, в котором они идут во входных данных.

Пример теста 1
Рассмотрим код

try:
   foo()
except ZeroDivision :
   print("ZeroDivision")
except OSError:
   print("OSError")
except ArithmeticError:
   print("ArithmeticError")
except FileNotFoundError:
   print("FileNotFoundError")


...

По условию этого теста, Костя посмотрел на этот код, и сказал Антону, что исключение FileNotFoundError можно не ловить,
ведь мы уже ловим OSError -- предок FileNotFoundError
Sample Input:

4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError
Sample Output:

FileNotFoundError
'''


class Relations:
    relations = {}
    classes = []
    tmp_queue = []
    list_of_queue = []
    result_list = []

    def add_relation(self, input_string):
        if input_string.find(":") != -1:
            cl_, bases_cl_string = input_string.split(":")
            cl = cl_.strip()
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
        # print(Relations.relations)

    def search(self, cl_1, cl_2):
        relations = Relations.relations
        cl_2_parents = relations.get(cl_2)
        if cl_2_parents.count(cl_1) != 0:
            result = True
            return result
        else:
            if len(cl_2_parents) == 0 and len(Relations.tmp_queue) == 0:
                result = False
                return result
            else:
                if len(cl_2_parents) != 0:
                    for element in cl_2_parents:
                        Relations.tmp_queue.append(element)
                return Relations.search(self, cl_1, Relations.tmp_queue.pop(0))

    def create_list_of_queue(self, num):
        for i in range(num):
            Relations.list_of_queue.append(str(input()).strip())
        # print(Relations.list_of_queue)

    def solution(self):
        list_of_queue = Relations.list_of_queue
        list_of_queue.reverse()
        for i in range(len(list_of_queue) - 1):
            # print(list_of_queue)
            element_1 = list_of_queue.pop(0)
            for element_2 in list_of_queue:
                # print('Relations(%s , %s)' % (element_2, element_1))
                if Relations.relations.get(element_1) is None:
                    # print('!')
                    # Relations.result_list.append(element_1)
                    break
                if element_1 == element_2:
                    # print('!!')
                    if Relations.result_list.count(element_1) == 0:
                        Relations.result_list.append(element_1)
                    break
                if Relations.search(self, element_2, element_1):
                    # print('!!!')
                    Relations.result_list.append(element_1)
                    break
                # print(Relations.result_list)
                # print('')
        Relations.result_list.reverse()
        for element in Relations.result_list:
            print(element)


if __name__ == '__main__':
    import sys
    sys.stdin = open("stepic_2_1_2_stdin", "r")
    evil = Relations()
    evil.relation_cycle()
    requests_num = int(input())
    evil.create_list_of_queue(requests_num)
    evil.solution()
