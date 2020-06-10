/*
Justin Igmen
200364880
ENSE 350 Lab 5
*/

#include <iostream>

using namespace std;

int main()
{
	int n;
	float segments, answer = 0;
	cout << "Trapezoidal rule \n\n";

	cout << "f(x) = 2 - 5x + 10x^2 + 0.5x^3" << endl;

	cout << "Enter number of segments: ";
	cin >> n;

	segments = (20 / n);	//10 - (-10) = 20
	int i = -10;
	while (i <= 10)
	{
		if ((i == 10) || (i == -10))
			answer += 2 - 5 * i + 10 * pow(i,2) + 0.5 * pow(i,3);
		else 
			answer += 2 * (2 - 5 * i + 10 * pow(i, 2) + 0.5 * pow(i, 3));

		i += segments;
	}

	answer *= segments/2;

	cout << "The intergral is: " << answer << endl << endl;

}

