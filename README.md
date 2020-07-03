# :abacus: Matrix Processor
### *Recommended for anyone studying Matrices & Determinants during Online Classes :sunglasses:* 

[![Run on Repl.it](https://repl.it/badge/github/PseudoCodeNerd/matrix-processor)](https://repl.it/github/PseudoCodeNerd/matrix-processor)

This program can accomplish tasks such as addition, subtraction and multiplication of matrices along with finding determinants and inverses of a matrix. *May be* pretty helplful in online classes to calculate on the fly. 
It can calculate ~85 % of NCERT questions. Trust me, I myself have used this in my math class and the teacher was really impressed.

**MVP: Finding Inverse**

# Usage
- **Cut / copy code source from `processor.py`** and paste to run via your favourite editor.
- **repl.it button** 

# Demo
1. Matrix Multiplication
```console
Numeric Matrix Processor

1. Add Matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: > 3
Enter size of first matrix: > 3 3
Enter first matrix: 
> 1 7 7
> 6 6 4
> 4 2 1
Enter size of second matrix: > 3 3
Enter second matrix: 
> 3 2 4
> 5 5 9
> 8 0 10
The result is: 
94 37 137
80 42 118
30 18 44
```
2. Finding inverse of a really complex matrix to show how cool this is.
    - Answer is correct. I checked on Wolfram-Alpha :-)
  
```console

Numeric Matrix Processor

1. Add Matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: > 6
Enter matrix size: > 4 4
Enter matrix: 
> 2.65 3.54 3.88 8.99
> 3.12 5.45 7.77 5.56
> 5.31 2.23 2.33 9.81
> 1.67 1.67 1.01 9.99
The result is: 
0.397 -0.215 0.277  -0.509
5.197 -2.07  -0.389 -3.143
-3.38  1.502  0.16   2.048
-0.593 0.23   0.003  0.503
```

## Contributing
The code may (most certainly) have bugs. Please feel free to open up an issue describing how I messed up (in a polite way please.) 

- `soumitradev` helped with initial testing and maintaining the repo.
- `bangyen`

--- 

## ToDo
- Add comments
- Beautify output
- Better error handling for `make()`
- Look into operations on 2x2 matrices.

