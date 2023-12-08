#include <iostream> //cout

using namespace std;

int main(int argc, char const *argv[])
{

	cout << argc << endl;
	cout << &argv[2] << endl;
	cout << *argv;
	if(argc > 1){
		cout << *argv[2];
		cout << *argv[1];
		cout << *argv[3];
	}
	return 0;
}
