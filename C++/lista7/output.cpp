#include "output.hpp"
#include <iostream>
using namespace std;
using namespace gameboard;
using namespace gameAi;

namespace output
{
    Game::Game(){}

    void Game::Start()
    {
        int board_size;
        bool tmp = true;
        while(tmp)
        {
            cout << "Enter board size (3 or 4): ";
            cin >> board_size;

            if(board_size != 3 and board_size != 4)
            {
                clog << "Error! The chosen board size is incorrect. Please choose 3 or 4. ";
            }
            else tmp = false;
        }

        tmp = true;
        int order = 1;
        
        while(tmp)
        {
            cout << "Do you wnat to play first or second?: (type 1 or 2)";
            cin >> order;
            if(order != 1 and order != 2) clog << "Error! The chosen order is incorrect. Please choose 1 or 2.";
            else tmp = false;
        }
        Board board(board_size);
        play(board, order%2); //order%2 beacause in play the order is 0 or 1;
    }

    void Game::display(const Board& board)
    {
        const int size = board.get_size();

        cout << endl << "  ";
        for(int i = 0; i < size; i++)
        {
            cout << (char)('A' + i) << " ";
        }
        cout << endl;

        for(int i = 0; i < size; i++)
        {
            cout << i+1 << " ";
            for(int j = 0; j < size; j++)
            {
                if(board.get_board()[i][j] == 0) //ai
                {
                    cout << "O ";
                }
                else if(board.get_board()[i][j] == 1) //player
                {
                    cout << "X ";
                }
                else
                {
                    cout << "- ";
                }
            }
            cout << endl;
        }
    }

    bool Game::correct_field(string field, int size) //a1 A1 1a 1A
    {
        if(field.size() > 2) return false;
        int row, col;

        if(isdigit(field[0]) && isalpha(field[1])) //1a 1A
        {
            row = field[0] - '1';
            col = toupper(field[1]) - 'A';
            
        }
        else if (isdigit(field[1]) && isalpha(field[0])) //a1 A1
        {
            row = field[1] - '1';
            col = toupper(field[0]) - 'A';
        }
        else return false;
        if(col < 0 || col > size - 1) return false;
        if (row < 0 || row > size - 1) return false;

        return true;
        
    }

    void Game::play(Board board,int order)
    {
        int size = board.get_size();
        string field;
        int player = 1;
        
        for(int i = 0; i < size*size; i++)
        {
            if(i % 2 != order) //player makes a move
            {
                display(board);
                cout << endl << "Which field do you choose? ";
                cin >> field;

                if(!correct_field(field, size))
                {
                   clog << "Error! You entered inccorect name of a field. The correct format is for example A1.";
                   i-=1;
                   continue;
                }
                else 
                {
                    int row, col;
                    if(isalpha(field[0])) //A1 or a1
                    {
                        col = toupper(field[0]) - 'A';
                        row = field[1] - '1';
        
                    }
                    else //1a or 1A
                    {
                        col = toupper(field[1]) - 'A';
                        row = field[0] - '1';
                    }
                    
                    if(board.is_valid_move(row,col))
                    {
                        board.make_move(row,col, player);
                    }
                    else
                    {
                        clog << "Error! You have chosen not an empty field. Please try again.";
                        i-=1;
                        continue;
                    }
                }
            }
            else //ai makes a move
            {
                ai_move(board);
            }

            if(board.wins())
            {
                display(board);
                if(board.player_wins(0)) cout << "\nUnfortunatley, you lost the game.";
                else cout << "\nCongratulations! You won the game.";
                return;
            }
        }
        cout << "End of the game. No one won.";
    }
}