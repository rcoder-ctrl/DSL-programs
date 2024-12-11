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
e) Two linked lists exists for two divisions. Concatenate two lists*/

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
        head->prn=prn;
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
        int count=count_members();
        if(count==0){
            cout<<"There exist no member in club";
        }else if(count==1){
            if(head->prn==prn){
                head=NULL;
                cout<<"Item deleted";
            }else{
                cout<<"member not found";
            }
        }else if(count==2){
            if(head->prn==prn){
                head=end;
                cout<<"Item Deleted";
            }else if(end->prn==prn){
                head->next=NULL;
                cout<<"Item deleted";
            }else{
                cout<<"Member not found";
            }
        }else if(count>2){
            if(head->prn==prn){
                head=head->next;
                cout<<"Item Deleted";
            }else if(head->next->prn==prn){
                head->next=head->next->next;
                cout<<"Item deleted";
            }else{
                a=head;
                int condition=0;
                while(a->next->next!=NULL){
                    if(a->next->next->prn==prn){
                        a->next->next=a->next->next->next;
                        cout<<"Item deleted";
                        condition=1;
                    }else{
                        a=a->next;
                    }
                }
                if(condition==0){
                    cout<<"Member not found";
                }
            }
        }
    }
    int count_members(){
        a=head;
        int count=0;
        if(a!=NULL){
            count++;
            while(a->next!=NULL){
                count++;
                a=a->next;
            }
        }
        return count;
    }
    void display(){
        a=head;
        while(a->next!=NULL){
            cout<<a->prn<<":"<<a->name<<"->";
            a=a->next;
        }
        cout<<a->prn<<":"<<a->name;
    }
    void display_reverse(Node *a,Node *b){
        Node *c=a;
        while(c->next!=b){
            c=c->next;
        }
        cout<<b->prn<<":"<<b->name<<"->";
        display_reverse(a,c);        
    }
    void contactenation(Node *connection){
        temp->prn=00;
        temp->name="new division";
        temp->next=connection;
        end->next=temp;
        display();
    }
};

int main(){
    cout<<"Welcome to club control program\n";
    int choice;
    char clubname;
    cout<<"Lets create clubs A and B\n";
    club A,B;
    cout<<"Enter corresponding choices as per requirement\n1:To add members in club\n2:To Delete members\n3:To calculate total number\n4:To Display\n5:To Display in reverse\n6:To add to lists\n7:exit\n";
    while(true){
        cout<<"\nEnter your choice:";
        cin>>choice;
        if(choice==1){
            cout<<"Enter the clubname:";
            cin>>clubname;
            if(clubname!='A' and clubname!='B'){
                cout<<"Invalid clubname\n";
            }else{
                if(clubname=='A'){
                    A.add_member();
                }else if(clubname=='B'){
                    B.add_member();
                }
            }
        }else if(choice==2){
            cout<<"Enter the clubname:";
            cin>>clubname;
            if(clubname!='A' and clubname!='B'){
                cout<<"Invalid clubname\n";
            }else{
                cout<<"Enter prn:";
                int prn;
                cin>>prn;
                if(clubname=='A'){
                    A.delete_member(prn);
                }else if(clubname=='B'){
                    B.delete_member(prn);
                }
            }
        }else if(choice==3){
            cout<<"Enter the clubname:";
            cin>>clubname;
            if(clubname!='A' and clubname!='B'){
                cout<<"Invalid clubname\n";
            }else{
                int count;
                if(clubname=='A'){
                    count=A.count_members();
                }else if(clubname=='B'){
                    count=B.count_members();
                }
                cout<<"Count of members is:"<<count;
            }
        }else if(choice==4){
            cout<<"Enter the clubname:";
            cin>>clubname;
            if(clubname!='A' and clubname!='B'){
                cout<<"Invalid clubname\n";
            }else{
                if(clubname=='A'){
                    A.display();
                }else if(clubname=='B'){
                    B.display();
                }
            }
        }else if(choice==5){
            cout<<"Enter the clubname:";
            cin>>clubname;
            if(clubname!='A' and clubname!='B'){
                cout<<"Invalid clubname\n";
            }else{
                if(clubname=='A'){
                    A.display_reverse(A.head,A.end);
                }else if(clubname=='B'){
                    B.display_reverse(B.head,B.end);
                }
            }
        }else if(choice==6){
            A.contactenation(B.head);
        }else if(choice==7){
            exit(0);
        }else{
            cout<<"Invalid input";
        }
    }
    return 0;
}