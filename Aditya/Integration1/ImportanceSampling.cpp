#include<iostream>
#include<random>
#include<ctime>
#include<vector>
#include<fstream>
#include<iomanip>
#include<cstdlib>
#include<stdexcept>
using namespace std;

class Integral{
    private:
        int N[6] = {500, 5000, 50000, 500000, 5000000, 50000000};
        mt19937 g;
        uniform_real_distribution<double> r;

        double f(double x){
            return 4/(1 + pow(x, 2));
        }

    public:
        Integral() : g(static_cast<unsigned int> (time(0))), r(0, 1) {}

        double findIntegral(int n){
            double sum = 0, rn, value;
            for (int i = 0; i < n; i++)
            {
                rn = r(g);
                sum += f(rn);
            }

            value = (1.0/n)*sum;
            return value;
        }

        vector<double> answers(){
            vector<double> answer;
            for (size_t j = 0; j < 6; j++)
            {
                answer.push_back(findIntegral(N[j]));
            }

            return answer;
        }

        void file_print(){
            vector<double> Ans = answers();
            try
            {
                ofstream file("C:/Users/lenovo/OneDrive/Desktop/Coding/SIES C++/Computational peoblems/Integration1/answers_of_f(x).txt");
                if (file.is_open())
                {
                    file<<"| Number of iterations | Integral of the given function |"<<endl;
                    for (size_t k = 0; k < 6; k++)
                    {
                        file<<"| "<<setw(21)<<fixed<<setprecision(0)<<left<<N[k]<<"| "<<setw(31)<<fixed<<setprecision(8)<<left<<Ans[k]<<"|"<<endl;
                    }
                    
                }
                else
                {
                    throw runtime_error("The file couldn't be opened");
                }
                
            }
            catch(const exception& e)
            {
                cerr<<e.what()<<endl;
            }
            
        }
};

int main(){
    cout<<"This Program will give the solution of the integration of function 4/(1+x^2) from 0 to 1."<<endl;
    Integral function;
    function.file_print();
    system("start answers_of_f(x).txt");
    return 0;
}