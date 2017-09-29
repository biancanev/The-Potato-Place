// Computes time difference of two time period
// Time periods are entered by the user

#include <iostream>
using namespace std;

struct TIME
{
  int seconds;
  int minutes;
  int hours;
};

void computeTimeDifference(struct TIME, struct TIME, struct TIME *);

int main()
{
    struct TIME t1, t2, difference;

    cout << "Enter start time." << endl;
    cout << "Enter hours, minutes and seconds respectively: ";
    cin >> t1.hours >> t1.minutes >> t1.seconds;

    cout << "Enter stop time." << endl;
    cout << "Enter hours, minutes and seconds respectively: ";
    cin >> t2.hours >> t2.minutes >> t2.seconds;

    computeTimeDifference(t1, t2, &difference);

    cout << endl << "TIME DIFFERENCE: " << t1.hours << ":" << t1.minutes << ":" << t1.seconds;
    cout << " - " << t2.hours << ":" << t2.minutes << ":" << t2.seconds;
    cout << " = " << difference.hours << ":" << difference.minutes << ":" << difference.seconds;
    return 0;
}
void computeTimeDifference(struct TIME t1, struct TIME t2, struct TIME *difference){
    
    if(t2.seconds > t1.seconds)
    {
        --t1.minutes;
        t1.seconds += 60;
        #include <iostream>
using namespace std;

struct student
{
    char name[50];
    int roll;
    float marks;
} s[10];

int main()
{
    cout << "Enter information of students: " << endl;

    // storing information
    for(int i = 0; i < 10; ++i)
    {
        s[i].roll = i+1;
        cout << "For roll number" << s[i].roll << "," << endl;

        cout << "Enter name: ";
        cin >> s[i].name;

        cout << "Enter marks: ";
        cin >> s[i].marks;

        cout << endl;
    }

    cout << "Displaying Information: " << endl;

    // Displaying information
    for(int i = 0; i < 10; ++i)
    {
        cout << "\nRoll number: " << i+1 << endl;
        cout << "Name: " << s[i].name << endl;
        cout << "Marks: " << s[i].marks << endl;
    }

    return 0;
}
// Complex numbers are entered by the user

#include <iostream>
using namespace std;

typedef struct complex
{
    float real;
    float imag;
} complexNumber;

complexNumber addComplexNumbers(complex, complex);

int main()
{
    complexNumber n1, n2, temporaryNumber;
    char signOfImag;

    cout << "For 1st complex number," << endl;
    cout << "Enter real and imaginary parts respectively:" << endl;
    cin >> n1.real >> n1.imag;

    cout << endl << "For 2nd complex number," << endl;
    cout << "Enter real and imaginary parts respectively:" << endl;
    cin >> n2.real >> n2.imag;

    signOfImag = (temporaryNumber.imag > 0) ? '+' : '-';
    temporaryNumber.imag = (temporaryNumber.imag > 0) ? temporaryNumber.imag : -temporaryNumber.imag; 

    temporaryNumber = addComplexNumbers(n1, n2);    
    cout << "Sum = "  << temporaryNumber.real << temporaryNumber.imag << "i";
    return 0;
}

complexNumber addComplexNumbers(complex n1,complex n2)
{
      complex temp;
      temp.real = n1.real+n2.real;
      temp.imag = n1.imag+n2.imag;
      return(temp);
    }

    difference->seconds = t1.seconds - t2.seconds;
    if(t2.minutes > t1.minutes)
    {
        --t1.hours;
        t1.minutes += 60;
    }
    difference->minutes = t1.minutes-t2.minutes;
    difference->hours = t1.hours-t2.hours;
}
