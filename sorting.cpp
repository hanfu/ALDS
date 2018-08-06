#include <cstdio>
#include <cmath>
#include <iostream>
//#include <algorithm>

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

void merge(int arr[], int start, int mid, int end)
{
	int il, ir;
	il = mid-start;
	ir = end-mid;
	int larr[il+1], rarr[ir+1];
	//copy(arr+start,arr+mid, larr)
	//copy(arr+mid, arr+end, rarr)
	for(il=0;il<mid-start;il++)
	{
		larr[il] = arr[start+il];
	}
	larr[il] = 100;
	//for infinity
	//not il+1, because il from last loop is already max+1
	for(ir=0;ir<end-mid;ir++)
	{
		rarr[ir] = arr[mid+ir];
	}
	rarr[ir] = 100;
	il = 0;
	ir = 0;
	int j;

	for(j=0;j<end-start;j++)
	{
		if(larr[il] < rarr[ir])
		{
			arr[j] = larr[il];
			il++;
		} else
		{
			arr[j] = rarr[ir];
			ir++;
		}
	}
}
void MergeSort(int arr[], int start, int end)
{
	if(end-start > 1)
	{
		int mid = (start+end)/2;
		MergeSort(arr, start, mid);
		MergeSort(arr, mid, end);
		merge(arr, start, mid, end);
	}
}

void printArray(int arr[], int n)
{
   int i;
   for (i=0; i < n; i++)
       cout<<arr[i]<<" ";
   cout<<endl;
}

int main(int argc, char const *argv[])
{
	int arr[] = {1,2,2};
    int n = sizeof(arr)/sizeof(arr[0]);
 
    MergeSort(arr, 0, n);
    //std::cout << arr <<endl;
 	printArray(arr, n);
	return 0;
}