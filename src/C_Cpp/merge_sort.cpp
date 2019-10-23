#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void merge(int arr[], int left, int mid, int right, int *temp) 
{
    int i = left;
    int j = mid + 1;
    int k = left;

    while(i <= mid && j <= right)
    {
        if (arr[i] <= arr[j])
        {
            temp[k++] = arr[i++];
        }
        else
        {
            temp[k++] = arr[j++];
        }
    }
    while (i <= mid) 
    {
        temp[k++] = arr[i++];
    }
    while (j <= right)
    {
        temp[k++] = arr[i++];
    }
    printf("i is: %d\n", i);

    memcpy(arr + left, temp + left, sizeof(int)*(right - left + 1));

}
void mergeSort(int array[], int left, int right, int* temp)
{
    if (left < right)
    {
        printf("2. right is %d\n", right);
        int mid = left + (right - left) / 2;
        printf("Mid is %d\n", mid);
        mergeSort(array, left, mid, temp);
        mergeSort(array, mid+1, right, temp);
        merge(array, left, mid, right, temp);
    }
}

int main()
{
    int arr[] = {6, 5, 3, 1, 8, 7, 2, 4};
    int len = sizeof(arr)/sizeof(arr[0]);
    printf("len is %d\n", len);

    int *temp = (int*)malloc(sizeof(int)*len);

    printf("1. len is %d\n", len);
    mergeSort(arr, 0, len - 1, temp);
    free(temp);

    for(int i = 0; i < len; i++)
    {
        printf("%d\t", arr[i]);
    }
    return 0;
}