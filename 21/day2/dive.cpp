#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream myFile;
    myFile.open("input.txt");
    string line;
    int horizontal = 0, depth = 0;
    if(myFile.is_open()){


        while (getline(myFile,line))
        {
            //cout << line << '\n';
            if(line.find("forward") != string::npos){
                horizontal += stoi(line.substr(line.length()-2));
            }else if(line.find("down")!=string::npos){
                depth += stoi(line.substr(line.length()-2));
            }else{
                depth -= stoi(line.substr(line.length()-2));
            }
        }
        
    }
    cout << depth * horizontal << '\n';
    return 0;
}