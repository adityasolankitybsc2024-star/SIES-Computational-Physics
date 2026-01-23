#include<iostream>
#include<vector>
#include<iomanip>
#include<cmath>
using namespace std;

class Integral{
    protected:
        const double uplim, lowlim;
        const int n;  

        double h = (uplim - lowlim)/n;

        inline double f(double x){
            return cos(x);
        }
    
    public:
        Integral(double l, double u, int n_) : uplim(u),lowlim(l), n(n_) {} 

        bool is_even(){

            if (n%2 == 0)
            {
                return true;
            }
            else
            {
                return false;
            }
            
        }
};

class Simpson1_3 : public Integral{
    public:
        Simpson1_3(double l, double u, int n_) : Integral(l, u, n_) {}

        double findIntegral(){
            double x = lowlim, sum = 0;
            while (x <= uplim)
            {
                if ((x == lowlim) || (x == uplim) || (x < uplim && x >= (uplim -h)))
                {
                    sum += f(x);
                }
                else if ((static_cast<int>((x - lowlim)/h))%2 == 0)
                {
                    sum += 2*f(x);
                }
                else
                {
                    sum += 4*f(x);
                }
                
                x += h;
            }            
            
            return (h/3)*sum;
        }
};

class Simpson3_8 : public Integral{
    public:
        Simpson3_8(double l, double u, int n_) : Integral(l, u, n_) {}

        double findIntegral(){
            double x = lowlim, sum = 0;
            while (x <= uplim)
            {
                if (x == lowlim || (x == uplim) || (x < uplim && x >= (uplim -h)))
                {
                    sum += f(x);
                }
                else if ((static_cast<int>((x - lowlim)/h))%3 == 0)
                {
                    sum += 2*f(x);
                }
                else
                {
                    sum += 3*f(x);
                }
                
                x += h;
            }
            
            return ((3*h)/8)*sum;
        }
};

int main(){
    double ll, ul, answer;
    int number;
    cout<<"This Program finds the integral of a function usng Simpson's integration method."<<endl;
    cout<<"Enter the lower limit of the integral:- ";
    cin>>ll;
    cout<<"Enter the upper limit of the integral:- ";
    cin>>ul;
    cout<<"Enter the number of points to be created to solve the integral(larger the points more the time but more the accuracy.):- ";
    cin>>number;

    Integral function(ll, ul, (number - 1));
    if (function.is_even() == true)
    {
        cout<<"Simpson's 1/3 rule was used."<<endl;
        Simpson1_3 s13(ll, ul, (number - 1));
        answer = s13.findIntegral();
    }
    else if ((function.is_even() == false) && ((number - 1)%3 == 0))
    {
        cout<<"Simpson's 3/8 rule was used."<<endl;
        Simpson3_8 s38(ll, ul, (number - 1));
        answer = s38.findIntegral();
    }
    else
    {
        cout<<"The number of subintervals should be either even or divisible by 3 if odd. The current interval is neither, so, the solution cannot be found."<<endl;
        return 0;
    }
    
    
    cout<<"The solution of the integral between the limits of "<<ll<<" and "<<ul<<" is "<<fixed<<setprecision(6)<<answer<<endl;
    return 0;
}