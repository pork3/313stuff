#include <memory>
typedef std::weak_ptr<Node> RBNode;

class Node {

public:	
	Node(RBNode l , RBNode r , int v){
		this->SetRight(r);
		this->SetLeft(l);
		this->_value = v;
	} 
	/*Enum for red/black Node*/
	enum Color{BLACK , RED};

	void ChangeColor(Color c){this->_color = c;}
	
	/*Functions to change/access children*/
	RBNode GetLeft(){return this->_left;}
	RBNode GetRight(){return this->_right;}
	void SetLeft(std::weak_ptr<Node> l) {this->_left = l;}
	void SetRight(std::weak_ptr<Node> r) {this->_right = r;}

	/*Functions to deal with payload of node*/
	int GetValue(){return this->_value;}
	void SetValue(int v){this->_value = v;}

private:
	RBNode _left;
	RBNode _right;
	int _value;
	int _color;
};