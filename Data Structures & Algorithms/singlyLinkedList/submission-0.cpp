class Node {
    int value;
    Node *next = nullptr;

public:
    Node(int val, Node *new_next = nullptr): value(val), next(new_next) {}

    void setNext(Node *new_next) {
        next = new_next;
    }

    Node *getNext() {
        return next;
    }

    int getValue() {
        return value;
    }
};

class LinkedList {
    Node *head = nullptr;
    Node *tail = nullptr;
    int size;
public:
    LinkedList(): head(nullptr), tail(nullptr), size(0) {}

    int get(int index) {
        if (index >= size || !head) return -1;
        
        Node *temp = head;
        for (int count = 0; count < index; count++) {
            if (!temp) return -1;
            temp = temp->getNext();
        }
        
        return temp ? temp->getValue() : -1;
    }

    void insertHead(int val) {
        Node *new_head = new Node(val, head);
        head = new_head;

        if(!tail) tail = head;

        size += 1;
    }

    void insertTail(int val) {
        Node *new_tail = new Node(val);
        if(!head) {
            head = tail = new_tail;
        } else {
            tail->setNext(new_tail);
            tail = new_tail;
        }
        size++;
    }

    bool remove(int index) {
        if(index >= size || !head) return false;

        Node *temp = head;

        if (index == 0) {
            head = head->getNext();
            delete temp;
            size--;
            if(size == 0) tail = nullptr;
            return true;
        }

        for (int i = 0; i < index - 1; i++) {
            if (!temp || !temp->getNext()) return false;
            temp = temp->getNext();
        }

        Node *toDelete = temp->getNext();
        if(!toDelete) return false;

        temp->setNext(toDelete->getNext());
        if(toDelete==tail) tail=temp;
        delete toDelete;
        size--;
        return true;
    }

    vector<int> getValues() {
        vector<int> values;
        int index = 0;
        Node *temp = head;
        while(temp) {
            values.push_back(temp->getValue());
            temp = temp->getNext();
        }
        return values;
    }
};

