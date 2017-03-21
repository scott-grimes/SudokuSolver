def solve(puzzle, row, col):
    #recursive soduku solver
    #given a row and column position r/c, iterate the value in r/c until a fit
    #is found, then then call solve on the next column
     
    #reached the end of the row, move on to the next one
    if(col>8): 
        row+=1
        col = 0;
     
    #reached the final slot (row 8, column 8), we must be done!
    if(row>8):  
        print "\nSolution is:"
        printPuzzle(puzzle)
        exit(0)
     
    #iterate the value in the current cell
    if(puzzle[row][col] is 0): 
        for i in range(1,10):  
            
            #call solve with the next cell if our value in r/c is valid
            if(isValid(puzzle,i,row,col)): 
                puzzle[row][col] = i       
                solve(puzzle,row,col+1)
                    
        #if this cell has been iterated 9 and further cells kept kicking back,
        #reset the cell and return to a previous one
        puzzle[row][col] = 0; 
                              
    else:
        #cell was filled in from the start of our problem, skip it!
        solve(puzzle,row,col+1) 

     
#is the current number valid? checks the row, column, and 3x3 cell to make sure 
#the number is not duplicated
def isValid(puzzle, number, row, col):
    
        #if the number is already in our row/col, return false
        for i in range(0,9):    
            if(puzzle[row][i]==number):
                return False;
            if(puzzle[i][col]==number):
                return False;
        
        #if the number is in our 3x3 cell already, return false
        colsector = (col//3)*3  
        rowsector = (row//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if(puzzle[rowsector+i][colsector+j] is number):
                    return False
        
        return True;
         
         
#prints out a puzzle row by row
def printPuzzle(p):
        for row in p :
                print row
        print "\n"


#start of our program

#define the starting values, 0 is a blank space
a = [
    [0,0,0,0,0,1,0,0,0], \
    [0,0,0,2,0,4,0,1,0], \
    [0,0,3,6,5,0,4,0,0], \
    [0,0,0,0,4,0,0,3,0], \
    [0,6,0,0,0,0,5,0,0], \
    [0,8,0,9,0,6,0,0,0], \
    [4,0,7,5,0,0,0,0,0], \
    [0,0,0,0,9,0,0,2,0], \
    [0,0,0,0,8,0,1,0,0]]

print "Initial Puzzle is:"
printPuzzle(a)

#call our solver with the first cell at [0,0]
solve(a,0,0)
