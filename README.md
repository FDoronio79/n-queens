The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. There are 92 solutions. The problem was first posed in the mid-19th century. In the modern era, it is often used as an example problem for various computer programming techniques.

The n-queens puzzle is the same problem but on any board of n rows and n columns.

You should have a function named find_positions(n) that takes the size of the n by n board and returns a list of the rows of the queen in each column, if a solution exists, otherwise returns None.

For example, here's one potential solution for a 4x4 board.

The result for this would be this zero-based list of positions for that arrangement in the previous image.

How to approach this problem
There are three main parts to this problem:

How to model the chessboard
How to determine if a position is "safe" for a given column
Figuring out the loops
There are a lot of solutions for this on the Web. If you get stuck, you may want to try to find one, read it, close it, then adapt what they showed you from memory.

Modeling the chessboard
Because the chessboard is an n by n matrix, a good way to model this is to build an n by n list. We know how to do this in  time using nested loops.

You can start off by putting 0 values in all of the places in the list of lists which would represent no queens on the board.

A value of 1 in one of the positions in the list of lists would indicate that a queen is on the board.

Determining if a position is safe
You have to search the row and diagonals to determine if the queen is "safe", that is, there is no other queen in the same row or diagonal as the queen being placed.

You can search your square list that you created to model the chessboard to find out if another queen is in the same row or diagonal as the queen you're trying to place.

Search the same row to see if there's a 1 in the row. If there is, it is not a safe move.
Search the two diagonals from the current row-column position to see if there's a 1 in either diagonal. If there is, it is not a safe move.
Figuring out the loops
This is really the meat of the problem. You want to start at the first column, then loop over each row to find out if its a safe position. If it is, mark the position with a "1" in the list of lists that is your board. Move to the next column, loop over the rows, and find a safe place.

If you get to a position where there are no safe moves, then you have to "unwind" your choices to that point and try, again.

Eventually, even the brute force method will solve this for small boards of size 4 or 5.

Try to get that working for a small board of 4 or 5. Then, try 6 and see if you can make it run faster.

Solution
We will release a solution for the N-Queens problem, tomorrow.