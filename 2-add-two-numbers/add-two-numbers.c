/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 typedef struct ListNode * NODE;
 NODE getnode(int item){
    NODE newnode= (NODE)malloc(sizeof(struct ListNode));
    newnode->val=item;
    newnode->next=NULL;
    return newnode;
 }
NODE insertend(NODE first, int item){
    NODE newnode=getnode(item);
    if (first==NULL){return newnode;}
    NODE temp=first;
    while (first->next!=NULL){
        first=first->next;
    }
    first->next=newnode;
    return temp;
}
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    NODE l3=NULL;
    int sum=0,carry=0;
    while (l1!=NULL && l2!=NULL){
        sum=(l1->val+l2->val+carry)%10;
        carry=(l1->val+l2->val+carry)/10;
        l3=insertend(l3,sum);
        l1=l1->next;
        l2=l2->next;
    }
    NODE l=(l1==NULL)?l2:l1;
    while (l!=NULL){
        sum=(l->val+carry)%10;
        carry=(l->val+carry)/10;
        l=l->next;
        l3=insertend(l3,sum);
    }
    if (carry){l3=insertend(l3,carry);}
    return l3;
}