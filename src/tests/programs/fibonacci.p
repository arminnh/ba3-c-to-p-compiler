ldc i 0
ssp 89
lda 0 5
ldc c 'f'
sto c
lda 0 6
ldc c 'i'
sto c
lda 0 7
ldc c 'b'
sto c
lda 0 8
ldc c ' '
sto c
lda 0 9
ldc c 'o'
sto c
lda 0 10
ldc c 'f'
sto c
lda 0 11
ldc c ' '
sto c
lda 0 12
ldc c '1'
sto c
lda 0 13
ldc c ':'
sto c
lda 0 14
ldc c ' '
sto c
lda 0 15
ldc c '%'
sto c
lda 0 16
ldc c 'i'
sto c
lda 0 17
ldc c '\n'
sto c
lda 0 18
ldc c 27
sto c
lda 0 19
ldc c 'f'
sto c
lda 0 20
ldc c 'i'
sto c
lda 0 21
ldc c 'b'
sto c
lda 0 22
ldc c ' '
sto c
lda 0 23
ldc c 'o'
sto c
lda 0 24
ldc c 'f'
sto c
lda 0 25
ldc c ' '
sto c
lda 0 26
ldc c '2'
sto c
lda 0 27
ldc c ':'
sto c
lda 0 28
ldc c ' '
sto c
lda 0 29
ldc c '%'
sto c
lda 0 30
ldc c 'i'
sto c
lda 0 31
ldc c '\n'
sto c
lda 0 32
ldc c 27
sto c
lda 0 33
ldc c 'f'
sto c
lda 0 34
ldc c 'i'
sto c
lda 0 35
ldc c 'b'
sto c
lda 0 36
ldc c ' '
sto c
lda 0 37
ldc c 'o'
sto c
lda 0 38
ldc c 'f'
sto c
lda 0 39
ldc c ' '
sto c
lda 0 40
ldc c '3'
sto c
lda 0 41
ldc c ':'
sto c
lda 0 42
ldc c ' '
sto c
lda 0 43
ldc c '%'
sto c
lda 0 44
ldc c 'i'
sto c
lda 0 45
ldc c '\n'
sto c
lda 0 46
ldc c 27
sto c
lda 0 47
ldc c 'f'
sto c
lda 0 48
ldc c 'i'
sto c
lda 0 49
ldc c 'b'
sto c
lda 0 50
ldc c ' '
sto c
lda 0 51
ldc c 'o'
sto c
lda 0 52
ldc c 'f'
sto c
lda 0 53
ldc c ' '
sto c
lda 0 54
ldc c '4'
sto c
lda 0 55
ldc c ':'
sto c
lda 0 56
ldc c ' '
sto c
lda 0 57
ldc c '%'
sto c
lda 0 58
ldc c 'i'
sto c
lda 0 59
ldc c '\n'
sto c
lda 0 60
ldc c 27
sto c
lda 0 61
ldc c 'f'
sto c
lda 0 62
ldc c 'i'
sto c
lda 0 63
ldc c 'b'
sto c
lda 0 64
ldc c ' '
sto c
lda 0 65
ldc c 'o'
sto c
lda 0 66
ldc c 'f'
sto c
lda 0 67
ldc c ' '
sto c
lda 0 68
ldc c '5'
sto c
lda 0 69
ldc c ':'
sto c
lda 0 70
ldc c ' '
sto c
lda 0 71
ldc c '%'
sto c
lda 0 72
ldc c 'i'
sto c
lda 0 73
ldc c '\n'
sto c
lda 0 74
ldc c 27
sto c
lda 0 75
ldc c 'f'
sto c
lda 0 76
ldc c 'i'
sto c
lda 0 77
ldc c 'b'
sto c
lda 0 78
ldc c ' '
sto c
lda 0 79
ldc c 'o'
sto c
lda 0 80
ldc c 'f'
sto c
lda 0 81
ldc c ' '
sto c
lda 0 82
ldc c '6'
sto c
lda 0 83
ldc c ':'
sto c
lda 0 84
ldc c ' '
sto c
lda 0 85
ldc c '%'
sto c
lda 0 86
ldc c 'i'
sto c
lda 0 87
ldc c '\n'
sto c
lda 0 88
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_fib:
ssp 6
lod i 0 5
ldc i 0
equ i
conv b i
conv i b
lod i 0 5
ldc i 1
equ i
conv b i
conv i b
or
conv b i
conv i b
fjp l1_else
ldc i 1
str i 0 0
retf
l1_else:
mst 1
lod i 0 5
ldc i 1
sub i
cup 1 function_fib
mst 1
lod i 0 5
ldc i 2
sub i
cup 1 function_fib
add i
str i 0 0
retf
retf

function_main:
ssp 5
ldc c 'f'
out c
ldc c 'i'
out c
ldc c 'b'
out c
ldc c ' '
out c
ldc c 'o'
out c
ldc c 'f'
out c
ldc c ' '
out c
ldc c '1'
out c
ldc c ':'
out c
ldc c ' '
out c
mst 1
ldc i 1
cup 1 function_fib
out i
ldc c '\n'
out c
ldc c 'f'
out c
ldc c 'i'
out c
ldc c 'b'
out c
ldc c ' '
out c
ldc c 'o'
out c
ldc c 'f'
out c
ldc c ' '
out c
ldc c '2'
out c
ldc c ':'
out c
ldc c ' '
out c
mst 1
ldc i 2
cup 1 function_fib
out i
ldc c '\n'
out c
ldc c 'f'
out c
ldc c 'i'
out c
ldc c 'b'
out c
ldc c ' '
out c
ldc c 'o'
out c
ldc c 'f'
out c
ldc c ' '
out c
ldc c '3'
out c
ldc c ':'
out c
ldc c ' '
out c
mst 1
ldc i 3
cup 1 function_fib
out i
ldc c '\n'
out c
ldc c 'f'
out c
ldc c 'i'
out c
ldc c 'b'
out c
ldc c ' '
out c
ldc c 'o'
out c
ldc c 'f'
out c
ldc c ' '
out c
ldc c '4'
out c
ldc c ':'
out c
ldc c ' '
out c
mst 1
ldc i 4
cup 1 function_fib
out i
ldc c '\n'
out c
ldc c 'f'
out c
ldc c 'i'
out c
ldc c 'b'
out c
ldc c ' '
out c
ldc c 'o'
out c
ldc c 'f'
out c
ldc c ' '
out c
ldc c '5'
out c
ldc c ':'
out c
ldc c ' '
out c
mst 1
ldc i 5
cup 1 function_fib
out i
ldc c '\n'
out c
ldc c 'f'
out c
ldc c 'i'
out c
ldc c 'b'
out c
ldc c ' '
out c
ldc c 'o'
out c
ldc c 'f'
out c
ldc c ' '
out c
ldc c '6'
out c
ldc c ':'
out c
ldc c ' '
out c
mst 1
ldc i 6
cup 1 function_fib
out i
ldc c '\n'
out c
ldc i 0
str i 0 0
retf
retf
