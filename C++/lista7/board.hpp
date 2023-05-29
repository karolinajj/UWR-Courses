#pragma once

#include <vector>
using namespace std;

namespace gameboard 
{

    class Board 
    {
        public:
            Board(int size); //constructor

            int get_size() const;
            bool is_valid_move(int row, int col) const;
            bool is_full() const;
            bool wins() const;
            bool player_wins(int player) const;
            void make_move(int row, int col,int player);
            
            vector<vector<int>> get_board() const;

        private:
            const int size;
            vector<vector<int>> board;
    };

} 
