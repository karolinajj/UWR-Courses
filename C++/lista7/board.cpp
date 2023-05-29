#include "board.hpp"
#include <iostream>
#include<vector>
using namespace std;

//-1 if a cell is empty, 0 if circle, 1 if cross
namespace gameboard 
{

    Board::Board(int size) : size(size), board(size, vector<int>(size)) 
    {
        for(int i = 0; i < size; i++)
        {
            for(int j = 0; j < size; j++)
            {
                board[i][j] = -1;
            }
        }
    }

    int Board::get_size() const 
    {
        return size;
    }

    bool Board::is_valid_move(int row, int col) const 
    {
        return row >= 0 && row < size && col >= 0 && col < size && board[row][col] == -1;
    }

    bool Board::is_full() const 
    {
        for (int i = 0; i < size; i++) 
        {
            for (int j = 0; j < size; j++)
            {
                if (board[i][j] == -1)
                {
                    return false;
                }
            }
        }
        return true;
    }

    bool Board::wins() const 
    {
        return player_wins(0) || player_wins(1);
    }

    bool Board::player_wins(int player) const 
    {
        for (int row = 0; row < size; row++) //rows
        {
            bool is_winning_line = true;
            for (int col = 0; col < size; col++) 
            {
                if (board[row][col] != player) 
                {
                    is_winning_line = false;
                    break;
                }
            }
            if (is_winning_line) 
            {
                return true;
            }
        }

        for (int col = 0; col < size; ++col) //columns
        {
            bool is_winning_line = true;
            for (int row = 0; row < size; ++row) 
            {
                if (board[row][col] != player) 
                {
                    is_winning_line = false;
                    break;
                }
            }
            if (is_winning_line) 
            {
                return true;
            }
        }

        bool is_winning_line = true;
        for (int i = 0; i < size; i++) //diagonal
        {
            if (board[i][i] != player) 
            {
                is_winning_line = false;
                break;
            }
        }
        if (is_winning_line) 
        {
            return true;
        }

        is_winning_line = true; //anti-diagonal
        for (int i = 0; i < size; i++) 
        {
            if (board[i][size - 1 - i] != player) 
            {
                is_winning_line = false;
                break;
            }
        }
        if (is_winning_line) 
        {
            return true;
        }

        return false;
    }

    void Board::make_move(int row, int col, int player) 
    {
        board[row][col] = player;
    }

    std::vector<std::vector<int>> Board::get_board() const 
    {
        return board;
    }

} 
