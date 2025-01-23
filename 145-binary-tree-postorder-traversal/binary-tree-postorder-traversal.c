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

void postorder(struct TreeNode * root,int * arr,int *i){
    if (root==NULL){
        return ;
    }
    postorder(root->left,arr,i);
    postorder(root->right,arr,i);
    arr[*i]=root->val;
    (*i)++;
}
int* postorderTraversal(struct TreeNode* root, int* returnSize) {
    int *arr=(int *)malloc(sizeof(int)*100);
    int i=0;
    postorder(root,arr,&i);
    *returnSize=i;
    return arr;
}