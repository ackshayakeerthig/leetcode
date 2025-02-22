/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    if (root==NULL){return 0;}
    if (root->left==NULL && root->right==NULL){return 1;}
    int c1=maxDepth(root->left);
    int c2=maxDepth(root->right);
    return (c1>c2)?c1+1:c2+1;
}