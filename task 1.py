# TODO решите задачу
import json

def task() -> float:
    s = 0
    with open('input.json') as file:
        a = json.load(file)
        for i in a:
            s += i['score']*i['weight']
    return round(s, 3)



print(task())
