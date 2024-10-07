d = {'a': 0,
 'p': [
        {
        'nano': 100, 
        'p': {
            'harrier': [
                {'tata': (3, 0, 1, {'fortuner': 1})
                }
                ]
            }
        }
     ]
}



# def GetAddition(item):
#     if type(item) in (list, tuple):
#         s = 0
#         for i in item:
#             s += GetAddition(i)
#         return s
        
#     elif type(item)==dict:
#         s = 0
#         for i in item.values():
#             s += GetAddition(i)
#         return s
#     elif type(item) is int:
#         return item
#     else:
#         return 0


def GetAddition(item):
    if type(item) in (list, tuple, set):
        return sum(GetAddition(i) for i in item)
    elif type(item) is dict:
        return sum(GetAddition(value) for value in item.values())
    else:
        return item

result = GetAddition(d)

print(result)
