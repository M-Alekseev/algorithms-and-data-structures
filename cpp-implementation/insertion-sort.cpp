#include <iostream>
#include <string.h>

template <class T> void insert(T *item, int count);

int main()
{
    char str[] = "dcab";
    insert(str, (int)strlen(str));
    std::cout << str << std::endl;
    return 0;
}

template <class T> void insert(T *item, int count)
{
    int a, b;
    T temp;
    for (a = 0; a < count; a++)
    {
        temp = item[a];
        for (b = a-1; b >= 0 && temp < item[b]; b--)
            item[b+1] = item[b];
        item[b+1] = temp;
    }
}
