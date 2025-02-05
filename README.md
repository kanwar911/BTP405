# BTP405
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17821425&assignment_repo_type=AssignmentRepo)
# Activity 1 (Due Tuesday January 21 - 4%)

## Learning Objectives

After completing this activity, you should be able to….

- use comprehensions to manipulate data structures which support iteration
- import external libraries to add functionality to a program
- design decorator functions to process data
- compare implementations which provide the same functionality
- 

## Late Submissions

Submissions after the due date will be penalized in 10% per day late.  Activities submitted 5 days after the due date will not be accepted and a 0 will be assigned.


## Instructions

Provide solutions to following problems in the empty files given in this repository. There are numerous "Introduction to Python" tutorials and textbooks available online and via [Seneca's digital library](https://library.senecacollege.ca) which you can reference.

Good coding practices from your previous courses should be used.  The submitted functions should also be annotated with *docstrings* as described [here](https://peps.python.org/pep-0257/).

1. (5 points) Write a Python function `getPrimeNumbers(n)` which returns a list containing all prime numbers between 2 and _n_.  Create a helper function to determine if a particular number is prime and then use a comprehension to generate your list.

2. (10 points) Write a Python function `graphSnowfall(t)` which retrives data in a text file _t_ and displays that information in a bar chart.

The file will have a single number on each line representing the amount of snowfall accumulation for a given day. Aggregate these values so that each one contributes to a particular 10 cm range.  For example, a file containing

10

15

45

5

20

25

would have

* 2 between 0-10cms
* 2 between 11-20cms
* 1 between 21-30cms
* 0 between 31-40cms
* 1 between 41-50cms

Use module [matplotlib](https://matplotlib.org/) to plot a bar graph showing your results. The x-axis should show the ranges and the y-axis should show the number of occurances in that range.

3. (5 points) Write a Python function `wordCount(t)` which retrives data in a text file _t_ and returns a dictionary where the _keys_ are unique words in the files and the corresponding _values_ are lists of line numbers where the words are found in the text.

4. (20 points) Write a Python function `printStats(t)` which retrives data in a text file _t_ which reads in lines of numbers.  For each line read in, the function must call a _decorator_ function which prints 
* the numbers read
* the count of the numbers read
* the average of the numbers
* the maximum of the numbers

5. (10 points) Consider the following code blocks which generate the same output.
    1. (7 points) Describe what each program snippet does to compute its results.
    2. (3 points) What type of function is `doubleG(n)`? What is the advantage of using such a function?



```
#Approach 1
def doubleL(n):
    res = []
    for i in range(n): res.append(i * 2)
    return res

for i in doubleL(5): 
    print(i, end=' : ')
```

```
#Approach 2
for x in [n * 2 for n in range(5)]:
    print(x, end=' : ')
```

```
#Approach 3
def doubleG(n):
        for i in range(n):
            yield i * 2

for i in doubleG(5):
        print(i, end=' : ')
```

6. (25 points) Implement and analyse sorting algorithms.

* Define a `Vehicle` class, which stores a vehicle's manufacturer, model, type (sedan, coupe, SUV, truck .etc), cost and current mileage.  The class should be defined so that objects of this type can be compared for sorting purposes.  Objects should also be able to print their current state in a human understandable format. 
* Define a `sort(lst, alg)` function where `lst` represents a list containing *only* `Vehicle` objects and `alg` is a function which sorts the list according to a given criteria (one of `Vehicle`'s fields).  This allows the sort routine used to be configurable by the caller (The Strategy design pattern achieves a simliar goal via subclassing). The function will return a sorted copy of the original list.
* Define the following sorting algorithms.  (Note: you are not allowed to use pre-defined libraries.  Source code must be included.  It is acceptable (and suggested) that you use implementations that are freely available on the Internet. Any code that you have not written yourself __must be cited__ and original author must be identified in the source code) 
  * selection sort
  * merge sort 
  * bubble sort

* Write a program which you will use to conduct your experiments.  In the `main()` method, you should create a configurable number of `Vehicle` objects and place them into a list via comprehension. The objects must be populated with random data.  You will invoke one of the sort routines (specified above) and print the sorted array. 
* Measure the performance of the sorting algorithms.  Test with a varied set of list sizes.  Graph your results to show how execution time varies as the list size increases.
* Summarize your results in a separate written document.  It should *describe how the various sort algorithms work* and *explain the experiment's results*.

7. (25 points) Be prepared to present and explain your work in the lab session immediately after the due date. 


