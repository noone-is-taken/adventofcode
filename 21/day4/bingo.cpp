//bingo problem!
//i have the numbers that the bingo will output and then the differents cards
//i need to find the first card to win and then sum all non selected numbers and 
//multiply that number by the last number that was given

#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

class BingoNumb{
	public:
		int num;
		bool selected;
};

int main(){
	ifstream myFile;
	myFile.open("inputexample.txt");
	vector<int> numerosBingo;
	string line;
	vector<BingoNumb[][5]> cards;
	BingoNumb bingoCards[5][5];
	cards.push_back(bingoCards);
	if(myFile.is_open()){
		getline(myFile,line);
		string number = "";
		for(int i=0; i<line.length();i++){
			if(line[i] == ','){
				int n = stoi(number);
				numerosBingo.push_back(n);
				number = "";
			}else
				number += line[i];
		}
		while(getline(myFile,line)){
			//read file	
		}
	}
	return 0;
}

