# sum-palindrome
def main():
    k = [2,12,9]
    k = map(int,k)
    temp = str(sum(k))
    if temp == temp[::-1] :
      print "palindrome"
    else:
     print "not palindrome"

if __name__ == '__main__':
    main()
