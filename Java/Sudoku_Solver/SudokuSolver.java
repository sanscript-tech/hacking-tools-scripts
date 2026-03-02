package sudoku;

import java.util.*;

public class SudokuSolver {
	
	// N=9 as there will be 9 rows and 9 colums
	static int N = 9; 
	
	static boolean solveSudoku(int grid[][], int row, int col) {
		// if we cross the last cell then we return true to avoid further back-tracking
		if (row == N - 1 && col == N) 
            return true; 
		// if we reach the last column then we move to the next row after setting col as 0
		if (col == N)  
        { 
            row++; 
            col = 0; 
        } 
		// check whether the cell is 0 and if it is not 0 then we move to the next column for further processing
		if (grid[row][col] != 0) 
            return solveSudoku(grid, row, col + 1); 
		
		// check if a no from 1 to 0=9 can be placed in a given row and column
		for(int no=1;no<10;no++) {
			if (isSafe(grid,row,col,no)) {
				// assigning no to the cell assuming it be correct
				grid[row][col] = no;
				
			// then go for the next column assuming the no assigned is correct	
			if (solveSudoku(grid,row,col+1))
				return true;	
			}
			// if the assumption is wrong assign 0 to the cell
			grid[row][col] = 0; 
		}
		return false;
	}
	
	static boolean isSafe(int grid[][], int row, int col,int num) {
		// return false if the given num is found in the column
		for (int i=0;i<8;i++) {
			if (grid[i][col]==num)
				return false;
		}
		
		// return false if the given num is found in the row
		for (int i=0;i<8;i++) {
			if (grid[row][i]==num)
				return false;
		}
		// check if num is present in the 3*3 matrix
		int startRow = row -(row%3);
		int startColumn = col -(col%3);
		for(int i=0;i<3;i++) {
			for(int j=0;j<3;j++) {
				if (grid[i+startRow][j+startColumn]==num)
					return false;
			}
		}
		return true;
	}
	
	// display the solved sudoku
	static void print(int[][] grid) {
		System.out.println("Solved Sudoku");
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++)
				System.out.print(grid[i][j]+" ");
			System.out.println();
		}
	}
 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int[][] grid = new int[N][N];
		System.out.println("Enter the Sudoku to be solved");
		// enter the matrix
		for(int i=0; i<N;i++) {
			for(int j=0;j<N;j++) {
				grid[i][j]=sc.nextInt();
			}
		}
		// check if solution exists
		if(solveSudoku(grid,0,0))
			print(grid);
		else
			System.out.println("Solution does not exist");
	}

}
