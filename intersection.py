import numpy as np
from bisect import bisect, bisect_left, bisect_right
class Obj:
    def __init__(self, v, bracket: bool, id = 0):
        """
        False: ( 
        True: )
        """
        self.value = v
        self.ooc = bracket
        self.id = id
    def __lt__(self, other):
        if self.value < other.value:
            return True
        return False

    def show(self):
        if self.ooc == False:
            print(f"({self.value}", end=" ")
        else:
            print(f"{self.value})", end=" ")


def solve_quadratic_inequality(a, b, c,seed = 0):
    """ ax^2 + bx +c <= 0 """
    if abs(a) < 1e-15:
        a = 0
    # if abs(b) < 1e-19:
    #     b = 0
    if a == 0:
        # print(f"b: {b}")
        if b > 0:
            return [(-np.inf, -c / b)]
            # return [(-np.inf, np.around(-c / b, 10))]
        elif b == 0:
            # print(f"c: {c}")
            if c <= 0:
                return [(-np.inf, np.inf)]
            else:
                print('Error bx + c', seed)
                return 
        else:
            return [(-c / b, np.inf)]
    delta = b*b - 4*a*c
    if delta < 0:
        if a < 0:
            return [(-np.inf, np.inf)]
        else:
            print("Error to find interval. ")
    # print("delta:", delta)
    # print(f"2a: {2*a}")
    x1 = (- b - np.sqrt(delta)) / (2.0*a)
    x2 = (- b + np.sqrt(delta)) / (2.0*a)
    # if x1 > x2:
    #     x1, x2 = x2, x1  
    # x1 = np.around(x1, 10)
    # x2 = np.around(x2, 10)
    if a < 0:
        return [(-np.inf, x2),(x1, np.inf)]
    return [(x1,x2)]

# def intersec_local(Raxis: list, interval: tuple):
#     """
#     Intersection for intervals from quadratic inequation 
#     """
#     ls = Raxis.copy()

#     a, b = Obj(interval[0][0], False), Obj(interval[0][1], True)
#     indexO = bisect(ls, a)
#     indexC = bisect(ls, b)

#     if indexO == len(ls):
#         return []
#     else:
#         temp = []
#         for i in range(indexO, min(indexC, len(ls))):
#             temp.append(ls[i])
#         if ls[indexO - 1].ooc == False:
#             temp = [a] + temp
#         if len(temp)==0 or temp[-1].ooc == False:
#             temp.append(b)
#         ls1 = temp
    
#     if len(interval) == 1:
#         return ls1
#     else:
#         ls = ls1 + ls[indexC:].copy()
        
#         c, d = Obj(interval[1][0], False), Obj(interval[1][1], True)
#         indexO = bisect(ls, c)
#         indexC = bisect(ls, d)

#         if indexO == len(ls):
#             return ls1
#         else:
#             temp = []
#             for i in range(indexO, min(indexC, len(ls))):
#                 temp.append(ls[i])

#             if ls[indexO - 1].ooc == False or temp[0].ooc == True:
#                 temp = [c] + temp
#             if temp[-1].ooc == False:
#                 temp.append(d)
#             ls2 = temp

#             return ls1 + ls2 
#     # raise "Error return"

# def Intersection(a: list) -> list:
#     Raxis = [Obj(-np.inf,False), Obj(np.inf,True)]
#     for each in a:
#         Raxis = intersec_local(Raxis, each)

#     res = []
#     for i in range(0, len(Raxis), 2):
#         res.append((Raxis[i].value, Raxis[i+1].value))
#     return res
# def Intersec_quad_linear(a: list, e: tuple) -> list:
#     Raxis = []
#     for i in range(0, len(a)):
#         Raxis.append(Obj(a[i][0], False))
#         Raxis.append(Obj(a[i][1], True ))
#     # print(e)
#     Raxis = intersec_local(Raxis, e)

#     res = []
#     for i in range(0, len(Raxis), 2):
#         res.append((Raxis[i].value, Raxis[i+1].value))
#     return res
def Intersec(a: list, b: list) -> list:
    Raxis = []
    for interval in a:
        l, r = interval
        Raxis.append(Obj(l, False, 0))
        Raxis.append(Obj(r, True, 0))
    for interval in b:
        l, r = interval
        l_ = Obj(l, False, 1)
        r_ = Obj(r, True, 1)
        Raxis.insert(bisect_left(Raxis, l_), l_)
        Raxis.insert(bisect_left(Raxis, r_), r_)
    
    finalinterval = []
    stack = []
    on0 = False
    on1 = False
    for obj in Raxis:
        # print('||| intersec')
        # obj.show()
        # print()


        if obj.ooc == False:
            if obj.id == 0:
                on0 = True 
            if obj.id == 1:
                on1 = True
            if len(stack) != 0:
                stack.pop()
            stack.append(obj)
        else:
            if len(stack) == 0:
                if obj.id == 0:
                    on0 = False 
                if obj.id == 1:
                    on1 = False
                continue
            temp = stack.pop()
            if on0 and on1:
                finalinterval.append((temp.value, obj.value))
            if obj.id == 0:
                on0 = False 
            if obj.id == 1:
                on1 = False
    return finalinterval
def Union(a: list, b: list) -> list:
    Raxis = []
    for interval in a:
        l, r = interval
        Raxis.append(Obj(l, False))
        Raxis.append(Obj(r, True))
    for interval in b:
        l, r = interval
        l_ = Obj(l, False)
        r_ = Obj(r, True)
        Raxis.insert(bisect_left(Raxis, l_), l_)
        Raxis.insert(bisect_left(Raxis, r_), r_)
    
    finalinterval = []
    stack = []
    for obj in Raxis:
        if obj.ooc == False:
            stack.append(obj)
        else:
            temp = stack.pop()
            if len(stack) == 0:
                finalinterval.append((temp.value, obj.value))
    
    return finalinterval

if __name__ == "__main__":
    da = [(-0.4122605383393618, -0.3804600576589586)] 
    fs = [(-0.47042270208769704, -0.3817176404989392)] 
    aic= [(-1.5756484596917149, -0.407189815328346), (1.0623004540292729, 9.392823837961563)]
# intervalinloop: [(-0.4122605383393618, -0.407189815328346), (1.0623004540292729, 9.392823837961563)]
    dafs = Intersec(da, fs)
    dafsaic = Intersec(dafs, aic)
    print(dafsaic)