enum Color{BLACK , RED};

class Node {
//typedef std::shared_ptr<Node> RBNode;

public:	
	Node(Node* l , Node* r , Node* p,  int v, Color c){
		this->SetRight(r);
		this->SetLeft(l);
		this->SetParent(p);
		this->value = v;
		this->color = c; 
	} 
	/*Enum for red/black Node*/
	

	void ChangeColor(Color c){this->color = c;}
	
	/*Functions to change/access children*/
	Node* GetLeft(){return this->left;}
	Node* GetRight(){return this->right;}
	void SetLeft(Node* l) {this->left = l;}
	void SetRight(Node* r) {this->right = r;}
	void SetParent(Node* p) {this->parent = p;}

	/*Functions to deal with payload of node*/
	int GetValue(){return this->value;}
	void SetValue(int v){this->value = v;}

private:
	
	Node* left;
	Node* right;
	Node* parent; 
	int value;
	Color color;
	friend class RedBlackTree;
};