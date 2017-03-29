#!/usr/bin/python
import sys

class stringcombo:
    def lettercombo(self,digits):
        print "digits is: " + digits
        myKeyMap = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",
                    "7":"pqr","8":"tuv","9":"wxyz"}
        if len(digits) == 0: return [""]
        if len(digits) == 1: return list(myKeyMap[digits])
        mapping = self.lettercombo(digits[:-1])
        append = myKeyMap[digits[-1]]
        print mapping
        print append
        return [a + b for a in mapping for b in append]


def main():
    digits = sys.argv[1]
    c = stringcombo()
    print c.lettercombo(digits)
    
if __name__ == "__main__":
    main()

