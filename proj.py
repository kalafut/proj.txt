import sys

from recordclass import recordclass

Task = recordclass('Task', 'description succ rem pri')

resources = 1
weekly_budget = 5 * resources

q = []
q.append(Task(description='A', succ=[], rem=9, pri=1))
q.append(Task(description='B', succ=[], rem=4, pri=2))
q.append(Task(description='C', succ=[], rem=4, pri=2))


def advance(q):
    """Schedule one period"""
    budget = weekly_budget

    # replace done tasks
    for task in q:
        amt = min(task.rem, budget)
        print(" ", task.description, amt)
        task.rem -= amt
        budget -= amt
        if budget <= 0:
            break

    q[:] = [x for x in q if x.rem > 0]

def schedule():
    week = 1
    while len(q) > 0:
        print(f'\nWeek {week}')
        advance(q)
        week += 1


def parse(fn):
    with open(fn) as f:
        for line in f:
            pass

if __name__ == '__main__':
    schedule()
    #parse(sys.argv[1])

