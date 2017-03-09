
/* This function takes last element as pivot, places 
   the pivot element at its correct position in sorted 
   array, and places all smaller (smaller than pivot)
   to left of pivot and all greater elements to right 
   of pivot */

#include <iostream>
using namespace std;

int partition (int arr[], int l, int h)
{
    int x = arr[h];
    int i = (l - 1);

    for (int j = l; j <= h- 1; j++)
    {
        if (arr[j] <= x)
        {
            i++;
            int temp;
            temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;

        }
    }
    int temp;
    temp=arr[i+1];
    arr[i+1]=arr[h];
    arr[h]=temp;
    
    return (i + 1);
}

/* A[] --> Array to be sorted, 
  l  --> Starting index, 
  h  --> Ending index 
  N  --> Number of elements in the array */
void quickSort(int A[], int l, int h, int N)
{
    if (l < h)
    {        
        /* Partitioning index */

        for(int k=0;k<N;k++)
      {
          cout<<A[k]<<' '; 
      }
      cout<<endl;

        int p = partition(A, l, h); 
        quickSort(A, l, p - 1,N);  
        quickSort(A, p + 1, h,N);
    }
}

int main()
{
 cout<< "Enter the number elements in the array"<<endl;
 int N;
 cin>>N;
 int A[N];
 for(int i=0;i<N;i++)
 {
  cout<<"Enter the next element"<<endl;
  cin>>A[i];
 }
 
 cout<<"Array before sorting"<<endl;

 for(int j=0;j<N;j++)
 {
  cout<<A[j]<<' '; 
 }
 cout<<endl;
 cout<<"Array transformations during the process of sorting"<<endl;
 quickSort(A,0,N-1,N);
 
 for(int k=0;k<N;k++)
 {
  cout<<A[k]<<' '; 
 }
 cout<<endl;

}