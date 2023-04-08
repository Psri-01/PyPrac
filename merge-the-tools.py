import textwrap
def merge_the_tools(string, k):
    for i in textwrap.wrap(string, k):
        d=dict()
        print(''.join([d.setdefault(c,c)for c in i if c not in d]))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    '''This code is an implementation of a function called merge_the_tools() that takes a string string and an integer k as input.

The function merge_the_tools() first uses the textwrap.wrap() method to divide the string into substrings of length k.

Then, for each substring, the function creates a dictionary d and iterates over each character c in the substring. 
If c is not already in the dictionary, it is added as a key with the value of c. 
The character c is then appended to a list. The list is then joined into a string and printed.

The purpose of the function is to print out unique characters in each substring of length k. 
The function ensures that no character is repeated within the same substring.

The if __name__ == '__main__': block is a conditional statement that runs the code inside it only if the script 
is executed directly (as opposed to being imported as a module). 
It prompts the user to input a string and an integer and then calls the merge_the_tools() function with these inputs.'''
