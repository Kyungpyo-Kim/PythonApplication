# Binary Search

- basic

  ```python
  def binary_search(arr, target):
      left = 0
      right = len(arr) - 1
      while left <= right:
          mid = (left + right)//2
          if arr[mid] > target:
              right = mid - 1
          elif arr[mid] < target:
              left = mid + 1
          else:
              return mid
  ```

- lower bound
  ```python
  def binary_search_lower_bound(arr, target):
      """
      return index of the element less than or equal to target
      """
      left = 0
      right = len(arr)
      while left < right:
          mid = (left + right)//2
          if target <= arr[mid]:
              right = mid
          else:
              left = mid + 1
      return left
  ```
- upper bound
  ```python
  def binary_search_upper_bound(arr, target):
      """
      return index of the element larger than or target
      """
      left = 0
      right = len(arr)
      while left < right:
          mid = (left + right)//2
          if target >= arr[mid]:
              left = mid + 1
          else:
              right = mid
      return left
  ```
