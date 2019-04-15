# MAXIMUM LOAD
:floppy_disk: Created with Python 3.7.0, 64-bit, with Visual Studio Code, MacOS Mojave 10.14.3

The program calculates the maximum load that can be placed on top of a given wall.

Author: _Pawel Flajszer, April 2019, pflajszer@gmail.com_ :envelope:

## Requirements:

In order to run the application please install the following modules:
- **re**, version==**2.2.1**
- **sys**, version==**3.7.0**

## Usage:

The application takes two command line arguments:
- the path to the text file formatted as a "wall" in ```*.txt``` file with extension included
  (if the file is not located in the same folder as the program make sure to use an absolute path).
- the initial position to start measuring maximum load for the given wall (index ```0``` starts at ```1``` as per specification)

Example usage:  

	Pawels-MacBook-Pro:~ username$ python application.py wall0.txt 10

	Pawels-MacBook-Pro:~ username$ python application.py /Users/Username/Desktop/brick_problem/textfile.txt 20

## Performance:

:chart_with_upwards_trend: Notation: ```O(2^n)```

The algorithm used is of type brute force. It finds every possible pathway from the initial brick to the bottom of the wall
by checking every possible combination of every brick through 2 bricks directly below.

For "wall input of 10 rows the cProfile returns:

           7171 function calls (7163 primitive calls) in 0.008 seconds

       Ordered by: internal time

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         3584    0.003    0.000    0.003    0.000 application.py:84(pathways)
            1    0.002    0.002    0.008    0.008 application.py:102(main)
           22    0.001    0.000    0.001    0.000 {method 'split' of 're.Pattern' objects}
          512    0.001    0.000    0.001    0.000 application.py:91(calculations)
            1    0.001    0.001    0.001    0.001 {method 'read' of '_io.TextIOWrapper' objects}
          512    0.000    0.000    0.000    0.000 application.py:77(pathway_last_two_rows)
    1604/1600    0.000    0.000    0.000    0.000 {built-in method builtins.len}



For "wall input of 20 rows the cProfile returns:

	        12059229 function calls (12059221 primitive calls) in 11.918 seconds

       Ordered by: internal time

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      8912896    7.328    0.000    7.337    0.000 application.py:84(pathways)
            1    2.390    2.390   11.444   11.444 application.py:102(main)
       524288    1.217    0.000    1.217    0.000 application.py:91(calculations)
       524288    0.243    0.000    0.271    0.000 application.py:77(pathway_last_two_rows)
    1572942/1572938    0.109    0.000    0.109    0.000 {built-in method builtins.len}
            1    0.106    0.106    0.106    0.106 {method 'sort' of 'list' objects}
       524367    0.044    0.000    0.044    0.000 {method 'append' of 'list' objects}
            1    0.021    0.021   11.465   11.465 application.py:9(<module>)
           42    0.005    0.000    0.005    0.000 {method 'split' of 're.Pattern' objects}
            1    0.001    0.001    0.001    0.001 {method 'read' of '_io.TextIOWrapper' objects}

```application.py:84(pathways)``` uses the most computing power and should be optimised for larger inputs.

:bulb: The performance drops significantly with larger inputs. With this in mind, the used algorithm needs to perform
2^100 main loops for the 100 row input (given in the _Bonus Task_). That is 1,267,650,600,228,229,401,496,703,205,376, or
one nonillion, 267 octillion, 650 septillion, 600 sextillion, 228 quintillion, 229 quadrillion, 401 trillion, 496 billion, 703 million, 205 thousand, 376 loops. Needless to say it would be unwise to hold your breath for the runtime.
**I'm currently working on the better algorithm to solve much larger problems in a reasonable runtime.**

## TODO

Possible improvements:
- efficiency enhancement (optimise pathway(), or change approach)
- Increase readability
- OO approach


Bugs:
- None :+1:


 
