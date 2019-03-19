from collections import Counter


def test_counter_counts_strings(expect):
    expect(Counter('abc123abc125')) == {'a':2, 'b':2, 'c':2, '1':2, '2':2, '3':1, '5':1}


def test_counter_counts_lists(expect):
    counted = Counter(['a', 'b', 'c', '1', '2', '3', 'a', 'b', 'c', '1', '2', '5'])
    expect(counted) == {'a':2, 'b':2, 'c':2, '1':2, '2':2, '3':1, '5':1}


def test_counter_init_with_counts(expect):
    counted = Counter(dict(a=3, b=5, c=10))
    expect(counted) == dict(a=3, b=5, c=10)


def test_counter_can_be_incemented(expect):
    counted = Counter(dict(a=3, b=5, c=10))
    expect(counted) == dict(a=3, b=5, c=10)

    counted.update('aaabcc')
    expect(counted) == dict(a=6, b=6, c=12)

    counted.update(dict(a=4, b=4, c=8, d=30))
    expect(counted) == dict(a=10, b=10, c=20, d=30)


def test_counter_accessors(expect):
    counted = Counter(dict(a=3, b=5, c=10))
    expect(counted['d']) == 0
    expect(counted['a']) == 3


def test_counter_arithmetic(expect):
    counted = Counter(dict(a=-3, b=5, c=10))
    another_counted = Counter(dict(a=3, b=5, c=10))
    expect(counted - another_counted) == Counter()
    expect(counted + another_counted) == Counter(b=10, c=20)

    # pos minimums
    expect(counted & another_counted) == Counter(b=5, c=10)
    # maximums
    expect(counted | another_counted) == Counter(a=3, b=5, c=10)
