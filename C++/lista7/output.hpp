#pragma once
#include <vector>
#include<iostream>
using namespace std;

#include "board.hpp"
#include "AI.hpp"

using namespace gameboard;
using namespace gameAi;

namespace output
{
    class Game 
    {
        public:
            Game();
            void Start();
            void play(Board board, int order);
        private:
            void display(const Board& board);
            bool correct_field(string field, int size);

    };

} 