/* This program gets the size of the array from the user 
gets the value of the array from the user and using insertion sort
technique it sorts the arrya and prints bothe the sorted and the unsorted array */

#include<stdio.h>

void main(){

    int key, size, j, i;

    // Getting the size of the variable 
    printf("enter the size of the list : ");
    scanf("%d", &size);

    // Initializing the arrray
    int array[size];

    // Getting the values of the array
    for (i = 0; i < size; i++)
    {
        printf("enter the %dth element : ", i + 1);
        scanf("%d", &array[i]);
    }

    // Printing the Unsorted Array 
    printf("Unsorted Array : ");
    for (i = 0; i < size-1; i++)
    {
        printf("%d --> ",array[i]);
    }
    printf("%d\n", array[size - 1]);

    // Implementation of insertion Sort
    for (i = 1; i < size; i++)
    {
        key = array[i];
        j = i - 1;
        while (j>=0&&array[j]>key)
        // This loop runs till all the element left to the key is sorted 
        {
            array[j + 1] = array[j];
            j--;
        }
        array[j + 1] = key;
    }

    printf("sorted Array : ");
    for (i = 0; i < size - 1; i++)
    {
        printf("%d --> ", array[i]);
    }
    printf("%d /n", array[size - 1]);
}