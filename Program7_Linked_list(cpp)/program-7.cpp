/*Department of Computer Engineering has student's club named 'Pinnacle Club'. Students of Second,
third and final year of department can be granted membership on request. Similarly, one may cancel the
membership of club. First node is reserved for president of club and last node is reserved for secretary
of club.
Write C++ program to maintain club member‘s information using singly linked list. Store student PRN
and Name. Write functions to
a) Add and delete the members as well as president or even secretary.
b) Compute total number of members of club
c) Display members
d) Display list in reverse order using recursion
e) Two linked lists exists for two divisions. Concatenate two lists
f) Merge two sorted singly linked lists.*/

#include<iostream>
using namespace std;

struct Node{
    int prn;
    string name;
    struct Node* next;
};

class club{
    public:
    struct Node *head=NULL, *end=NULL,*temp=NULL,*a;
    void President(){
        head=new Node;
        cout<<"Enter the name of President:";
        string name;
        cin>>name;
        head->name=name;
        cout<<"Enter the prn of President:";
        int prn;
        cin>>prn;
        head->prn;
        head->next=NULL;   
    }
    void Secretary(){
        end=new Node;
        cout<<"Enter the name of Secretary:";
        string name;
        cin>>name;
        end->name=name;
        cout<<"Enter the prn of Secreatary:";
        int prn;
        cin>>prn;
        end->prn=prn;
        end->next=NULL;
        head->next=end;
    }
    club(){
        President();
        Secretary();
    }
    void add_member(){
        temp=new Node;
        cout<<"Enter the name of Member:";
        string name;
        cin>>name;
        temp->name=name;
        cout<<"Enter the prn of Member:";
        int prn;
        cin>>prn;
        temp->prn=prn;
        a=head;
        while(a->next!=end){
            a=a->next;
        }
        a->next=temp;
        temp->next=end;
    }
    void delete_member(int prn){
        if(head->prn==prn){
            head=head->next;
        }else{
            int condition=0;
            a=head;
            while(a->next!=NULL){
                if (a->prn==prn){
                    condition=1;
                    
                }
            }
        }
    }
};

int main(){
    club c;
    c.create_head(12,"in");
    c.display();
    return 0;
}