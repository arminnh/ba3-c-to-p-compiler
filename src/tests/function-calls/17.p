ldc i 0
ldc i 0
ldc i 0
ssp 48
lda 0 34
ldc c '%'
sto c
lda 0 35
ldc c 'i'
sto c
lda 0 36
ldc c ' '
sto c
lda 0 37
ldc c '%'
sto c
lda 0 38
ldc c 'd'
sto c
lda 0 39
ldc c ' '
sto c
lda 0 40
ldc c '%'
sto c
lda 0 41
ldc c 'i'
sto c
lda 0 42
ldc c '\n'
sto c
lda 0 43
ldc c 27
sto c
lda 0 44
ldc c '%'
sto c
lda 0 45
ldc c 's'
sto c
lda 0 46
ldc c '\n'
sto c
lda 0 47
ldc c 27
sto c
lda 0 21
ldc c '%'
sto c
lda 0 22
ldc c 's'
sto c
lda 0 23
ldc c ' '
sto c
lda 0 24
ldc c '%'
sto c
lda 0 25
ldc c 'd'
sto c
lda 0 26
ldc c ' '
sto c
lda 0 27
ldc c '%'
sto c
lda 0 28
ldc c 'i'
sto c
lda 0 29
ldc c ' '
sto c
lda 0 30
ldc c '%'
sto c
lda 0 31
ldc c 's'
sto c
lda 0 32
ldc c '\n'
sto c
lda 0 33
ldc c 27
sto c
lda 0 15
ldc c 'h'
sto c
lda 0 16
ldc c 'e'
sto c
lda 0 17
ldc c 'l'
sto c
lda 0 18
ldc c 'l'
sto c
lda 0 19
ldc c 'o'
sto c
lda 0 20
ldc c 27
sto c
lda 0 5
ldc c 'w'
sto c
lda 0 6
ldc c 'o'
sto c
lda 0 7
ldc c 'r'
sto c
lda 0 8
ldc c 'l'
sto c
lda 0 9
ldc c 'd'
sto c
lda 0 10
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 8
ldc i 1
str i 0 5
ldc i 2
str i 0 6
str a 0 7
ldc a 1
lda 1 15
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
ldc c '\n'
out c
ldc a 1
lda 1 15
sto a
ldc a 0
ldc i 0
sto i
ldc a 1
ind a
l3_out_loop:

dpl a
ind c
ldc c 27
neq c
fjp l4_after_out_loop
dpl a
ind c
out c
inc a 1
ujp l3_out_loop
l4_after_out_loop:
ldc c ' '
out c
lod i 0 5
out i
ldc c ' '
out c
lod i 0 6
out i
ldc c ' '
out c
ldc a 1
lda 1 5
sto a
ldc a 0
ldc i 0
sto i
ldc a 1
ind a
l5_out_loop:

dpl a
ind c
ldc c 27
neq c
fjp l6_after_out_loop
dpl a
ind c
out c
inc a 1
ujp l5_out_loop
l6_after_out_loop:
ldc c '\n'
out c
lod i 0 5
out i
ldc c ' '
out c
lod i 0 6
out i
ldc c ' '
out c
ldc c ' '
out c
ldc c '%'
out c
ldc c 'i'
out c
ldc c '\n'
out c
ldc c '%'
out c
ldc c 's'
out c
ldc c '\n'
out c
ldc i 0
str i 0 0
retf
retf
