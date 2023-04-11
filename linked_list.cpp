#include<iostream>
using namespace std;

class node
{
   public:
   int data;
   node * next;

   node(int d)
   {
      this->data=d;
      this->next=NULL;
   }
};
void Insert_Athead(node *& head,int data)
{
     node * temp = new node(data);
     temp->next=head;
     head=temp;
}

void Insert_Attail(node *& tail,int data)
{
     node * temp = new node(data);
     tail->next=temp;
     tail=temp;
}
void Insert_Atposition(node * & tail,node *& head,int position,int data)
{
    int count=1;
    node * temp=head;

    if(position==1)
    {
      Insert_Athead(head,data);
      return ;
    }
    while(count < position-1)
    {
      
      temp=temp->next;
      count ++;
    }
    
    if(temp->next==NULL)
    {
      Insert_Attail(tail,data);
      return ;
    }
    node * temp1= new node(data);

    temp1->next=temp->next;
    temp->next=temp1;
}
void print(node *& head)
{
   node * temp =head;

   while(temp!=NULL)
   {
      cout << temp->data << " ";
      temp = temp->next;
   }

   cout << endl;
}
void Deletion_of_node(node *& tail,node *& head,int position)
{
   int count=1;
   int count1=1;
   node * temp=head;
   node * temp1=head;
   
   if(position==1)
   {
      head=temp->next;
      return ;
   }

   while(count < position-1)
   {
      temp=temp->next;
      count++;
   }

   while(count1 <= position-1)
   {
      temp1=temp1->next;
      count1++;
   }
   

   if(temp1->next==NULL)
   {
   tail->data=temp->data;
   }

   temp->next=temp1->next;

}
void Deletion_Athead(node * &tail,node *&head)
{
   node * temp=head;
   head=temp->next;
   return ;
}

void Deletion_Attail(node *& tail,node *& head)
{
   if (head == tail) {
       delete tail;
       head = NULL;
       tail = NULL;
       return;
   }
   
   node *temp = head;
   while (temp->next != tail) {
       temp = temp->next;
   }
   
   temp->next = NULL;
   delete tail;
   tail = temp;

}
int main()
{
   
   node * node1 = new node(10);


   node * head=node1;
   node * tail=node1;

   print(head);
   
   Insert_Attail(tail,12);
   print(head);
   
   Insert_Athead(head,6);
   print(head);
   Insert_Attail(tail,15);
   print(head);

  Insert_Atposition(tail,head,3,14);
  print(head);
  
  Insert_Athead(head,4);
   print(head);
  Insert_Atposition(tail,head,5,19);
  print(head);

  Insert_Atposition(tail,head,6,21);
  print(head);
  cout << "Head is:"<<head->data<<endl;
  cout << "Tail is:"<<tail->data<<endl<<endl;

  Deletion_of_node(tail,head,6);
  print(head);
  cout << "Head is:"<<head->data<<endl;
  cout << "Tail is:"<<tail->data<<endl;
 
 Deletion_Athead(tail,head);
 print(head);
 cout << "Head is:"<<head->data<<endl;
 cout << "Tail is:"<<tail->data<<endl;
 
 Deletion_Attail(tail,head);
  print(head);
 cout << "Head is:"<<head->data<<endl;
 cout << "Tail is:"<<tail->data<<endl;
  
   return 0;
}
