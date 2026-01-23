#include<iostream>
#include<random>
#include<ctime>
#include<array>
#include<vector>
#include<fstream>
#include<iomanip>
#include<stdexcept>
#include<cstdlib>
using namespace std;

class reactions{
    private:
        double c1 = 0.1, c2 = 2;
        const int tfinal = 100, X_bar = 500;
        mt19937 g;
        uniform_real_distribution<double> r;
        vector<int> Xmol, Ymol, Zmol;
        vector<double> tval;

    public:
        reactions() : g(static_cast<unsigned int> (time(0))), r(0, 1) {}

        inline int reaction1(int Y){
            return ++Y;
        }

        array<int, 2> reaction2(int Y, int Z){
            Y -= 2;
            array<int, 2> mol = {Y, ++Z};
            return mol;
        }

        array<double, 3> a(int Y){
            double a1 = c1*X_bar*Y, a2 = c2*(Y*(Y - 1))/2.0, a0;
            a0 = a1 + a2;
            array<double, 3> propensities = {a1, a2, a0};
            return propensities;
        }

        void process(){
            double t = 0;
            int Y = 10, Z = 0;
            while (t <= tfinal)
            {
                Xmol.push_back(X_bar);
                Ymol.push_back(Y);
                Zmol.push_back(Z);
                tval.push_back(t);
                double r1 = r(g), r2 = r(g);

                array<double, 3> propensities = a(Y);
                
                double T = (1/propensities[2])*log(1/r1);

                if (r2*propensities[2] <= propensities[0])
                {
                    Y = reaction1(Y);
                }
                else
                {
                    array<int, 2> molecules = reaction2(Y, Z);
                    Y = molecules[0];
                    Z = molecules[1];
                }

                t += T;
            }
            
        }

        void plot(){
            try
            {
                ofstream file("C:/Users/lenovo/OneDrive/Desktop/Coding/SIES C++/Computational peoblems/Gillespie problems/problem 1/data.txt");
                if (file.is_open())
                {
                    for (size_t i = 0; i < tval.size(); i++)
                    {
                        file<<setw(12)<<fixed<<setprecision(6)<<tval[i]<<setw(6)<<fixed<<setprecision(0)<<Xmol[i]<<setw(6)<<fixed<<setprecision(0)<<Ymol[i]<<setw(6)<<fixed<<setprecision(0)<<Zmol[i]<<endl;
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
                ofstream gp("C:/Users/lenovo/OneDrive/Desktop/Coding/SIES C++/Computational peoblems/Gillespie problems/problem 1/plot.gp");
                if (gp.is_open())
                {
                    gp<<"set terminal window enhanced font 'Times New Roman, 18'\n"<<endl;
                    gp<<"set title 'Plot of system of 2 reactions and number of its molecules over time.' font ', 30' tc rgb 'red'"<<endl;
                    gp<<"set xlabel 'time (in seconds)' tc rgb 'black'"<<endl;
                    gp<<"set ylabel 'number of mulecules' tc rgb 'black'"<<endl;
                    gp<<"set grid lt 1 lw 2 lc rgb 'gray'"<<endl;
                    gp<<"set key outside\n"<<endl;
                    gp<<"plot\\"<<endl;
                    gp<<"'data.txt' u 1:2 w l lt 1 lw 2 lc rgb 'violet' t 'Molecules of X_{bar}',\\"<<endl;
                    gp<<"'data.txt' u 1:3 w l lt 1 lw 2 lc rgb 'green' t 'Molecules of Y',\\"<<endl;
                    gp<<"'data.txt' u 1:4 w l lt 1 lw 2 lc rgb 'blue' t 'Molecules of Z'\n"<<endl;
                    gp<<"pause -1"<<endl;
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
            
        }
};

int main(){
    clock_t start = clock();
    cout<<"This Program will plot a graph of system having 2 reactions and the number of molecules as they change for reactants."<<endl;
    reactions chemical;
    chemical.process();
    chemical.plot();
    system("gnuplot plot.gp");

    clock_t end = clock();
    double duration = static_cast<double>(end - start)/CLOCKS_PER_SEC;
    cout<<"The code took "<<duration<<" seconds to run."<<endl;
    return 0;
}