
/**
 * Write a description of class sudoku here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class sudoku
{
    // instance variables - replace the example below with your own
   static int numOfTries;

    /**
     * Constructor for objects of class sudoku
     */
    public static void main(String args[])
    {
        numOfTries=0;
        int[][] a = {
            {0,0,0,0,0,1,0,0,0},
            {0,0,0,2,0,4,0,1,0},
            {0,0,3,6,5,0,4,0,0},
            {0,0,0,0,4,0,0,3,0},
            {0,6,0,0,0,0,5,0,0},
            {0,8,0,9,0,6,0,0,0},
            {4,0,7,5,0,0,0,0,0},
            {0,0,0,0,9,0,0,2,0},
            {0,0,0,0,8,0,1,0,0},    
        };
        System.out.println("Initial Puzzle is:");
        printPuzzle(a);
        solve(a,0,0);
    }

   
    public static void solve(int[][] puzzle, int row, int col)
    {
        
        if(col>8){
            row++;
            col = 0;
        }
        if(row>8){
            System.out.println("\nSolution is:");
            printPuzzle(puzzle);
            System.exit(0);
        }
        
        if(puzzle[row][col]==0){
            for(int i = 1;i<10;i++){
            if(isValid(puzzle,i,row,col)){
                
             puzzle[row][col] = i;
             solve(puzzle,row,+1);
            }
        }
        puzzle[row][col] = 0;
        }
        else{
            solve(puzzle,row,col+1);
        }
    }
    
    public static boolean isValid(int[][] puzzle, int number, int row, int col){
        for(int i = 0;i<9;i++){
            if(puzzle[row][i]==number)
            return false;
            if(puzzle[i][col]==number)
            return false;
        }
        int colsector = (col/3)*3;
        int rowsector = (row/3)*3;
        for(int i = 0;i<3;i++){
        for(int j = 0;j<3;j++){
            if(puzzle[rowsector+i][colsector+j]==number)
            return false;
        }}
        return true;
        
        
    }
    public static void printPuzzle(int[][] p){
        for(int i = 0;i<9;i++){
        for(int j = 0;j<9;j++){
            System.out.print(p[i][j]+" ");
    }
    System.out.println();
}
}
}
