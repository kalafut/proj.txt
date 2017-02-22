from typing import List, Set, Dict, Tuple, Text, Optional, AnyStr
#from datetime import timedelta as D
import re
import sys

class D(int):
    pass

class BaseDuration(D):
    def __str__(self):
        return "{} hours per day".format(self.hpd)

def durationclass(hpd_):
    class C(BaseDuration):
        hpd = hpd_

    return C


class Schedule:
    resources = 1
    weekly_budget = 5 * resources

    def __init__(self):
        self._sched: List[Tuple[Task, D]] = []
        pass


class Task:
    def __init__(self, tid: int, description: str, duration: D, succ: List=[], pri: int=1, pred_str: str='') -> None:
        self.tid = tid
        self.description = description
        self.rem = duration
        self.pri = pri
        self.succ = succ
        self.pred_str = pred_str


class Network:
    def __init__(self):
        self._all_tasks: Dict[int, Task] = {}
        self._root_tasks: List[Task] = []
        self._linked: bool = False

    @property
    def all_tasks(self) -> Dict[int, Task]:
        if not self._linked:
            raise Exception("Tasks not linked")
        return self._all_tasks

    @property
    def root_tasks(self) -> List[Task]:
        if not self._linked:
            raise Exception("Tasks not linked")
        return self._root_tasks

    def add(self, task) -> None:
        self._linked = False
        if task.tid in self._all_tasks:
            raise Exception('Duplicate task ID')
        else:
            self._all_tasks[task.tid] = task

    def link(self):
        """ """
        self._root_tasks = []
        for task in self._all_tasks.values():
            if task.pred_str:
                for tid in task.pred_str.replace(' ', '').strip('[]').split(','):
                    self._all_tasks[int(tid)].succ.append(task)
            else:
                self._root_tasks.append(task)
        self._linked = True



def advance(q):
    """Schedule one period"""
    budget = D(5)

    for task in q:
        amt = min(task.rem, budget)
        print(" ", task.description, amt)
        task.rem -= amt
        budget -= amt
        if budget <= D(0):
            break

    # replace done tasks
    new_q = []
    for task in q:
        if task.rem > D(0):
            new_q.append(task)
        else:
            for succ in task.succ:
                if succ.rem > D(0):
                    new_q.append(succ)

    return new_q

def schedule(q):
    week = 1
    while len(q) > 0:
        print('\nWeek {}'.format(week))
        q = advance(q)
        week += 1


task_re = re.compile(r'(?P<id>\d+) +(?P<task>.*?) *(?P<deps>\[.*\])?$')
def parse(fn):
    all_tasks = {}
    with open(fn) as f:
        for line in f:
            match = task_re.match(line)
            if match:
                print(match.groups())
                print(match.group('task'))

if __name__ == '__main__':
    q = []
    q.append(Task(tid=1, description='B', succ=[], duration=D(4), pri=2))
    q.append(Task(tid=2, description='C', succ=[Task(tid=3, description='A', succ=[], duration=D(9), pri=1)], duration=D(4), pri=2))

    parse('proj.txt')
    schedule(q)
    #parse(sys.argv[1])

