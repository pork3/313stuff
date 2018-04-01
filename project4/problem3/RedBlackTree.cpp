#include <vector>
#include "RedBlackTree.h"
#include "Node.h"

typedef std::weak_ptr<Node> RBNode;

int RedBlackTree::GetMin(){
	if(this->_root == nullptr){
		std::cout << "Empty" << std::endl;
	} else {
		RBNode min = this->root;
		while( min->left != nullptr){
			min = min->left;
		}
	}
	return min._value;
}

int RedBlackTree::GetMax(){
	if( this->_root == nullptr){
		std::cout << "Empty" << std::endl;
		//handle exceptions
	}else{
		RBNode max = this->root;
		while(  max->right != nullptr){
			max = max->right;
		}
	}
	return max._value;
}

std::string RedBlackTree::SearchTree(int val){
	if (this->root == nullptr){
		retstr 
	}
	RBNode node = this->root;
	if(node._value > )
}