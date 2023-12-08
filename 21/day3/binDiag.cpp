#include <iostream>
#include <fstream>
#include <string>

using namespace std;
const int binSize = 12;
int binToEnter(int binArr[]){
    int r = 0, multp = 1;
    for (int i = binSize-1; i >= 0 ; i--)
    {
        r += binArr[i] * multp;
        multp *= 2;
    }
    
    return r;
}
int main(){
    ifstream myFile;

    myFile.open("input.txt");
    string line;
    
    int binari1[binSize] ;
    int binari0[binSize] ;
    int gamma[binSize] ;
    int epsilon[binSize] ;
    for (int i = 0; i < binSize; i++)
    {
        binari1[i] = 0;
        binari0[i] = 0;
        gamma[i] = 0;
        epsilon[i] = 0;
    }
    

    if(myFile.is_open()){
        while (getline(myFile,line))
        {
            for (int i = 0; i < line.length(); i++)
            {
                if(line[i] == '1')
                    binari1[i]++;
                else
                    binari0[i]++;
            }
            
        }
        for (int i = 0; i < binSize; i++)
        {
            if(binari0[i] < binari1[i])
                gamma[i] = 1;
            else
                epsilon[i] = 1;
            
        }
        cout << binToEnter(gamma)*binToEnter(epsilon);
    }
    return 0;
}