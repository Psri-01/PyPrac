def max_value(values_on_cards, no_of_people):
    values_on_cards.sort()
    max_val = 0   
    for i in range(no_of_people):
        new_val = i
        if new_val > max_val:
            max_val = new_val
    return max_val
values_on_cards = [5, 1, 2, 3, 4]
no_of_people = len(values_on_cards)
result = max_value(values_on_cards, no_of_people)
print(result)

def find_max_tip(ai, bi, no_of_integers, X, Y):   
    differences = [(ai[i] - bi[i], i) for i in range(no_of_integers)]   
    differences.sort(reverse=True)   
    total_tip = 0
    for diff, idx in differences:
        if X > 0 and (Y <= 0 or ai[idx] >= bi[idx]):
            total_tip += ai[idx]
            X -= 1
        else:
            total_tip += bi[idx]
            Y -= 1
    return total_tip
ai1 = [11, 2, 3, 4, 5]
bi1 = [15, 4, 3, 2, 11]
no_of_integers1 = 5
X1 = 3
Y1 = 3
output1 = find_max_tip(ai1, bi1, no_of_integers1, X1, Y1)  
ai2 = [14, 6, 3, 7, 2, 4]
bi2 = [15, 3, 4, 2, 3, 7]
no_of_integers2 = 6
X2 = 4
Y2 = 3
output2 = find_max_tip(ai2, bi2, no_of_integers2, X2, Y2)  

import sys
input_from_question=input()
def solution(input_from_question):
  lt=input().split(' ')
  ltn=[]
  for i in lt:
    ltn.append(int(i))
  a=max(ltn)
  ltn.remove(a)
  b=max(ltn)
  ltn.remove(b)
  c=max(ltn)
  ltn.remove(c)
  return a+b+c
print(solution(input_from_question))
