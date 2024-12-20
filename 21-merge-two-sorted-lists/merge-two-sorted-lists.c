/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 typedef struct ListNode * NODE;
 NODE getnode(){
    return (NODE)malloc(sizeof(struct ListNode));
 }
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    NODE  l3=NULL,temp1=l1,temp2=l2;
    NODE end=NULL;
    while (temp1!=NULL && temp2!=NULL){
        
        NODE newnode=getnode();
        if (temp1->val > temp2->val){
            newnode->val=temp2->val;
            temp2=temp2->next;
        }
        else if (temp1->val <= temp2->val){
            newnode->val=temp1->val;
            temp1=temp1->next;
        }
        newnode->next=NULL;
        if (end==NULL){
            l3=newnode;}
        else {end->next=newnode;}
        end=newnode;
    }
    NODE temp=(temp1==NULL)?temp2:temp1;
    while (temp!=NULL){
        NODE newnode=getnode();
        newnode->val=temp->val;
        newnode->next=NULL;
        if (end==NULL){
            l3=newnode;}
        else{
        end->next=newnode;}
        end=newnode;
        temp=temp->next;
    }
    return l3;
}