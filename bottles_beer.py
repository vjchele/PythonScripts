import random
names = ['Srinivas','Satish','Dileep','Ayyappan','Sucharith','Vijay']
print('Happy Birthday Sucharith!!!!')

for i in range(42,0,-1):
    if (i ==1):
        print('No more bottles of beer on the wall, no more bottles of beer.')
        print('If that one bottle should happen to fall, what a waste of alcohol')
    else:
        print('{0} bottles of beer on the wall, {0} bottles of beer on the wall'.format(i))
        print('Take one down, {0} - Gulp it down!, {1} bottles of beer on the wall'.format(names[random.randint(0,len(names)-1)],i-1))

'''
Happy Birthday Sucharith!!!!
42 bottles of beer on the wall, 42 bottles of beer on the wall
Take one down, Sucharith - Gulp in down!, 41 bottles of beer on the wall
41 bottles of beer on the wall, 41 bottles of beer on the wall
Take one down, Sucharith - Gulp in down!, 40 bottles of beer on the wall
40 bottles of beer on the wall, 40 bottles of beer on the wall
Take one down, Srinivas - Gulp in down!, 39 bottles of beer on the wall
39 bottles of beer on the wall, 39 bottles of beer on the wall
Take one down, Sucharith - Gulp in down!, 38 bottles of beer on the wall
38 bottles of beer on the wall, 38 bottles of beer on the wall
Take one down, Satish - Gulp in down!, 37 bottles of beer on the wall
37 bottles of beer on the wall, 37 bottles of beer on the wall
Take one down, Srinivas - Gulp in down!, 36 bottles of beer on the wall
36 bottles of beer on the wall, 36 bottles of beer on the wall
Take one down, Ayyappan - Gulp in down!, 35 bottles of beer on the wall
35 bottles of beer on the wall, 35 bottles of beer on the wall
Take one down, Vijay - Gulp in down!, 34 bottles of beer on the wall
34 bottles of beer on the wall, 34 bottles of beer on the wall
Take one down, Sucharith - Gulp in down!, 33 bottles of beer on the wall
33 bottles of beer on the wall, 33 bottles of beer on the wall
Take one down, Srinivas - Gulp in down!, 32 bottles of beer on the wall
32 bottles of beer on the wall, 32 bottles of beer on the wall
Take one down, Satish - Gulp in down!, 31 bottles of beer on the wall
31 bottles of beer on the wall, 31 bottles of beer on the wall
Take one down, Ayyappan - Gulp in down!, 30 bottles of beer on the wall
30 bottles of beer on the wall, 30 bottles of beer on the wall
Take one down, Dileep - Gulp in down!, 29 bottles of beer on the wall
29 bottles of beer on the wall, 29 bottles of beer on the wall
Take one down, Vijay - Gulp in down!, 28 bottles of beer on the wall
28 bottles of beer on the wall, 28 bottles of beer on the wall
Take one down, Sucharith - Gulp in down!, 27 bottles of beer on the wall
27 bottles of beer on the wall, 27 bottles of beer on the wall
Take one down, Ayyappan - Gulp in down!, 26 bottles of beer on the wall
26 bottles of beer on the wall, 26 bottles of beer on the wall
Take one down, Ayyappan - Gulp in down!, 25 bottles of beer on the wall
25 bottles of beer on the wall, 25 bottles of beer on the wall
Take one down, Ayyappan - Gulp in down!, 24 bottles of beer on the wall
24 bottles of beer on the wall, 24 bottles of beer on the wall
Take one down, Ayyappan - Gulp in down!, 23 bottles of beer on the wall
23 bottles of beer on the wall, 23 bottles of beer on the wall
Take one down, Dileep - Gulp in down!, 22 bottles of beer on the wall
22 bottles of beer on the wall, 22 bottles of beer on the wall
Take one down, Ayyappan - Gulp in down!, 21 bottles of beer on the wall
21 bottles of beer on the wall, 21 bottles of beer on the wall
Take one down, Dileep - Gulp in down!, 20 bottles of beer on the wall
20 bottles of beer on the wall, 20 bottles of beer on the wall
Take one down, Srinivas - Gulp in down!, 19 bottles of beer on the wall
19 bottles of beer on the wall, 19 bottles of beer on the wall
Take one down, Dileep - Gulp in down!, 18 bottles of beer on the wall
18 bottles of beer on the wall, 18 bottles of beer on the wall
Take one down, Dileep - Gulp in down!, 17 bottles of beer on the wall
17 bottles of beer on the wall, 17 bottles of beer on the wall
Take one down, Ayyappan - Gulp in down!, 16 bottles of beer on the wall
16 bottles of beer on the wall, 16 bottles of beer on the wall
Take one down, Dileep - Gulp in down!, 15 bottles of beer on the wall
15 bottles of beer on the wall, 15 bottles of beer on the wall
Take one down, Sucharith - Gulp in down!, 14 bottles of beer on the wall
14 bottles of beer on the wall, 14 bottles of beer on the wall
Take one down, Vijay - Gulp in down!, 13 bottles of beer on the wall
13 bottles of beer on the wall, 13 bottles of beer on the wall
Take one down, Sucharith - Gulp in down!, 12 bottles of beer on the wall
12 bottles of beer on the wall, 12 bottles of beer on the wall
Take one down, Srinivas - Gulp in down!, 11 bottles of beer on the wall
11 bottles of beer on the wall, 11 bottles of beer on the wall
Take one down, Vijay - Gulp in down!, 10 bottles of beer on the wall
10 bottles of beer on the wall, 10 bottles of beer on the wall
Take one down, Ayyappan - Gulp in down!, 9 bottles of beer on the wall
9 bottles of beer on the wall, 9 bottles of beer on the wall
Take one down, Satish - Gulp in down!, 8 bottles of beer on the wall
8 bottles of beer on the wall, 8 bottles of beer on the wall
Take one down, Srinivas - Gulp in down!, 7 bottles of beer on the wall
7 bottles of beer on the wall, 7 bottles of beer on the wall
Take one down, Dileep - Gulp in down!, 6 bottles of beer on the wall
6 bottles of beer on the wall, 6 bottles of beer on the wall
Take one down, Srinivas - Gulp in down!, 5 bottles of beer on the wall
5 bottles of beer on the wall, 5 bottles of beer on the wall
Take one down, Sucharith - Gulp in down!, 4 bottles of beer on the wall
4 bottles of beer on the wall, 4 bottles of beer on the wall
Take one down, Sucharith - Gulp in down!, 3 bottles of beer on the wall
3 bottles of beer on the wall, 3 bottles of beer on the wall
Take one down, Vijay - Gulp in down!, 2 bottles of beer on the wall
2 bottles of beer on the wall, 2 bottles of beer on the wall
Take one down, Vijay - Gulp in down!, 1 bottles of beer on the wall
No more bottles of beer on the wall, no more bottles of beer.
If that one bottle should happen to fall, what a waste of alcohol
'''
