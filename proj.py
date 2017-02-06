from recordclass import recordclass

Task = recordclass('Task', 'description succ rem pri')

resources = 1
weekly_budget = 5 * resources

q = []
q.append(Task(description='A', succ=[], rem=2, pri=1))
q.append(Task(description='B', succ=[], rem=4, pri=2))


def advance(q):
    budget = weekly_budget

    # replace done tasks
    for task in q:
        amt = min(task.rem, budget)
        print(task.description, amt)
        task.rem -= amt
        budget -= amt
        if budget <= 0:
            break




advance(q)

