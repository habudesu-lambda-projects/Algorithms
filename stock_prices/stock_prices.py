#!/usr/bin/python

import argparse

def find_max_profit(prices):
  buyIndex = 0
  sellIndex = 1

  for i in range(2, len(prices)):
    
    if prices[i] > prices[sellIndex]:
      sellIndex = i
      k = buyIndex + 1
      while k < sellIndex:
        if prices[k] < prices[buyIndex]:
          buyIndex = k
        k += 1
    
  return prices[sellIndex] - prices[buyIndex]



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))