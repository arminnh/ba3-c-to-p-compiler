ldc i 0
ldc i 0
ldc i 0
ssp 68
lda 0 5
ldc c '\n'
sto c
lda 0 6
ldc c 'E'
sto c
lda 0 7
ldc c 'n'
sto c
lda 0 8
ldc c 't'
sto c
lda 0 9
ldc c 'e'
sto c
lda 0 10
ldc c 'r'
sto c
lda 0 11
ldc c ' '
sto c
lda 0 12
ldc c 'a'
sto c
lda 0 13
ldc c 'n'
sto c
lda 0 14
ldc c 'y'
sto c
lda 0 15
ldc c ' '
sto c
lda 0 16
ldc c 's'
sto c
lda 0 17
ldc c 't'
sto c
lda 0 18
ldc c 'r'
sto c
lda 0 19
ldc c 'i'
sto c
lda 0 20
ldc c 'n'
sto c
lda 0 21
ldc c 'g'
sto c
lda 0 22
ldc c ' '
sto c
lda 0 23
ldc c ':'
sto c
lda 0 24
ldc c ' '
sto c
lda 0 25
ldc c 27
sto c
lda 0 26
ldc c 'T'
sto c
lda 0 27
ldc c 'h'
sto c
lda 0 28
ldc c 'e'
sto c
lda 0 29
ldc c ' '
sto c
lda 0 30
ldc c 'l'
sto c
lda 0 31
ldc c 'e'
sto c
lda 0 32
ldc c 'n'
sto c
lda 0 33
ldc c 'g'
sto c
lda 0 34
ldc c 't'
sto c
lda 0 35
ldc c 'h'
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
ldc c 't'
sto c
lda 0 41
ldc c 'h'
sto c
lda 0 42
ldc c 'e'
sto c
lda 0 43
ldc c ' '
sto c
lda 0 44
ldc c 'g'
sto c
lda 0 45
ldc c 'i'
sto c
lda 0 46
ldc c 'v'
sto c
lda 0 47
ldc c 'e'
sto c
lda 0 48
ldc c 'n'
sto c
lda 0 49
ldc c ' '
sto c
lda 0 50
ldc c 's'
sto c
lda 0 51
ldc c 't'
sto c
lda 0 52
ldc c 'r'
sto c
lda 0 53
ldc c 'i'
sto c
lda 0 54
ldc c 'n'
sto c
lda 0 55
ldc c 'g'
sto c
lda 0 56
ldc c ' '
sto c
lda 0 57
ldc c '%'
sto c
lda 0 58
ldc c 's'
sto c
lda 0 59
ldc c ' '
sto c
lda 0 60
ldc c 'i'
sto c
lda 0 61
ldc c 's'
sto c
lda 0 62
ldc c ' '
sto c
lda 0 63
ldc c ':'
sto c
lda 0 64
ldc c ' '
sto c
lda 0 65
ldc c '%'
sto c
lda 0 66
ldc c 'd'
sto c
lda 0 67
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 26
ldc c 0
str c 0 5
ldc c 0
str c 0 6
ldc c 0
str c 0 7
ldc c 0
str c 0 8
ldc c 0
str c 0 9
ldc c 0
str c 0 10
ldc c 0
str c 0 11
ldc c 0
str c 0 12
ldc c 0
str c 0 13
ldc c 0
str c 0 14
ldc c 0
str c 0 15
ldc c 0
str c 0 16
ldc c 0
str c 0 17
ldc c 0
str c 0 18
ldc c 0
str c 0 19
ldc c 0
str c 0 20
ldc c 0
str c 0 21
ldc c 0
str c 0 22
ldc c 0
str c 0 23
ldc c 0
str c 0 24
ldc i 0
str i 0 25
ldc c '\n'
out c
ldc c 'E'
out c
ldc c 'n'
out c
ldc c 't'
out c
ldc c 'e'
out c
ldc c 'r'
out c
ldc c ' '
out c
ldc c 'a'
out c
ldc c 'n'
out c
ldc c 'y'
out c
ldc c ' '
out c
ldc c 's'
out c
ldc c 't'
out c
ldc c 'r'
out c
ldc c 'i'
out c
ldc c 'n'
out c
ldc c 'g'
out c
ldc c ' '
out c
ldc c ':'
out c
ldc c ' '
out c
ldc a 0
lda 0 25
dpl a
mst 1
lda 0 5
cup 1 function_string_ln
sto i
ind i
sto i
ldc c 'T'
out c
ldc c 'h'
out c
ldc c 'e'
out c
ldc c ' '
out c
ldc c 'l'
out c
ldc c 'e'
out c
ldc c 'n'
out c
ldc c 'g'
out c
ldc c 't'
out c
ldc c 'h'
out c
ldc c ' '
out c
ldc c 'o'
out c
ldc c 'f'
out c
ldc c ' '
out c
ldc c 't'
out c
ldc c 'h'
out c
ldc c 'e'
out c
ldc c ' '
out c
ldc c 'g'
out c
ldc c 'i'
out c
ldc c 'v'
out c
ldc c 'e'
out c
ldc c 'n'
out c
ldc c ' '
out c
ldc c 's'
out c
ldc c 't'
out c
ldc c 'r'
out c
ldc c 'i'
out c
ldc c 'n'
out c
ldc c 'g'
out c
ldc c ' '
out c
ldc a 1
lda 0 5
sto a
ldc a 0
ldc i 0
sto i
ldc a 1
ind a
l1_out_loop:

dpl a
ind c
ldc c 27
neq c
fjp l2_after_out_loop
dpl a
ind c
out c
inc a 1
ujp l1_out_loop
l2_after_out_loop:
ldc c ' '
out c
ldc c 'i'
out c
ldc c 's'
out c
ldc c ' '
out c
ldc c ':'
out c
ldc c ' '
out c
lod i 0 25
out i
retf

function_string_ln:
ssp 7
ldc i 0
str i 0 6
l3_while_condition:
lod a 0 5
ind c
ldc c '\0'
neq c
conv b i
conv i b
fjp l4_while_after
ldc a 0
lda 0 6
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ldc a 0
lda 0 5
dpl a
dpl a
ind a
conv a i
inc i 1
conv i a
sto a
ind a
conv a i
dec i 1
conv i a
sto a
ujp l3_while_condition
l4_while_after:
lod i 0 6
str i 0 0
retf
retf
