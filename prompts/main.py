import sys
import fire
from inspect import getmembers


def dummy(verbose=0):
  available_functions = list(map(lambda x: x[0], filter(lambda x: x[0].startswith('get_'), getmembers(sys.modules['__main__']))))
  print(f"Available fn: {', '.join(available_functions)}")


def main(fn='dummy', verbose=0):
  available_functions = list(filter(lambda x: x[0].startswith('get_'), getmembers(sys.modules['__main__'])))
  if fn == 'dummy':
    dummy(verbose)
  elif fn not in list(map(lambda x: x[0], available_functions)):
    dummy(verbose)
  else:
    curr_fn = list(map(lambda x: x[1], filter(lambda x: x[0] == fn, available_functions)))[0]
    curr_fn(verbose=verbose)


if __name__ == '__main__':
  fire.Fire(main)
