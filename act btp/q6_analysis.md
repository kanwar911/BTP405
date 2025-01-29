Include written analysis here 

Each algorithm uses a different approach to sort data.
Selection Sort works by repeatedly finding the minimum element in the unsorted portion and placing it at the correct position. 
Bubble Sort compares adjacent elements and swaps them if they're out of order, repeating until the list is sorted. Merge Sort takes a divide-and-conquer approach, recursively splitting the list into smaller parts, sorting them, and then combining them back in order.

The results showed clear performance differences between these algorithms. Merge Sort, with its O(n log n) time complexity, performed significantly better than the others, especially with larger datasets. Both Selection Sort and Bubble Sort, having O(n²) time complexity, showed acceptable performance with small lists but became notably slower as the list size increased.
Based on our findings, Merge Sort is the recommended choice for larger datasets due to its superior efficiency. Selection Sort and Bubble Sort, while suitable for small lists, become impractical as the data size grows. This aligns with theoretical expectations and demonstrates why Merge Sort is often preferred in practical applications.
