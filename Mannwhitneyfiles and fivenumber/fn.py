import numpy as np
import csv
def fivenum(data): return np.percentile(
    data, [0, 25, 50, 75, 100], interpolation='midpoint')
print('one')
test1 = [88.47,
87.63,
88.47,
88.47,
89.15,
88.47,
87.12,
90.68,
87.46,
91.69]
print(fivenum(test1))
print('two')
test2 = [94.07,
92.2,
94.07,
92.71,
93.39,
92.71,
93.39,
92.88,
90.34,
93.05]
print(fivenum(test2))
print('three')

test3 = [93.9,
90.85,
93.9,
92.37,
93.39,
91.86,
92.37,
90,
93.56,
93.39]
print(fivenum(test3))
print('four')

test4 = [87.27,
90.15,
85.55,
90.14,
89.66,
89.14,
89.97,
89.82,
91.68,
90.49]
print(fivenum(test4))

print('five')


test5 = [93.71,
94.23,
94.23,
95.52,
92.7,
93.88,
93.54,
94.24,
92.53,
91.68]
print(fivenum(test5))
print('six')
test6 = [90.68,
93.55,
93.73,
93.22,
93.89,
93.72,
93.04,
93.72,
93.89,
94.06]
print(fivenum(test6))
print('seven')
test7 = [77.07,
75.39,
74.71,
75.06,
74.19,
73.18,
74.7,
75.54,
74.35,
73.84]
print(fivenum(test7))
print('eight')
test8 = [77.4,
77.76,
78.78,
74.03,
78.28,
78.78,
78.12,
79.27,
79.29,
79.81]
print(fivenum(test8))

print('nine')
test9 = [77.75,
80.32,
78.28,
78.44,
79.81,
79.8,
78.78,
79.8,
76.24,
78.25]
print(fivenum(test9))

print('ten')
test10 = [88.64,
91.36,
92.71,
92.2,
87.63,
85.59,
87.29,
92.2,
90,
88.81]
print(fivenum(test10))
print('eleven')
test11 = [94.48,
94.92,
94.92,
96.27,
94.58,
93.9,
93.73,
94.58,
96.27,
92.88]
print(fivenum(test11))
print('twelve')
test12 = [91.69,
90.34,
94.58,
94.07,
92.71,
94.41,
93.73,
95.25,
93.39,
94.07]
print(fivenum(test12))
print('thirteen')
test13 = [93.38,
95.08,
93.55,
94.91,
92.54,
93.05,
93.21,
94.06,
90.49,
92.54]
print(fivenum(test13))
print('fourteen')
test14 = [95.76,
95.92,
95.08,
94.56,
95.58,
96.61,
93.9,
94.9,
92.36,
96.1]
print(fivenum(test14))
print('fifteen')
test15 = [95.92,
94.56,
93.55,
92.03,
95.25,
92.18,
93.39,
92.36,
95.41,
96.1]
print(fivenum(test15))
print('sixteen')
test16 = [78.09,
81.15,
80.82,
79.29,
80.65,
76.73,
79.98,
79.46,
80.31,
79.78]
print(fivenum(test16))
print('seventeen')
test17 = [76.56,
78.08,
79.8,
78.95,
77.4,
81.48,
78.61,
76.72,
77.76,
80.82]
print(fivenum(test17))
print('eighteen')
test18 = [83.19,
80.12,
80.8,
78.95,
80.31,
80.3,
78.78,
81.14,
78.6,
79.45]
print(fivenum(test18))
print('nineteen')
test19 = [91.69,
88.81,
88.64,
91.02,
84.07,
91.69,
93.05,
88.81,
85.59,
92.03]
print(fivenum(test19))
print('twenty')
test20 = [94.07,
91.86,
93.22,
95.59,
95.08,
91.86,
92.2,
94.92,
92.03,
92.54]
print(fivenum(test20))
print('twenty one')
test21 = [93.39,
93.9,
94.24,
94.24,
94.24,
93.73,
93.56,
93.05,
91.19,
92.88]
print(fivenum(test21))
print('twenty two')
test22 = [93.55,
93.55,
93.55,
93.21,
93.21,
94.23,
94.4,
93.39,
94.22,
94.91]
print(fivenum(test22))
print('twenty three')
test23 = [92.71,
95.59,
94.56,
93.55,
93.72,
94.73,
94.75,
95.42,
95.59,
93.55]
print(fivenum(test23))
print('twenty four')
test24 = [93.69,
95.24,
95.76,
92.18,
94.57,
92.54,
92.37,
95.08,
91.01,
94.24]
print(fivenum(test24))
print('twenty five')
test25 = [82.02,
80.63,
81.15,
81.17,
76.24,
80.46,
78.95,
77.75,
78.95,
78.94]
print(fivenum(test25))
print('twenty six')
test26 = [79.09,
80.81,
79.79,
78.78,
81.3,
76.4,
79.96,
78.1,
78.6,
79.44]
print(fivenum(test26))
print('twenty seven')
test27 = [80.48,
79.62,
73.69,
79.63,
77.77,
78.46,
77.08,
79.28,
79.82,
80.98]
print(fivenum(test27))

with open('output.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow([fivenum(test1)])
    csvwriter.writerow([fivenum(test2)])
    csvwriter.writerow([fivenum(test3)])
    csvwriter.writerow([fivenum(test4)])
    csvwriter.writerow([fivenum(test5)])
    csvwriter.writerow([fivenum(test6)])
    csvwriter.writerow([fivenum(test7)])
    csvwriter.writerow([fivenum(test8)])
    csvwriter.writerow([fivenum(test9)])
    csvwriter.writerow([fivenum(test10)])
    csvwriter.writerow([fivenum(test11)])
    csvwriter.writerow([fivenum(test12)])
    csvwriter.writerow([fivenum(test13)])
    csvwriter.writerow([fivenum(test14)])
    csvwriter.writerow([fivenum(test15)])
    csvwriter.writerow([fivenum(test16)])
    csvwriter.writerow([fivenum(test17)])
    csvwriter.writerow([fivenum(test18)])
    csvwriter.writerow([fivenum(test19)])
    csvwriter.writerow([fivenum(test20)])
    csvwriter.writerow([fivenum(test21)])
    csvwriter.writerow([fivenum(test22)])
    csvwriter.writerow([fivenum(test23)])
    csvwriter.writerow([fivenum(test24)])
    csvwriter.writerow([fivenum(test25)])
    csvwriter.writerow([fivenum(test26)])
    csvwriter.writerow([fivenum(test27)])




