#include <stdlib>
#include "redblack.h"

int tree_max(Node* root){
	while (root!= NULL){
		root = root->right;
	} return root->value; 
}
/*change to void to handle exceptions*/
int tree_min(Node* root){
	while (root!=NULL){
		root = root->left;
	} return root->value;
}

/* Normal bst insert, then correect if needed*/
void insert(Node* root , int val){
	Node* iNode = malloc(sizeof(Node));
	iNode->value = val;
	Node* tNode = NULL;
	Node* pNode = root;

	while(pNode != NULL){
		tNode = pNode;
		if(iNode->value < pNode->value)
			pNode = pNode->left;
		if(iNode->value > pNode->value)
			pNode = pNode->right;
	}
	iNode->parent = tNode;
	if(tNode == NULL)
		/*maybe make color black*/
		root = iNode;
	else if (iNode->value < tNode->value)
		tNode->left = iNode;
	else
		tNode->right = iNode;
	iNode->left = NULL;
	iNode->right = NULL;
	iNode->color = RED;
	redblack_insert_fix(root , iNode);
}

/*function to maintain the redblack property(*/
void redblack_insert_fix(Node* root , Node* iNode){
	while(iNode->parent->color == RED){
		if(iNode->parent == iNode->parent->parent->left){
			Node* y = iNode->parent->parent->right;
			if(y->color == RED){
				iNode->parent->color = BLACK;
				y->color = BLACK;
				iNode->parent->parent->color = RED;
				iNode = iNode->parent->parent;
			} else{
				if(iNode == iNode->parent->right){
					iNode = iNode->parent;
					left_rotate(root , iNode);
				}
				iNode->parent->color = BLACK;
				iNode->parent->parent->color = RED;
				right_rotate(root , iNode->parent->parent);
			}
		}
		else{
			Node* y = iNode->parent->parent->left;
			if(y->color ==  RED){
				iNode->parent->color = BLACK;
				y->color = BLACK;
				iNode->parent->parent->color = RED;
				iNode = iNode->parent->parent;
			} else {
				if (iNode == iNode->parent->left){
					iNode = iNode->parent;
					right_rotate(root , iNode);
				}
				iNode->parent->color = BLACK;
				iNode->parent->parent->color = RED;
				left_rotate(root , iNode->parent->parent);
			}
		}
	}
	root->color = BLACK;
}

void left_rotate(Node* root , Node* iNode){
	Node* y = iNode->right;
	iNode->right = y->left;
	if(y->left !=NULL)
		y->left->parent = iNode;
	y->parent = iNode->parent;
	if(iNode->parent == NULL)
		root = y;
	else if (iNode->parent->left == iNode)
		iNode->parent->left = y;
	else
		iNode->parent->right = y;
	y->left = iNode;
	iNode->parent = y;
}

void right_rotate(Node* root , Node* iNode){
	Node* y = iNode->left;
	iNode->left = y->right;
	if(y->right !=NULL)
		y->right->parent = iNode;
	y->parent = iNode->parent;
	if(iNode->parent == NULL)
		root = y;
	else if (iNode->parent->left == iNode)
		iNode->parent->left = y;
	else
		iNode->parent->right = y;
	y->right = iNode;
	iNode->parent = y;
}