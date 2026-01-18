# Binary Search Template

## Basic Structure

### Standard Binary Search for "Find Target"
```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```


### Standard Binary Search for "Range Convergence"
```python
def findBoundary(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] < nums[m + 1]: # this can be any condition eg, compared with nums[r], isBadVersion(m), etc.
            l = m + 1
        else:
            r = m
    return l
```

### Find first and last position
Keep searching when we found the target. And trust the process (`while l <= r:`) as we keeps changing `l` or `r` so it will eventually breaks the while loop.

1. The Shifting Window
The key to avoiding an infinite loop is ensuring that the distance between l and r decreases in every single iteration.

To find the leftmost: When nums[m] == target, you save the index and then set r = m - 1.

To find the rightmost: When nums[m] == target, you save the index and then set l = m + 1.

Because you are moving a pointer past the current mid, the range [l, r] is guaranteed to get smaller. Eventually, l will become greater than r, and the while l <= r condition will naturally break.

## Common Patterns

### 1. Search in Sorted Array
```python
def search_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 2. Search in Rotated Array
```python
while l <= r:
    m = (l + r) // 2

    # Check if nums[m] is target
    if nums[m] == target:
        return m

    # when nums[m] is not target
    # Check which side is sorted.
    if nums[l] <= nums[m]: # Left is sorted, Right is not
        if nums[l] <= target < nums[m]:
            r = m - 1
        else:
            l = m + 1
    else: # nums[l] > nums[m]. Right is sorted, Left is not
        if nums[m] < target <= nums[r]:
            l = m + 1
        else:
            r = m - 1
```
The Core Logic: Which side is "Normal"?
In a standard binary search, you check if target is greater or smaller than the mid point. In a rotated array, you first have to figure out which half of your current range is actually sorted.

e.g.,
[4, 5, 6, 7, 8, 1, 2, 3]

* If `mid` is 7, then left is normal, right is abnormal
* If `mid` is 6, same thing
* If `mid` is 1, then left is abnormal, right is normal
---
Here is why we need both comparisons and the specific use of <=.

1. Why Two Comparisons? (`nums[l] <= target < nums[m]`)
In a normal binary search, you only need one comparison (`nums[m] < target`, `nums[m] > target` is it bigger or smaller?) because the entire array is sorted.

In a rotated array, you only have partial information. When you determine the **left** side is sorted:
e.g.,
`[4, 5, 6, 7, 8, 1, 2, 3]`; `target = 5`

* If `mid` is 7, then left is normal, right is abnormal

You know the range from nums[l] (4) to nums[m] (7) is a clean, increasing line.

But the other side (nums[m+1] (8) to nums[r] (3)) contains the rotation point (the "drop"), so it's a mix of very large and very small numbers.

By checking both ends (nums[l] <= target AND target < nums[m]), you are asking: "Is the target definitely inside this specific sorted window?"

If Yes (target = 5): You can safely throw away the entire right side.

If No (target = 2 or 8): You don't know exactly where it is, but you know it’s not in the sorted window, so you jump to the "messy" side.

2. Why use <= instead of just <?

IMPORTANT: We use `nums[l] <= target` because the **target** could actually be the *"first element"* in your current range.

Example: nums = [4, 5, 6, 7, 0, 1, 2], target = 4

l = 0, r = 6, m = 3 (nums[m] = 7).

Left side is sorted (4 to 7).

**If you used nums[l] < target, the condition 4 < 4 would be False!**

You would incorrectly skip the left side and look in the right side, even though your target was sitting right there at nums[l].

The <= ensures that the edges of your sorted window are included in the search.

And why not `target <= nums[m]`? because we already confirmed `target` != `nums[m]` earlier, so this won't happen at all. Hence, use `target < nums[m]` is sufficient.

3. Why the <= for the "which side is sorted check", the `if nums[l] <= nums[m]?` , specifically?

The equal sign is a "safety net" for when your search range gets very small (specifically when you only have two elements left).
Scenario: nums = [3, 1], target = 1
* l = 0, r = 1.
* m = (0 + 1) // 2 = 0. So nums[m] = 3.
* Now, we compare nums[l] and nums[m]. Since l and m are both index 0, the value is the same ($3 = 3$).
* By using <=, we correctly identify that the left side (even if it's just one number) is the starting point for our logic, keeping the pointers moving correctly.

### 3. Find Peak Element
```python
    while l <= r:
        m = (l + r) // 2
        
        # Check if m is on a downward slope. ie., there exists at least 1 peak on the left
        # hence, we will go left, r = m-1
        # (if m is at the very end, it's a peak)
        if m == n - 1 or nums[m] > nums[m + 1]:
            ans = m    # This could be the peak! Save it.
            r = m - 1  # Now see if there's a peak even further to the left.
        else: # upward slope
            l = m + 1  # Slope is going up, peak MUST be to the right.
            
    return ans
```

Think of the array as a mountain landscape.

Climbing the slope: If we pick a middle element and the element to its right is greater (nums[mid] < nums[mid + 1]), we are on an "uphill" slope. This means a peak must exist somewhere to the right (eventually the values will drop or hit the end of the array, which counts as ).

Descending the slope: If the element to the right is smaller (nums[mid] > nums[mid + 1]), we are on a "downhill" slope (or currently on a peak). This means a peak must exist to the left (or at the current position).
We cut the search space in half at every step based on the slope.


### 4. Search Insert Position: understand the "crossover"
```python
    def searchInsert(self, nums, target):
        l = 0 
        r= len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        # When the loop breaks, l is the insertion point
        return l
```
The `<=` in your `while` loop condition is exactly what forces that final "crossover" to happen.

If the loop was while l < r, the pointers would stop the moment they touched. But because it is while l <= r, they are forced to interact one last time when they are on the same element.

Here is exactly how that while condition dictates the final positions of l and r

1. The "Final Interaction"
When l == r, the loop runs one last time. During this final lap, m is calculated as being equal to both l and r.

* If nums[m] is too small: l jumps to m + 1.

* If nums[m] is too large: r drops to m - 1.

Because one of them must move past the other for the condition l <= r to finally become false, they end up "swapped."

2. The Relationship After the Loop
Once the loop breaks, the following "Post-Condition" is always true:

* r < l (Specifically, r + 1 = l)

This creates a "sandwich" where the insertion point is the dividing line:

Everything from index 0 to r is strictly smaller than the target.

Everything from index l to the end is greater than or equal to the target.

ps.,In the context of the Standard Binary Search (while l <= r) where the target is not found, yes, it is ALWAYS true that $r + 1 = l$ when the loop terminates.

This happens because the loop only stops when the condition l <= r is broken. The "smallest" way to break that condition is for the pointers to pass each other by exactly one position. As long as it does not return early.

* "Where is the element just smaller than the target?" $\rightarrow$ Return $r$.
* "Where should I insert the target?" $\rightarrow$ Return $l$.
* "How many elements are smaller than the target?" $\rightarrow$ Return $l$ (since $l$ elements exist from index $0$ to $r$).

## Key Techniques
- Use `left <= right` for exact match, `left < right` for boundary search
- Calculate mid as `left + (right - left) // 2` to avoid overflow
- Decide whether to include/exclude mid in next iteration
- Handle rotated arrays by checking which half is sorted
- Use binary search on answer space for optimization problems

