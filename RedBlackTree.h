#include <memory>
#include <vector>
#include "Node.h"

class RedBlackTree{

public:
	/*initialize vector*/
	RedBlackTree() : root(nullptr) {}
	//~RedBlackTree(); //do a traversal of tree (in sorted order) and del not 


	/*Insert Functions */
	void Insert(int val);


	/*Remove Functions*/
	void Transplant(Node* node, Node* node2);
	void Remove();

	/*Easy to Implement Functions*/
	int GetMax();
	int GetMin();
	void searchHelper(Node* n , int val);
	void SearchTree(int val);


	void PrintRoot();

private:
	Node* root;
	std::vector<Node*> nodeAr;

	/*helper functions to maintain RB Tree*/
	void RedInsertFix(Node* n);
	void LeftRotate(Node* n);
	void RightRotate(Node* n);
	
};