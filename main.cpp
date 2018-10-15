#include <iostream>

using std::cout;
using std::endl;

const int ROW = 6;
const int COL = 7;

void reset(int[ROW][COL]);
void display(int[ROW][COL]);

int main() {
    char board[ROW][COL];
    reset(board);
    display(board);
    return 0;
}

void reset(int board[ROW][COL]){
    for (int r = 0; r < ROW; r++) {
        for (int c = 0; c < COL; c++) {
            board[r][c] = ' ';
        }
    }
}

void display(int board[ROW][COL]) {
    for (int r = 0; r < ROW; r++) {
        for (int c = 0; c < COL; c++) {
            cout << board[r][c];
        }
        cout << endl;
    }
}