/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return build(nums, 0, nums.size());
    }
    TreeNode* build(vector<int>& nums, int left, int right) {
    
    if (left == right) return nullptr;
    int max_idx = left;
    for (int i = left + 1; i < right; ++i) {
        if (nums[i] > nums[max_idx]) max_idx = i;
    }
    TreeNode* root = new TreeNode(nums[max_idx]);
    root->left = build(nums, left, max_idx);
    root->right = build(nums, max_idx + 1, right);

    return root;
}
};