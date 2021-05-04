#include <iostream>
using namespace std;
struct point
{
    int x, y;
    point(int x, int y) : x(x), y(y)
    {
    }
};
struct line
{
    int a, b, c;
    line(int a, int b, int c) : a(a), b(b), c(c)
    {
    }
    line()
    {
    }
};
int evalPointOnLine(point p, line curLine)
{
    int eval = curLine.a * p.x +
               curLine.b * p.y +
               curLine.c;
    if (eval > 0)
        return 1;
    return -1;
}
int minJumpToReachDestination(point start,
                              point dest, line lines[], int N)
{
    int jumps = 0;
    for (int i = 0; i < N; i++)
    {
        int signStart = evalPointOnLine(start, lines[i]);
        int signDest = evalPointOnLine(dest, lines[i]);
        if (signStart * signDest < 0)
            jumps++;
    }
    return jumps;
}
int main()
{
    point start(1, 1);
    point dest(-2, -1);
    line lines[3];
    lines[0] = line(1, 0, 0);
    lines[1] = line(0, 1, 0);
    lines[2] = line(1, 1, -2);
    cout << minJumpToReachDestination(start, dest, lines, 3);
    return 0;
}
