#include <vector>
#include <iostream>
#include "RedBlackTree.h"

int RedBlackTree::GetMin(){
	Node* tmin;
	if(root == nullptr){
		std::cout << "Empty" << std::endl;
	} else {
		tmin = this->root;
		while( tmin->left != nullptr){
			tmin = tmin->left;
		}
	}
	return tmin->value;
}

int RedBlackTree::GetMax(){
	Node* tmax;
	if( this->root == nullptr){
		std::cout << "Empty" << std::endl;
		//handle exceptions
	}else{
		Node* tmax = this->root;
		while(  tmax->right != nullptr){
			tmax = tmax->right;
		}
	}
	return tmax->value;
}

void RedBlackTree::SearchTree(int val){
	if (this->root == nullptr){
		std::cout << "NotFound";
	} else{
		searchHelper(this->root , val);
	}
}

void RedBlackTree::searchHelper(Node* n, int val){

	if (n == nullptr){
		std::cout << "NotFound" << std::endl;
	} else if (n->value == val){
		std::cout << "Found" << std::endl;
	} else{
		if (n->value > val){
			searchHelper(n->left , val);
		} else{
			searchHelper(n->right , val);
		}
	}
}

void RedBlackTree::Insert(int val){
	/*create a red node by default*/
	Node* insertNode = new Node(nullptr,nullptr,nullptr,val,RED);

	Node* parent = nullptr;
	Node* node = this->root;
	while(node != nullptr){
		parent = node;
		if (insertNode->value < node->value){
			node = node->left;
		} else {
			node = node->right;
		}
	}
	insertNode->parent = parent;
	if (parent == nullptr){

		this->root = insertNode;
	} else if (insertNode->value < parent->value){
		parent->left = insertNode;
	} else {
		parent->right = insertNode;
	}
	RedInsertFix(insertNode);
}

/*helper function to maintailn redblack property*/
/*(seg faulting here... ) check for null ptr dereference*/
void RedBlackTree::RedInsertFix(Node* n){
	Node* parent = nullptr;
	Node* grandNode = nullptr;

	std::cout << n->value << std::endl;
	/*breaks on fourth iteration*/
	while(this->root !=n && n->color != BLACK && n->parent->color == RED){

		grandNode = n->parent->parent;

		if(n->parent == grandNode->left)
		{	
			/*uncle is red, recolor needed nodes*/
			Node* uncle = grandNode->right;
			if(uncle != nullptr && uncle->color == RED){
				grandNode->color = RED;
				n->parent->color = BLACK;
				uncle->color = BLACK;
				n = grandNode;
				} else {
					if (n == n->parent->right){
						//LeftRotate(n);
						/*double check logic*/
						parent = n->parent;
						n = parent;
						parent = n->parent;
					}
					//RightRotate(n);
					Color p = grandNode->color;
					grandNode->color = parent->color;
					parent->color = p; 
			}
		}else{
			/*uncle is re*/
			Node* uncle = grandNode->left;
			if (uncle != nullptr && uncle->color == RED){
				grandNode->color = RED;
				n->parent->color = BLACK;
				uncle->color = BLACK;
				n = grandNode;
				} else {
					if(n == n->parent->left){
						//RightRotate(n);
						parent = n->parent;
						n = parent;
						n->parent = parent->parent;
					}
					//LeftRotate(n);
					Color p = grandNode->color;
					grandNode->color = parent->color;
					parent->color = p;
					n = n->parent;
				}
			}
	}
	this->root->color = BLACK;
}

void RedBlackTree::LeftRotate(Node* n){
	Node* node = n->right;
	n->right = n->left;
	if(node->left != nullptr){
		this->root = node;
	} else if ( n->parent == n->parent->left){
		n->parent->left = node;
	} else {
		n->parent->right = node;
	}
	node->left = n;
	n->parent = node;
}

void RedBlackTree::RightRotate(Node* n){
	Node* node = n->left;
	n->left = node->right;
	if(node->right !=nullptr){
		this->root = node;
	} else if(n->parent == n->parent->right){
		n->parent->right = node;
	} else {
		n->parent->left = node;
	}
	node->right = n;
	n->parent = node;

}










void RedBlackTree::PrintRoot(){
	int value = this->root->value;
	std::cout << value <<  " " << this->root->color  << std::endl;

}

