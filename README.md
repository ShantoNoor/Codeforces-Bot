# Codeforces-Bot

# What can it do!
It can download all the provided test cases for a single problem or all problems of a single contest at once with proper folder structure.
And create the solution files for c++ and as well as python with the contents of cpp_template.txt and py_template.txt for each problem.</br>
```bash
Educational Codeforces Round 92 (Rated for Div. 2)\
        A. LCM Problem\
                A. LCM Problem.py
                A. LCM Problem.cpp
                input.txt
                output.txt
        ..........................
        ..........................
        F. Bicolored Segments\
                F. Bicolored Segments.py
                F. Bicolored Segments.cpp
                input.txt
                output.txt
                input1.txt
                output1.txt
                input2.txt
                output2.txt
        ..........................
        ..........................
```

# Setup/Installation
### Requirements: Python 3.7+, Python Modules: requests, re, os, sys </br>
#### All required modules are built in modules except requests module! </br>
```python
# Install requests via pip: 
pip install requests
```

# How to use
Just provide the link to the problem or contest with path(here to download). Here the path is optional. </br>
If don't provided then it will by default use the default path provided in ```CF_Bot.py at line 93```

```python
# file name = CF_Bot.py
# line number = 93

path = r'' #<-- Default Path: if not set it will use main_path(where CF_Bot.py is located!)
```
Run CF_Bot.py and give link and a path(optional! separated by ','[comma character]).</br>
Run Command: ```python CF_Bot.py``` <br />
```bash
# Example 1:
Enter info(link, path): https://codeforces.com/contest/1389/problem/C
```
```bash
# Example 2:
Enter info(link, path): https://codeforces.com/contest/1389/problem/C, C:\Users\Shanto\Desktop\CodeForces
```
```bash
# Output: Example 2

Codeforces Bot by Shanto Noor !...
Starting process...

Link: https://codeforces.com/contest/1389/problem/C
Path: C:\Users\Shanto\Desktop\CodeForces

        C. Good String\
                C. Good String.py
                C. Good String.cpp
                input.txt
                output.txt

Process finished successfully!...
```
Also can be run with command line arguments. </br>
Give link and path(optional! separated by ' '[space character] and also surround it with double quotation if it contains space character in it!) as command line arguments.</br>
```bash
# Example 1:
python CF_Bot.py CF_Bot.py https://codeforces.com/contest/1389/
```
```bash
# Example 2:
python CF_Bot.py https://codeforces.com/contest/1389/ "C:\Users\Shanto\Desktop\CodeForces"
```
```bash
# Output: Example 2

Codeforces Bot by Shanto Noor !...
Starting process...

Link: https://codeforces.com/contest/1389/
Path: C:\Users\Shanto\Desktop\CodeForces

Educational Codeforces Round 92 (Rated for Div. 2)\
        A. LCM Problem\
                A. LCM Problem.py
                A. LCM Problem.cpp
                input.txt
                output.txt
        B. Array Walk\
                B. Array Walk.py
                B. Array Walk.cpp
                input.txt
                output.txt
        C. Good String\
                C. Good String.py
                C. Good String.cpp
                input.txt
                output.txt
        D. Segment Intersections\
                D. Segment Intersections.py
                D. Segment Intersections.cpp
                input.txt
                output.txt
        E. Calendar Ambiguity\
                E. Calendar Ambiguity.py
                E. Calendar Ambiguity.cpp
                input.txt
                output.txt
        F. Bicolored Segments\
                F. Bicolored Segments.py
                F. Bicolored Segments.cpp
                input.txt
                output.txt
                input1.txt
                output1.txt
                input2.txt
                output2.txt
        G. Directing Edges\
                G. Directing Edges.py
                G. Directing Edges.cpp
                input.txt
                output.txt
                input1.txt
                output1.txt

Process finished successfully!...
```
#
# Thanks For Reading!
