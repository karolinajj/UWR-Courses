#include "AI.hpp"
#include <iostream>
#include <vector>
using namespace std;
using namespace gameboard;

namespace gameAi
{
    int random_number(int max_value) 
    {
        srand(time(NULL));
        return rand() % max_value; // generate random number
    }

    vector<pair<int, int>> get_available_moves(Board& board, int size)
    {
        vector<pair<int,int>> result;
        for(int i = 0; i < size; i++)
        {
            for(int j = 0; j < size; j++)
            {
                if(board.get_board()[i][j] == -1)
                {
                    result.push_back(make_pair(i,j));
                }
            }
        }
        return result;
    }

    void ai_move(Board& board)
    {
        const int size = board.get_size();
        vector<pair<int, int>> available_moves = get_available_moves(board, size);

        while(true)
        {
           int index = random_number(available_moves.size());
           int row = available_moves[index].first;
           int col = available_moves[index].second;

            if(board.is_valid_move(row, col))
            {
                board.make_move(row, col, 0); //Ai is a player 0
                break;
            }
        }
    }

}

