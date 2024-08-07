
class Euclids:
    @staticmethod
    def gcd(a, b):
        while True:
            if a == 0 or b == 0:
                break
            a, b = a % b, b % a
            r = b + a
        return r
    
    @staticmethod
    def gcdx(a, b):
        if a == 0:
            return b, 0, 1
        r = b % a
        r, x1, y1 = Euclids.gcdx(r, a)
        x = y1 - (b // a) * x1
        y = x1
        return r, x, y
      
