#include <stdio.h>

void insertion_sort(int *array, int arraySize)
{
    for(int j = 1; j < arraySize; j++)
    {
        int key = array[j];
        int i = j -1;
        printf("j is: %d\n", j);
        while(i >= 0 && array[i] > key)
        {
            int temp = array[i];
            array[i] = array[i + 1];
            array[i+1] = temp;
            i --;
            key=array[i+1];
            printf("j is: %d\t, chenge key to: %d\n", j, key); 
        }
    }
}

int main()
{
    int array[] = {8, 2, 4, 1, 5, 9, 7, 0};

    int len = sizeof(array)/sizeof(array[0]);
    insertion_sort(array, len);
    printf("\n");
    for(int i = 0; i < len; i ++)
    {
        printf("%d\t", array[i]);
    }
    printf("\n");
    return 0;
}