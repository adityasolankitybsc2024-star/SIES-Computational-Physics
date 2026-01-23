set terminal window enhanced font 'Arial, 18'

set title 'Plot of inverse square + Gaussian function' tc rgb 'red' font ', 30'
set xlabel 'xvalues' tc rgb 'red'
set ylabel 'yvalues' tc rgb 'red'
unset key
set grid lt 1 lw 1 lc rgb 'gray'

plot 'data.txt' u 1:2 w l lt 7 lw 2 lc rgb 'blue'

pause -1
