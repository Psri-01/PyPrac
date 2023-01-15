def is_even(number):
  if number%2==0:
    return True
  return False
'''there is no else block because after exec return statements the function exits, so the code that follows doesn't get executed.
detailed explanation:
when a return statement is executed, the function exits so that the code that follows doesn't get executed. 
This means that if the number is even, the computer will reach the return true statement and exit the function. 
Anything that comes after that will only be executed if the condition in the if statement was false. 
In other words, once the function reaches the return false line, we know for sure that the if condition was false which means the number was odd.'''
