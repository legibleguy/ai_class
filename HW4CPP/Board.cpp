#include "Board.h"
#include <algorithm>

#define push_front(v,val) v.insert(v.begin(), 1, val);
#define pop_front(v)  if(!v.empty())v.erase(v.begin());

Board::Board(int width, int height){
    Width = width;
    height = height;
    Values = vector<int>(Width * Height, EMPTY);
}

vector<int> Board::GetCellsWithSign(BoardSign Sign){
    vector<int> res;
    for(int i =0; i < Values.size(); i++)
        if(Values[i] == Sign) res.push_back(i);
    return res;
}

int Board::GetNumCellsWithSign(BoardSign Sign){
    int res = 0;
    for(int i =0; i < Values.size(); i++)
        if(Values[i] == Sign) res++;
    return res;
}

vector<int> IndexToCoord(const int Index, const int BoardW){
    vector<int> Coord(2);
    Coord[0] = Index / BoardW;
    Coord[1] = Index % BoardW;
    return Coord;
}

int CoordToCell(const int Row, const int Col, const int BoardW){
    return (Row * BoardW) + Col;
}

int Board::GetCellAtDir(const int FromPoint, const int DeltaX, const int DeltaY){
    vector<int> AtCoord = IndexToCoord(FromPoint, Width);
    AtCoord[0] += DeltaY;
    AtCoord[1] += DeltaX;
    if(AtCoord[0] < 0 || AtCoord[0] >= Height) 
        return -1;
    else if(AtCoord[1] < 0 || AtCoord[1] >= Width)
        return -1;
    else
        return CoordToCell(AtCoord[0], AtCoord[1], Width);
}

void Board::SequenceCheck(int AtCell, BoardSign WithSign){
    vector<int> ModifiedSequences;
    for(int row = -1; row < 2; row++)
        for(int col = -1; col < 2; col++){
            if (row == 0 && col == 0) 
                continue;
            
            int neighbor = GetCellAtDir(AtCell, row, col);
            if (neighbor != -1 && Values[neighbor] == WithSign){
                bool NewSequence = true;

                int neighborsMin = min(AtCell, neighbor);
                int neighborsMax = max(AtCell, neighbor);

                for(int seq = 0; seq < Sequences.size(); seq++){
                    if(count(Sequences[seq].begin(), Sequences[seq].end(), neighbor)){
                        int Direction  = neighborsMax - neighborsMin;

                        if (AtCell > Sequences[seq][Sequences[seq].size()-1])
                            Sequences[seq].push_back(AtCell);
                        else if(AtCell < Sequences[seq][0]){
                            push_front(Sequences[seq], AtCell);
                        }
                        else
                            Sequences[seq].insert(Sequences[seq].begin() + Sequences[seq].size()-2, AtCell);
                        
                        NewSequence = false;
                        ModifiedSequences.push_back(seq);
                        break;
                    }
                }

                if (NewSequence){
                    Sequences.push_back(vector<int> (neighborsMin, neighborsMax));
                    ModifiedSequences.push_back(Sequences.size()-1);
                }
            }
        }

    vector<int> ToRemove;
    for (int seq : ModifiedSequences)
        for (int otherS : ModifiedSequences){
            if (seq == otherS) continue;
            bool TailIsHead = Sequences[seq][Sequences[seq].size()-1] == Sequences[otherS][0];
            bool SameDirection = GetSeqDirection(seq) == GetSeqDirection(otherS);
            if (TailIsHead && SameDirection){
                pop_front(Sequences[otherS]);
                ToRemove.push_back(otherS);
                Sequences[seq].insert(Sequences[seq].end(), Sequences[otherS].begin(), Sequences[otherS].end());
            }
        }
    
    sort(ToRemove.begin(), ToRemove.end());
    for (int i = ToRemove.size() - 1; i >= 0; i--)
        Sequences.erase(Sequences.begin()+ToRemove[i]);
}

int Board::GetSeqDirection(int Seq){
    int LastIdx = Sequences[Seq].size()-1;
    int MaxIdx = max(Sequences[Seq][LastIdx], Sequences[Seq][LastIdx-1]);
    int MinIdx = min(Sequences[Seq][LastIdx], Sequences[Seq][LastIdx-1]);
    return MaxIdx - MinIdx;
}

int main(){
    return 0;
}