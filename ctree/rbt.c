#include <stdlib.h>

#include "redblack.h"

#define BLACK 0
#define RED 1


typedef struct RedBlackTree{
	Node* root;
} RedBlackTree;

Node* find(Node* root , int val){
	if (root == NULL)
		printf("Need to handle exception");
	if(root->value == val)
		return root;
	if (val < root->value)
		return find(root->left, val);
	else
		return find(root->right, val);
}

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

void transplant(Node* root, Node* xNode , Node* yNode){
	if(xNode->parent == NULL)
		root = yNode;
	else if (xNode == xNode->parent->left)
		xNode->parent->left = yNode;
	else
		xNode->parent->right = yNode;
	yNode->parent = xNode->parent;
}

void delte_fix(Node* root, Node* dNode){
	while(dNode!= root && dNode->color == BLACK){
		if(dNode == dNode->parent->left){
			Node* y = dNode->parent->right;
			if(y->color == RED){
				y->color = BLACK;
				dNode->parent->color = RED;
				left_rotate(root, dNode->parent);
				y = y->parent->right;
			}
			if (y->left->color == BLACK && y->right->color == BLACK){
				y->color = RED;
				dNode = dNode->parent;
			} else{
				if(y->right->color == BLACK){
					y->left->color = BLACK;
					y->color = RED;
					right_rotate(root , y);
					y = y->parent->right;
				}
				y->color = dNode->parent->color;
				dNode->parent->color = BLACK;
				y->right->color = BLACK;
				left_rotate(root , dNode->parent);
				dNode = root;
			}

		} else{
			Node* y = y->parent->left;
			if(y->color == RED){
				y->color = BLACK;
				dNode->parent->color =  RED;
				right_rotate(root, dNode->parent);
				y = dNode->parent->left;
			}if (y->left->color == BLACK && y->right->color == BLACK){
				y->color = RED;
				dNode = dNode->parent;
			}
			else{

				if(y->left->color == BLACK){
					y->right->color = BLACK;
					y->color = RED;
					left_rotate(root , y);
					y = dNode->parent->left;
				}
				y->color = dNode->parent->color;
				dNode->parent->color = BLACK;
				y->left->color = BLACK;
				right_rotate(root, dNode->parent);
				dNode = root;
				}
			}
	}
	dNode->color = BLACK;
}

void delte(Node* root , int val){
	Node* dNode = search(root , val);
	if (dNode == NULL)
		return;
	
}


int main(int argc , char** argv){



	//free here
	return 0;
}