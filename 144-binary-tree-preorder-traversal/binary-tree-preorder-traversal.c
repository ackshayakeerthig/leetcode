/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void preorder(struct TreeNode * root,int * arr,int *i){
    if (root==NULL){
        return ;
    }
    arr[*i]=root->val;
    (*i)++;
    preorder(root->left,arr,i);
    preorder(root->right,arr,i);
}
int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    int *arr=(int *)malloc(sizeof(int)*100);
    int i=0;
    preorder(root,arr,&i);
    *returnSize=i;
    return arr;
}