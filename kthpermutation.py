def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n -1)
def find_kth_permutation(v, k, result):
  if not v:
    return
  n = len(v)
  # count is number of permutations starting with first digit
  count = factorial(n - 1)
  selected = (k - 1) #count
  result += str(v[selected])
  del v[selected]
  k = k - (count * selected)
  find_kth_permutation(v, k, result)
def get_permutation(n, k):
  v = list(range(1, n + 1))
  result = []
  find_kth_permutation(v, k, result)
  return ''.join(result)
def main():
  n = factorial(4)
  for i in range(1, n + 1):
    print(str(i) + "th permutation = \t", get_permutation(4, i))
main()

'''If input vector is empty return result vector
block_size = (n-1)! ['n' is the size of vector]
Figure out which block k will lie in and select the first element of that block
(this can be done by doing (k-1)/block_size )
Append selected element to result vector and remove it from original input vector
Deduce from k the blocks that are skipped i.e k = k - selected*block_size and goto step 1'''
