#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

int main(void){
    std::ifstream inputFile("input.txt");
    std::string line;

    if (!inputFile){
        return 1;
    }
    int data[6][5];

    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 5; ++j) {
            inputFile >> data[i][j];
        }
    }

    inputFile.close();


    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            std::cout << data[i][j] > data[i+1][j];
        }
        std::cout << std::endl;
    }
    return 0;
}
