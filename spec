One character for each board square
Board size of 7 columns, 6 rows
Players 'X' and 'L' take turns moving
Four of the same character in a row, column, or diagonal is a win
No placements above max row
Game is over when a player wins or the board is full
Bold the four winning characters and reprint the board
Add the ability to change the board dimensions

--------------------------------------------------------------------------------

miscellany:

Array of ~9 char arrays
    Each item initialized to ' '
    Move count
        if move count & 1 -> player one's move
                        else player two's move
    Check wins using pointer manipulation?
        Start checking after move 7
        left *p +1 +2 +3 +4
        down *p +9 +18 +27 +36
        diagonal *p +10 +19 +28 +37
        use a for loop, win when four in a row


