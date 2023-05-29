#pragma once

#include "board.hpp"
using namespace gameboard;

namespace gameAi 
{
    int random_number(int max_value);
    vector<pair<int, int>> get_avaiable_moves(Board& board, int size);
    void ai_move(Board& board);
};
