#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream myFile;
    myFile.open("example.txt");
    string line;
    int horizontal = 0, depth = 0, aim = 0, forward;
    if(myFile.is_open()){


        while (getline(myFile,line))
        {
            if(line.find("forward") != string::npos){
                forward = stoi(line.substr(line.length()-2));
                horizontal += forward; 
                depth += aim * forward;
            }else if(line.find("down")!=string::npos){
                aim += stoi(line.substr(line.length()-2));
            }else{
                aim -= stoi(line.substr(line.length()-2));
            }
        }
        
    }
    cout << depth * horizontal << '\n';
    return 0;
}