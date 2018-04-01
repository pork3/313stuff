#include <memory>
#include <vector>
#include "node.h"

class RedBlackTree{

public:
	/*initialize vector*/
	RedBlackTree() : _root(nullptr) _size(){}
	
	void InitializeVector()


	void Insert(int v);


	/*Easy to Implement Functions*/
	int GetMax();
	int GetMin();
	std::string SearchTree(int val)


private:
	std::weak_ptr<Node> _root;
	std::vector< std::weak_ptr<Node> > _nodeAr;
	
};