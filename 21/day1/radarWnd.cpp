#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream myFile;
    myFile.open("input.txt");
    int sumAnt = INT32_MAX, sumAct, sum = 0;
    int n1,n2,n3, numLines = 0;
    if(myFile.is_open()){
        string line;

        getline(myFile,line);
        n1 = stoi(line);
        getline(myFile,line);
        n2 = stoi(line);
        getline(myFile,line);
        n3 = stoi(line);

        sumAnt = n1+n2+n3;

        while(getline(myFile,line)){
            n1 = n2;
            n2 = n3;
            n3 = stoi(line);
            sumAct = n1 + n2 + n3;
            //cout << n3 << endl;
            if(sumAct > sumAnt)
                sum++;
            sumAnt = sumAct;
            //cout << n3 << endl;
        }
    }
    cout << sum;
    myFile.close();
    return 0;
}