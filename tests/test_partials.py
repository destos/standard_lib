from functools import partial

import pytest


# ARGS

def function_with_many_args(something, extra):
    return something + extra


new_arg_func = partial(function_with_many_args, 'content')


def test_our_partial(expect):
    result = new_arg_func('_is_good')
    expect(result) == 'content_is_good'


def test_not_enough_args():
    with pytest.raises(TypeError):
        new_arg_func()


# KWARGS

def function_with_kwargs(something, more=None, optional="is_ok"):
    options = [something, more, optional]
    return '_'.join(options)


new_kwarg_func = partial(function_with_kwargs, 'starting')

def test_our_kwarg_partial(expect):
    result = new_kwarg_func(more='later')
    expect(result) == 'starting_later_is_ok'

    result = new_kwarg_func('right_now', optional='is_great')
    expect(result) == 'starting_right_now_is_great'


def test_out_kwarg_partial_errors():
    with pytest.raises(TypeError):
        new_kwarg_func()

    with pytest.raises(TypeError):
        new_kwarg_func(optional='something')
