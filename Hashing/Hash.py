
class Hash():
    A = float( (5**(0.5) -1 )/2)
    M = 2 ** 14
    
    def Division(self, key, Prime):
        return (key % Prime)
    
    def Multiplication(self, key):
        return int( self.M * ( (key * self.A ) % 1))

if __name__ == "__main__":
    key = int( input() )
    Hashing = Hash()
    print( Hashing.Division(key, 701))
    print( Hashing.Multiplication(key))
    
        