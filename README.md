#  LeetCode & Data Science Journey

<!-- Технологические бейджи -->
![Python](https://shields.io)
![LeetCode](https://shields.io)
![Data Science](https://shields.io📊-blue?style=for-the-badge)

Hi! I'm a first-year **Information Systems and Technologies (IS&T)** student at MADI. I have a strong passion for mathematics, linear algebra, and I am consistently moving towards **Data Science and Artificial Intelligence (AI)**.

* **Core Language:** Python 🐍
* **Focus Areas:** Algorithms, Matrix Operations & Statistical Computing

This repository serves as a collection of my algorithmic solutions from LeetCode. My goal is not just to find a working solution, but to optimize the code to its limits and connect programming with a solid mathematical foundation.

## 📊 LeetCode Achievements
* **Max Execution Speed:** Beats 100.00% ⚡
* **Memory Optimization:** Beats 99.03% 🧠

## 📁 Repository Structure

### 🔢 Linear Algebra & Matrices (2D Arrays)
* [x] **867. Transpose Matrix** ([`Matrix/Transpose_Matrix.py`](./Matrix/Transpose_Matrix.py)) — Transposing rectangular and square matrices. Fully optimized using raw memory indices.
* [x] **1572. Matrix Diagonal Sum** ([`Matrix/Matrix_Diagonal_Sum.py`](./Matrix/Matrix_Diagonal_Sum.py)) — Calculating the sum of primary and secondary diagonals in a single $O(N)$ loop, handling the overlapping central element.

### 📐 Basic Algorithms & Arrays
* [x] **1. Two Sum** ([`Hash_Map/Two_Sum.py`](./Hash_Map/Two_Sum.py)) — Finding a pair of numbers that add up to a specific target.
* [x] **88. Merge Sorted Array** ([`Array_String/Merge_Sorted_Array.py`](./Array_String/Merge_Sorted_Array.py)) — Efficient merging of two sorted arrays.

---
*Pumping up engineering skills while listening to Kai Angel's new album. Never stopping, never settling!* 🔥


## 🟢 27. Remove Element

### 📝 Problem Description
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

### 💡 Solution Approach
This solution uses an **optimized Pythonic approach** with slice assignment (`nums[:]`). By using a list comprehension inside a slice, we filter out all occurrences of `val` and overwrite the original array directly in memory. This satisfies the strict **in-place** modification requirement enforced by the LeetCode testing environment without changing the object's reference ID.

### 💻 Code
```python
class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        return len(nums)
```

### 📊 Complexity Analysis
- **Time Complexity:** $O(N)$ — where $N$ is the length of the array. We iterate through the array once to filter the elements.
- **Space Complexity:** $O(N)$ — temporary space is used by the list comprehension before writing the values back into the original slice.


