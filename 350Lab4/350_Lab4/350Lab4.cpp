/**
Justin Igmen
200364880
ENSE 350
Lab 4
**/

#include <iostream>
#include <iomanip>
using namespace std;

int getMatrix(float a[10][10]);
void getLU(float a[10][10], float l[10][10], float u[10][10], int matSize);

int main()
{
	int matSize;

	float a[10][10], l[10][10], u[10][10];

	cout << "LU Decomposition\n";
	matSize = getMatrix(a);
	getLU(a, l, u, matSize);
}

int getMatrix(float a[10][10])
{
	int matSize;
	cout << "Enter size of square matrix: ";
	cin >> matSize;

	cout << "Enter matrix values: ";
	for (int i = 0; i < matSize; i++)
	{
		for (int j = 0; j < matSize; j++)
			cin >> a[i][j];
	}

    cout << endl << "A=" << endl;
    for (int i = 0; i < matSize; i++)
    {
        for (int j = 0; j < matSize; j++)
        {
            cout << setw(6) << a[i][j];
        }
        cout << endl;
    }


	return matSize;
}

void getLU(float a[10][10], float l[10][10], float u[10][10], int matSize)
{
	int i, j, k;
	for (i = 0; i < matSize; i++)
	{
		for (j = 0; j < matSize; j++)
		{
			u[i][j] = a[i][j]; // Assigning elements in U to be the
			if (i == j)					// same as the input matrix 
			{
				l[i][j] = 1;
			}
			else
				l[i][j] = 0;
		}
	}

	// Calculate for U and L matrix

	for (i = 0; i < matSize; i++)
	{
		for (j = i + 1; j < matSize; j++)
		{
			l[j][i] = u[j][i] / u[i][i];

			for (k = 0; k < matSize; k++)
			{
				u[j][k] = u[j][k] - l[j][i] * u[i][k];
			}
		}
	}

    cout << "L = " << endl;
    for (i = 0; i < matSize; i++) {
        for (j = 0; j < matSize; j++) {
            cout << setw(6) << setprecision(3) << l[i][j] ;
        }
        cout << endl;
    }
    cout << "U = " << endl;
    for (i = 0; i < matSize; i++) {
        for (j = 0; j < matSize; j++) {
            cout << setw(6) << setprecision(3) << u[i][j];
        }
        cout << endl;
    }
}