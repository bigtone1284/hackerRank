"""========================================================================================================================

Problem statement

Given two points P and Q, output the symmetric point of point P about Q.

Input format: 
The first line contains an integer T representing the number of testcases (T <= 15) 
Each test case contains Px Py Qx Qy representing the (x,y) coordinates of P and Q, all of them being integers.

Constraints 
1 <= T <= 15 
-100 <= x, y <= 100

Output format 
For each test case output x and y coordinates of the symmetric point

Sample input

1  
0 0 1 1
Sample output

2 2
This challenge was a part of Pragyan 12

========================================================================================================================"""

def symm_point(a,b,c,d):
    return str(c-a+c)+" "+str(d-b+d)

def main():
    cases = raw_input()
    for i in range(int(cases)):
        answer = map(int,raw_input().split(" "))
        print symm_point(answer[0],answer[1],answer[2],answer[3])
        
if __name__ == "__main__":
	main()
