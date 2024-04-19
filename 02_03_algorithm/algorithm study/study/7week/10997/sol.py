'''
1 : 
* 1
2 :
2 * 4 - 1
7 7 - N
***** 5
* 1
* *** 5
* * * 5 
* * * 5
*   * 5
***** 5
3 :
3 * 4 - 1
11 h - 2
********* 9
*         9
* ******* 9
* *     * 9
* * *** * 9 
* * * * * 9
* * * * * 9
* *   * * 9
* ***** * 9
*       * 9
********* 9
'''

def draw(n, y, x):
    star = '*'
    if n == 1:
        stars[x][y] = star
        stars[x][y+1] = star
        stars[x][y+2] = star
        return
    else:
        for _ in range(4 * N - 4):
            stars[x][y] = '*'
            stars[y][x] = '*'
            x += 1
        for j in range(4 * N - 2):
            pass
        for q in range(4 * N - 4):
            pass
        for p in range(4 * N - 2):
            pass
        return
N = int(input())

if N == 1:
    print('*')
else:
    width = 4 * N - 3
    height = 4 * N - 1
    stars = [['' for _ in range(width)] for _ in range(height)]
    draw(N, width - 1, height)
    print(stars)