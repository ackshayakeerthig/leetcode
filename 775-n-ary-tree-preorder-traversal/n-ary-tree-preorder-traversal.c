/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void preorder1(struct Node * root, int * arr, int * i){
    if (root==NULL){return;}
    arr[(*i)++]=root->val;
    for (int j=0;j<root->numChildren;j++){
        preorder1(root->children[j],arr,i);
    }
    return;
}
int* preorder(struct Node* root, int* returnSize) {
    int *arr=(int *)malloc(sizeof(int)*10000);
    int i=0;
    preorder1(root,arr,&i);
    *returnSize=i;
    return arr;
}