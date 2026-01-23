#define _USE_MATH_DEFINES
#include<iostream>
#include<cmath>
#include<vector>
#include<fstream>
#include<iomanip>
#include<stdexcept>
#include<cstdlib>
using namespace std;

class plot{
    private:
        const float difference = 0.01, end = 5;

        inline float inversesq(float a){
            return 1/pow(a, 2);
        }

        inline float Gaussian(float b){
            float sigma = 0.5, mu = 1;
            // return 1000*(1/(sigma*pow((2*M_PI), 0.5)))*exp(-1*(pow((b-mu), 2)/(2*pow(sigma, 2))));
            return log((1/(sqrt(2*M_PI*sigma*sigma)))*(exp(-(pow((b - mu), 2)/(2*sigma*sigma)))));
        }

    public:
        
        void plotfn(){
            float num = 0.01, c, d;
            vector<float> xval, yval;
            while (num <= end)
            {   
                xval.push_back(num);
                // yval.push_back(inversesq(num) + Gaussian(num));
                yval.push_back(Gaussian(num));
                num += difference;
            }
            
            try
            {
                ofstream file("C:/Users/lenovo/OneDrive/Desktop/Coding/SIES C++/Computational peoblems/Plot of Gaussian and 1/data.txt");
                if (file.is_open())
                {
                    for (size_t i = 0; i < xval.size(); i++)
                    {
                        file<<setw(8)<<fixed<<setprecision(2)<<left<<xval[i]<<setw(15)<<fixed<<setprecision(4)<<left<<yval[i]<<endl;
                    }
                    
                }
                else
                {
                    throw runtime_error("The file couldn't be opened.");
                }
            }
            catch(const exception& e)
            {
                cerr<<e.what()<<endl;
            }
            
            try
            {
                ofstream gp("C:/Users/lenovo/OneDrive/Desktop/Coding/SIES C++/Computational peoblems/Plot of Gaussian and 1/plot.gp");
                if (gp.is_open())
                {
                    gp<<"set terminal window enhanced font 'Arial, 18'\n"<<endl;
                    gp<<"set title 'Plot of inverse square + Gaussian function' tc rgb 'red' font ', 30'"<<endl;
                    gp<<"set xlabel 'xvalues' tc rgb 'red'"<<endl;
                    gp<<"set ylabel 'yvalues' tc rgb 'red'"<<endl;
                    gp<<"unset key"<<endl;
                    gp<<"set grid lt 1 lw 1 lc rgb 'gray'\n"<<endl;
                    gp<<"plot 'data.txt' u 1:2 w l lt 7 lw 2 lc rgb 'blue'\n"<<endl;
                    gp<<"pause -1"<<endl;
                }
                else
                {
                    throw runtime_error("The file couldn't be opened.");
                }
                
            }
            catch(const exception& f)
            {
                cerr<<f.what()<<endl;
            }
            
        }
};

int main(){
    cout<<"This Program will plot a graph of a function 1/r^2 + gaussian."<<endl;
    plot graph;
    graph.plotfn();
    system("gnuplot \"C:/Users/lenovo/OneDrive/Desktop/Coding/SIES C++/Computational peoblems/Plot of Gaussian and 1/plot.gp\"");
    return 0;
}