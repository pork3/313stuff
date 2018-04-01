#include <iostream>
#include <string>
#include "RedBlackTree.h"

int main(int argc , char** argv){

	RedBlackTree rbt;
	rbt.Insert(15);
	rbt.Insert(3);
	rbt.Insert(8);
	rbt.Insert(7);
	rbt.Insert(22);
	rbt.Insert(30);
	rbt.Insert(14);
	rbt.Insert(4);
	rbt.Insert(7);
	rbt.PrintRoot();

	rbt.SearchTree(4);
	//std::cout << r << std::endl;

	return 1; 
}