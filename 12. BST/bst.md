# BST

BinarySearch -> Search Space divided by Half on every iteration
             -> O(logn)

BinarySearchTree -> For every Node these properties should satisfy
                    Left subtree node data is Greater
                    root.data > Left subtree data
                    Right subtree node data is Smaller
                    root.data < Right subtree data
                    This Criteria should apply for all Nodes

If IP -> me -1 aya ruk jaeo tree banana Generally

# Inorder Predessor/ Successor

Inorder Predessor -> Inorder traversal me node se pahle wala node
                  -> Node se Pahle wala Elements
                  -> Node ke left subtree me maximum value is predessor just xota with Node
                  -> Assume Left subtree should be exit if not exit than not found
                  -> this can be valid for some of Nodes
Inorder Successor -> Inorder traversal me node ke badd wala node
                  -> Node ke just vada elemnts nikalana haii
                  -> Exit in Right subtree minimum value in right subtree on Node
                  -> this can be valid for some of Nodes
Variation of deletion can be asked in BST


# Deletion in BST
4 Cases

1.Case: if node left and right is NULL
        make this node as None
2.Case: if left is NuLL and right is not NUll
        -> Its child should be linked to prev node
        -> return root.right
3. case: if left is not NULL and right is NULL
        -> return root.left
4. case: if node have both left and right not NULL
        -> delete iss tarike kare ki Tree BST hi rahe
        two - choices is here
        Replace root.data ko Inorder Predessor se
        Replace root.data ko Inorder Successor se
        copy that and delete node which one is copied

Height/Daimeter - Same logic ans binary tree

        








