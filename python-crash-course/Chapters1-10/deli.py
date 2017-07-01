sandwich_orders = ['ham and cheese', 'pastrami', 'pb & j', 'pastrami', 'blt', 'turkey club', 'pastrami', 'buffalo chicken']
finished_sandwiches = []
print('Oh no, the deli has ran out of pastrami!')
while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')
for order in sandwich_orders:
  print('I just made your ' + order.title() + ' sandwich.')
  finished_sandwiches.append(order)
print('Finished sandwiches: ')
for sandwich in finished_sandwiches:
  print(sandwich.title())
