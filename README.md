## What is Knapsack?

There are many ways to describe the problem, but my favorite is to describe it as a thief robbing a store:
> Imagine a thief robbing a store with a bag of some capacity. The thief sees many items, and each item has a different value and weight. If he can only take one of each item, which items should he take to maximize his profit?


### Understanding the problem
What are some ways to solve this problem?

At first glance, the knapsack problem seems as if a greedy approach would be suitable. But, a greedy approach does not guarantee an optimal solution.

Let's look at a case where the greedy approach does not find an optimal solution.

| Item      | Weight    | Value     | Value/Weight |
| --------- | --------- | --------- | ------------ |
| A         | 3         | 16        | 5.33         |
| B         | 2         | 10        | 5            |
| C         | 2         | 10        | 5            |

Let's solve the problem for a capacity of 4.

Using the greedy approach, we would take item A since it has the highest value-weight ratio. After we take item A, we won't have space for other items.

But the optimal solution is to take items B and C.

This counterexample shows that the greedy approach is not always optimal. 

Can we solve knapsack with dynamic programming? Does the problem have the two dynamic programming properties?

## Solving 0/1 Knapsack
In the previous post we discussed that to solve dynamic programming problems, you need:
> 1. the problem defined as relatable subproblems
2. recurrence relation to relate the sub-solutions to the original solution
3. base cases for the recurrence relation

### 1. Problem as relatable subproblems
Let's identify the dynamic programming characteristics of the problem. Then, we can check if we can use dynamic programming.

#### Defining subproblems 
In the knapsack problem, we can choose to take or leave the item if the item fits into our knapsack. We need two variables to identify each choice (subproblem): the **item index** and the **remaining capacity**.

> **_Variable definitions:_** 
`i`: item index
`rc`: remaining capacity
`i_weight`: current item weight
`i_val`: current item value

We can define the subproblems to be `state(i, rc)`. The collection of subproblems is all instances of `state(i, rc)` where `0 <= i < num_items` and `0 < rc <= total_capacity`. The solution to each subproblem is the maximum profit  at `state(i, rc)`.

#### Optimal substructure
Can we construct the solution to `state(i, rc)` using smaller subproblems?

At item `i`, we have two choices: to include `i`, or to exclude `i`. If we choose to exclude `i`, the solution does not change from the previous item. If we choose to include `i`, we need to make room for the item weight and include the item. The larger of the two is the solution to `state(i, rc)`

Solution to `state(i, rc)` is the maximum of:
- `state(i-1, rc)` (exclude item `i`)
- `state(i-1, rc-i_weight) + i_val` (include item `i`)

We can use smaller subproblems to find the optimal solution.
So, the problem has the optimal substructure property.

#### Overlapping subproblems

We need to calculate the subproblems `state(i-1, rc)` and `state(i-1, rc-i_weight) + i_val` in almost every state.

So, the problem has the same subproblems, and the problem has the overlapping subproblems property.

### 2. Recurrence relation
We already found the recurrence relation above!

> ...maximum of:
- `state(i-1, rc)` (exclude item `i`)
- `state(i-1, rc-i_weight) + i_val` (include item `i`)

Finding the recurrence relation is usually the hardest part of the problem.
Here are some tips for finding the recurrence relation:
- How can we use smaller subproblems to solve larger subproblems?
- Does the problem ask for the min/max of something? If so, the recurrence relation is often the min/max of a subset of subproblems.

### 3. Base cases for the recurrence relation
When the problem is about finding the min/max of something, the base case value is usually 0.

The base case is:
> When `i` or `rc` is out of range, we return 0.

### Top-down approach
A simple way to think about the top-down approach is "DFS + memoization". If we do not need to solve all subproblems linearly, a top-down approach can be more efficient than a bottom-up approach

The three important parts are:
- function to solve a single subproblem
- DFS to traverse through the state-space tree
- data structure for memoization
- recurrence relation to relate the subproblems
- base cases for the recurrence relation

Here is a solution with comments using python.

gist: https://gist.github.com/alexhanbich/521edf2e7c485cc183759db1a12f94c0

#### Time complexity for top-down approach
Time complexity: O(NM) where N = num_items, M = capacity.
Space complexity: O(NM) where N = num_items, M = capacity.

### Bottom-up approach V1
A simple way to think about the bottom-up approach is filling out the table. The bottom-up approach does not use recursion, so there is no recursion overhead.

The important parts are
- table to keep to store solutions to subproblems (dimension = num_variable in each state)
- loop to fill out the table
- recurrence relation to relate the subproblems
- base cases for the recurrence relation

Here is a solution with comments using python.
gist: https://gist.github.com/alexhanbich/2d968eb60a07c06cb84eea5f187f2ccb

#### Time complexity for bottom-up approach V1
Time complexity: O(NM) where N = num_items, M = capacity.
Space complexity: O(NM) where N = num_items, M = capacity.

### Bottom-up approach V2
Can we reduce the space complexity? 

In the recurrence relation, we only access the previous and current row. We can use just two rows to solve knapsack.

Here is a solution with comments using python.

gist: https://gist.github.com/alexhanbich/eb25099259d2f46c98723be95d411b71

#### Time complexity for bottom-up approach V2
Time complexity: O(NM) where N = num_items, M = capacity.
Space complexity: O(M) where M = capacity.

### Bottom-up approach V3
Can we reduce the space complexity even more?

In the recurrence relation, we access the previous and current row. But, we only access columns to the left of the previous row. If we iterate the columns from the right, we can use a single row to solve knapsack.

gist https://gist.github.com/alexhanbich/9c0dce644bee97d7778a7fe5bd961b16

#### Time complexity for bottom-up approach V3
Time complexity: O(NM) where N = num_items, M = capacity.
Space complexity: O(M) where M = capacity.

## Comparing different methods
To test my algorithms, I used the 8 test cases from [here](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html). Test 8 is a fairly large test case where num_item = 24 and capacity = 6404180.

For fun, here is the execution time of each versions of knapsack.

| Knapsack function| Execution time|
| ---------------- | ------------- |
| Top-down         | 5.599s        |
| Bottom-up v1     | 33.246s       |
| Bottom-up v2     | 25.293s       |
| Bottom-up v3     | 19.063s       |

The reason why the top-down approach is so fast is that the weights(each 6 digits) and the capacity(7 digits) are large.

In this case, calculating for every single capacity is an overkill, since all weight values are 6 digits long.

The difference between the execution time of the bottom-up approaches is most likely from:
- creating different array sizes
- different number of conditionals
- unknown compiler optimizations

## Conclusion
Knapsack is a classic, but not an easy dynamic programming question. To solve dynamic programming questions, we need to identify the dynamic programming characteristics. When we identify them, we can find how the subproblems relate, and eventually lead to the recurrence relation.
