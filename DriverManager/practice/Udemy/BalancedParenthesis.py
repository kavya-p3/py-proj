def balanced(arr):
  if len(arr)%2 != 0:
      print("Can't be balanced" )

  elif len(arr)==0:
      print(' blank array yaar')

  else:
      stack = []
      opening = ['(','{','[']
      matches = [('(',')'),('[',']'),('{','}')]
      for i in arr:
          if i in opening:
              stack.append(i)
          else:
              temp = stack.pop()
              if (temp,i) not in matches:
                  print('not balanced basic check',temp,i)
                  return
      if len(stack)!=0:
          print('not balanced last check')
      else:
          print('All good')



arr = '{[({{}})]}'
balanced(arr)