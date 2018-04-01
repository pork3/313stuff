/*all declares for redblacktree*/

typedef struct Node{
	/*Node children/parent pointers*/
	struct Node* left;
	struct Node* right;
	struct Node* parent;
	int value;
	int color;
} Node;


int tree_max(Node* root);
int tree_min(Node* root);
void insert(Node* root , int val);
void redblack_insert_fix(Node* root , Node* iNode);
void left_rotate(Node* root , Node* iNode);
void right_rotate(Node* root , Node* iNode);
