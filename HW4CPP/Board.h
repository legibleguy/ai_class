#include <vector>

using namespace std;

enum BoardSign{
    EMPTY,
    X,
    O
};

class Board{

    public:

    Board(int width, int height);

    int GetCellAtDir(const int FromPoint, const int DeltaX, const int DeltaY);

    void SetCellValue(int Idx, BoardSign Value) {if(Idx >= 0 && Idx < Values.size()) Values[Idx] = Value;}

    vector<int> GetCellsWithSign(BoardSign Sign);

    int GetNumCellsWithSign(BoardSign Sign);

    char GetValueAsCharAt(int At){
        if (At < 0 || At >= Values.size()) return ' ';
        switch (Values[At])
        {
        case EMPTY :
            return ' ';
        
        case X :
            return 'X';
        case O:
            return 'O';

        default:
            return ' ';
        };
    }

    private:

    void SequenceCheck(int AtCell, BoardSign WithSign);
    int GetSeqDirection(int InSeq);

    int Width, Height;
    vector<int> Values;
    vector< vector<int> > Sequences;
};