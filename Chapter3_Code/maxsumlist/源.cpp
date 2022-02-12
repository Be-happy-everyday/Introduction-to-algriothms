#include<iostream>
using namespace std;

int* find_max_crossing_subarray(int* A, int low, int mid, int high);
int* find_maximum_subarray(int* A, int low, int high);

int main()
{
	int* nums = new int[16]{13,-3,-25,-20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7};
	int i = 0;
	while (i < 16)
	{
		cout << nums[i++] << " ";
	}

	cout << endl;
	int* p = find_maximum_subarray(nums, 0, 15);
	i = 0;
	while (i < 3)
	{
		cout << p[i++] << " ";
	}
	return 0;
}

int* find_max_crossing_subarray(int* A, int low, int mid, int high)
{
	int left_sum = A[mid] - 1;
	int sum = 0;
	int max_left, max_right;
	for (int i = mid; i >= low; i--)
	{
		sum = sum + A[i];
		if (sum > left_sum)
		{
			left_sum = sum;
			max_left = i;
		}
	}

	int right_sum = A[mid + 1] - 1;
	sum = 0;
	for (int i = mid + 1; i <= high; i++)
	{
		sum = sum + A[i];
		if (sum > right_sum)
		{
			right_sum = sum;
			max_right = i;
		}
	}

	int* p = new int[3]{ max_left, max_right, left_sum+right_sum };
	return p;
}

int* find_maximum_subarray(int* A, int low, int high)
{
	if (low == high)
	{
		int* p = new int[3]{ low, high, A[low] };
		return p;
	}
	else
	{
		int mid = (low + high) / 2;
		int* left = find_maximum_subarray(A, low, mid);
		int* right = find_maximum_subarray(A, mid + 1, high);
		int* cross = find_max_crossing_subarray(A, low, mid, high);

		if (left[2] > right[2] && left[2] > cross[2])
		{
			return left;
		}
		else if (right[2] > left[2] && right[2] > cross[2])
		{
			return right;
		}
		else
		{
			return cross;
		}
	}
}

