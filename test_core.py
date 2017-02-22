from proj import Task, Network, durationclass

def test_construction():
    a = Task(1, 'a', 1)
    b = Task(2, 'b', 1)
    c = Task(3, 'c', 1, pred_str='[ 1  , 2]')

    n = Network()
    n.add(a)
    n.add(b)
    n.add(c)

    n.link()
    for x in [a, b, c]:
        assert x.tid in n.all_tasks

    assert a in n.root_tasks
    assert b in n.root_tasks
    assert c in a.succ
    assert c in b.succ

def test_duration_class():
    D = durationclass(8)
    x = D()
    y = D()
    assert x.hpd == 8
    assert y.hpd == 8
    assert id(x) != id(y)
    assert str(x) == '8 hours per day'
