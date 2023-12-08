
//life support = oxygen gen * co2 scrubber
//
//keep numbers selected by *bit criteria*
//if you only have one number left, stop; this is the rating
//otherwise repet considering the next bit to the right
//
//bitcriteria:
//-oxygen generator rating:most common value in current position
//if 0 aand 1 are equally common keep then 1
//-c-2 scrubber rating least common
//if 0 aand 1 are equally common keep then 0


// life support = 001000111101 = 573 
// oxygen generator = 101101010110 = 2902
//
#include <list>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

const int binSize = 6;

vector<int> ibuscaBinari(list<vector<int>> lst, int indx){
	vector<int> r;
	if(lst.size()==1){
		r = lst.front();
	}else{
		list<vector<int>> llista1;
		list<vector<int>> llista0;
		for(vector<int> v: lst){
			if(v[indx] == 1)
				llista1.push_back(v);
			else
				llista0.push_back(v);
		}

		if(llista1.size() >= llista0.size())
			r = ibuscaBinari(llista0, ++indx);
		else
			r = ibuscaBinari(llista1, ++indx);

	}
	return r;
}

vector<int> buscaBinari(list<vector<int>> lst){
	return ibuscaBinari(lst,0);
}


int main(){
	ifstream myFile;
	myFile.open("input.txt");
	string line;
	list<vector<int>> llistabin;

	

	if(myFile.is_open()){
		while(getline(myFile, line)){

			vector<int> v;

			for(int i = 0; i < line.length(); i++){
				string s;
			      	s = line[i];
				int n = stoi(s);
				v.push_back(n);
			}
			llistabin.push_back(v);
		}
	}
	vector<int> a;
       	a = buscaBinari(llistabin); 	
	//oxigen trobat :)
	cout << "result:" << endl;
	for(int i: a){
		cout << i;
	}

//	for(vector<int> v: llistabin){
//		for (int i: v){
//			cout << i;
//		}
//		cout << '\n';
//	}



	return 0;
}
