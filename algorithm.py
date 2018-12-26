
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

class Prime():
  def __init__(self, n):
    self.n= n

  # time complexity: O(m) m= ( int(n**0.5) )/2
  def check(self):
    n= self.n
    if n<=1: return False
    if n==2 or n==3: return True

    if n%2==0: return False  # <=3 or even number

    max_n= int(n**0.5)+1
    for i in range(3, max_n, 2):   # only odd numbers
      if n%i==0: return False
    return True

if __name__ == '__main__':
    n= 100

    primes= []
    for i in range(-3, 100):
      if Prime(i).check(): primes.append(i)
    print (primes)





  


  
  



