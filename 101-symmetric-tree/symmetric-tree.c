// /**
//  * Definition for a binary tree node.
//  * struct TreeNode {
//  *     int val;
//  *     struct TreeNode *left;
//  *     struct TreeNode *right;
//  * };
//  */
 typedef struct TreeNode * NODE;
//  void inordertraversal(int * inorder,NODE root, int *n){
//     if (root==NULL){
//         inorder[*n]=-101;
//         *n=*n+1;
//         return;
//     }
//     if (root->left==NULL && root->right==NULL){
//         inorder[*n]=root->val;
//         *n=*n+1;
//         return;}
    
//     inordertraversal(inorder,root->left,n);
//     inorder[*n]=root->val;
//     *n=*n+1;
//     inordertraversal(inorder,root->right,n);
//  }
 
// //  void postodertraversal(int * postorder,NODE root, int *n2){
// //     if (root==NULL){
// //         // postorder[*n2]=-101;
// //         // *n2=*n2+1;
// //         return;}
// //     postodertraversal(postorder,root->left,n2);
// //     postodertraversal(postorder,root->right,n2);
// //     postorder[*n2]=root->val;
// //     *n2=*n2+1;
// //  }
// //  int checkpostorder(int * postorder, int n2){

// //  }
// //  int postorder[1000];
// int ispalindrome(int * inorder, int n){
//     int i=0,j=n-1;
//     while (i<j){
//         if (inorder[i++]!=inorder[j--]){
//             return 0;
//         }
//     }
//     return 1;
// }
// int inorder[1000];
// bool isSymmetric(struct TreeNode* root) {
//     int n=0,n2=0;
//     inordertraversal(inorder,root,&n);
//     // postodertraversal(postorder,root,&n2);
//     return ispalindrome(inorder,n);
// }
bool check(NODE leftsub, NODE rightsub){
    if (leftsub==NULL && rightsub==NULL){return true;}
    else if (leftsub==NULL || rightsub==NULL){return false;}
    if (leftsub->val!=rightsub->val){return false;}
    return check(leftsub->left,rightsub->right)&& check(leftsub->right,rightsub->left);
}
bool isSymmetric(struct TreeNode* root) {
    if (root==NULL){return  true;}
    return check(root->left,root->right);
}