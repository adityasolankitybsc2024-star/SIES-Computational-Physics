#include<iostream>
#include<random>
#include<ctime>
#include<cmath>
#include<iomanip>
using namespace std;

class integration{
    private:
        const int N = pow(10, 8);
        mt19937 g;
        uniform_real_distribution<double> r;
        inline double f(double x){
            return sqrt(x/(1+(x*x*x)));
        }

    public:
        integration() : g(static_cast<unsigned int> (time(0))), r(0, 1) {}

        double findIntegral(){
            double sum = 0;
            for (size_t i = 0; i < N; i++)
            {
                sum += f(r(g));
            }
            
            return sum/N;
        }
};

int main(){
    clock_t start = clock();
    cout<<"This Porgram will find the integration of a function using Monte carlo method."<<endl;
    integration function;
    double solution = function.findIntegral();
    cout<<"The solution of the integral is "<<fixed<<setprecision(6)<<solution<<endl;
    clock_t end = clock();

    cout<<"Time taken to run the program: "<<fixed<<setprecision(4)<<static_cast<double> (end - start)/CLOCKS_PER_SEC<<" seconds"<<endl;
    return 0;
}