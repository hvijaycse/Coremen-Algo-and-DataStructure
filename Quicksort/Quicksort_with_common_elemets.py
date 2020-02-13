class QuickSort() : 
    
    def __init__(self, Start, End, Array):
        self.Array = Array
        self.Start = Start
        self.End = End
    
    def Swap(self, Index_1, Index_2):
        Temp =  self.Array[ Index_1]
        self.Array[ Index_1 ] = self.Array[ Index_2 ]
        self.Array[ Index_2 ] = Temp
        return
            
    def Partition(self, Start, End ):
        
        if Start < End:
            Index = Start - 1
            last = self.Array [ End ]
            for Position in range( Start, End ):
                if self.Array[ Position] < last:
                    Index = Index + 1
                    self.Swap( Index, Position)
                    
                if self.Array[ Position] > last:
                    Index =  Position -1
            
            if Index != Start -1:
                self.Swap( Index + 1, End)
            else:
                return (Start + End )//2
        else :
            Index = Start - 1
        return Index + 1
        
    def Sort(self,  Start, End ):
        if Start < End :
            q = self.Partition( Start, End)
            self.Sort( Start, q-1 )
            self.Sort( q+1, End )
            
        return self.Array

if __name__ == "__main__":
    print("Enter the length of array to be sorted")
    Count = int( input() )
    print( "Enter the elements ")
    array = list( map( int, input().strip().split() ))
    Quick = QuickSort( 0, Count - 1, array )
    array = Quick.Sort( 0, Count -1)
    print( 'Sorted Array \n', array )
    
    
                 