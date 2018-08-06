#include <cstdio>
#include <cmath>
#include <iostream>
using namespace std;

void InsertionSort(int arr[], int n)
{
	int i, j, key;
	for(i = 1; i<n; i++)
	{
		j = i;
		key = arr[i];
		while(key < arr[j-1] && j>0)
		{
			arr[j] = arr[j-1];
			j--;
		}
		arr[j] = key;
	}

}

void SelectionSort(int arr[], int n)
{
	int i, j, min;
	for(i=0;i<n-1;i++)
	{
		min = i;
		for(j=i+1;j<n;j++)
		{
			if (arr[j] < arr[min])
			{
				min = j;
			}
		}
		//swap(&arr[min], &arr[i]);
		//arr is a pointer, but arr[0] is int
		//so we need &arr[i]
	int min_num = arr[min];
	arr[min] = arr[i];
	arr[i] = min_num;

	}
}

void printArray(int arr[], int n)
{
   int i;
   for (i=0; i < n; i++)
       printf("%d ", arr[i]);
   printf("\n");
}

int main(int argc, char const *argv[])
{
	int arr[] = {4,2,3,2,1,0};
    int n = sizeof(arr)/sizeof(arr[0]);
 
    SelectionSort(arr, n);
    //std::cout << arr <<endl;
 	printArray(arr, n);
	return 0;
}