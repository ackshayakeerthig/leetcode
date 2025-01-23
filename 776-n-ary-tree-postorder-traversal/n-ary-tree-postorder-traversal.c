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

void postorder1(struct Node * root, int * arr, int * i){
    if (root==NULL){return;}
    for (int j=0;j<root->numChildren;j++){
        postorder1(root->children[j],arr,i);
    }
    arr[(*i)++]=root->val;
    return;
}
int* postorder(struct Node* root, int* returnSize) {
    int *arr=(int *)malloc(sizeof(int)*10000);
    int i=0;
    postorder1(root,arr,&i);
    *returnSize=i;
    return arr;
}