from replit import clear
#HINT: You can call clear() to clear the output in the console.
bid_list={}
run=True
while run:
  name=input('Name of bidder: ')
  bidvalue=int(input('Enter bid amount: '))
  bid_list[name]=bidvalue
  repeat=input('''Is there any other bidder
  'Type' 'Y' or 'N': ''').upper()
  if repeat=='Y':
    clear()
  else:
    run=False
list_amount=[]
for i in bid_list:
  list_amount+=[bid_list[i]]
max_amount=max(list_amount)
winner=[name for name, bidvalue in bid_list.items() if bidvalue==max_amount]
won=winner[0]
print(f'so the winner of this bid is {won}')