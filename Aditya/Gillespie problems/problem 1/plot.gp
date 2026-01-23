set terminal window enhanced font 'Times New Roman, 18'

set title 'Plot of system of 2 reactions and number of its molecules over time.' font ', 30' tc rgb 'red'
set xlabel 'time (in seconds)' tc rgb 'black'
set ylabel 'number of mulecules' tc rgb 'black'
set grid lt 1 lw 2 lc rgb 'gray'
set key outside

plot\
'data.txt' u 1:2 w l lt 1 lw 2 lc rgb 'violet' t 'Molecules of X_{bar}',\
'data.txt' u 1:3 w l lt 1 lw 2 lc rgb 'green' t 'Molecules of Y',\
'data.txt' u 1:4 w l lt 1 lw 2 lc rgb 'blue' t 'Molecules of Z'

pause -1
