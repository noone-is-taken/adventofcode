#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream myFile;
    myFile.open("filename.txt");
    int numAnt = INT32_MAX, numAct, sum = 0;
    if(myFile.is_open()){
        string line;
        while(getline(myFile,line)){
            numAct = stoi(line);
            if(numAct >= numAnt)
                sum++;
            numAnt = numAct;
        }
    }
    cout << sum;
    myFile.close();
    return 0;
}