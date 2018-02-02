/*********************************************************
 * Copyright (c) 2018 Jeff Lund
 * Prints out a binary search tree in pre-order, in-order
 * and post-order traversals
 *********************************************************/
#include <stdio.h>
#include <stdlib.h>

// Node struct for BST
typedef struct node {
    int val;
    struct node *left;
    struct node *right;   
} node;

// Creates and returns a new node
node* createNode(int v) {
    node *temp = malloc(sizeof(node));
    temp->left = NULL;
    temp->right = NULL;
    temp->val = v;
    return temp;
} 

// Inserts a value into a BST
void insert(node *root, int v) {
    if(v == root->val)
        return;
    else if(v < root->val) {
        if(root->left == NULL) {
            root->left = createNode(v);
            return;
        }
        else
            insert(root->left, v);
    }
    else { // v > root->val
        if(root->right == NULL) {
            root->right = createNode(v);
            return;
        }
        else
            insert(root->right, v);
    }
}

// Prints out pre order traversal of BST
void preOrder(node* root) {
    printf("%d ", root->val);
    if(root->left != NULL)
        preOrder(root->left);
    if(root->right != NULL)
        preOrder(root->right);
}

// Prints out in order traversal of BST
void inOrder(node *root) {
    if(root->left != NULL)
        inOrder(root->left);
    printf("%d ", root->val);
    if(root->right != NULL)
        inOrder(root->right);
}

// Prints out post order traversal of BST
void postOrder(node *root) {
    if(root->left != NULL)
        postOrder(root->left);
    if(root->right != NULL)
        postOrder(root->right);
    printf("%d ", root->val);
}

int main(void) {
    int value;
    FILE *fp = fopen("test", "r");
    fscanf(fp, "%d", &value);
    node *root = createNode(value);

    while(fscanf(fp, "%d", &value) != EOF) {
        insert(root, value);
    }

    printf("Pre order traversal: ");
    preOrder(root);
    printf("\nIn order traversal: ");
    inOrder(root);
    printf("\nPost order traversal: ");
    postOrder(root);
    printf("\n");

    return 0;
}
