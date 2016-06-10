ldc i 0
ldc i 0
ldc i 0
ssp 16
lda 0 14
ldc c 'B'
sto c
lda 0 12
ldc c 'a'
sto c
lda 0 5
ldc c 'a'
sto c
lda 0 6
ldc c 'n'
sto c
lda 0 7
ldc c 'b'
sto c
lda 0 8
ldc c 'l'
sto c
lda 0 9
ldc c 'e'
sto c
lda 0 10
ldc c 'a'
sto c
lda 0 11
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 35
ldc r 5.000000
str r 0 5
initialize element at depth 1 for array b with 'a'
initialize element at depth 1 for array b with 'b'
str a 0 6
str a 0 8
ldc c 'd'
str c 0 8
lda 0 9
ldc c 'a'
sto c
lda 0 10
ldc c 'n'
sto c
lda 0 11
ldc c 'b'
sto c
lda 0 12
ldc c 'l'
sto c
lda 0 13
ldc c 'e'
sto c
lda 0 14
ldc c 'a'
sto c
lda 0 15
ldc c 27
sto c
str a 0 16
lda 0 16
str a 0 17
lda 0 17
str a 0 18
ldc a 0
lod a 0 18
ind a
dpl a
lda 1 7
ind a
sto a
ind a
sto a
ldc a 0
lda 0 16
dpl a
lda 1 7
ind a
sto a
ind a
sto a
ldc a 0
lda 0 16
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
ldc a 0
lda 0 16
dpl a
lda 1 9
ind a
sto a
ind a
sto a
initialize element at depth 1 for array aaa with 1
initialize element at depth 1 for array aaa with 2
initialize element at depth 1 for array aaa with 3
initialize element at depth 1 for array aaa with 4
initialize element at depth 1 for array aaa with 5
str a 0 19
initialize element at depth 1 for array aaaa with 1
initialize element at depth 1 for array aaaa with 2
str a 0 24
lda 0 19
str a 0 26
ldc a 0
lda 0 26
dpl a
lda 0 24
sto a
ind a
sto a
ldc i 1
str i 0 27
ldc r 5.000000
str r 0 28
ldc r 0.0
str r 0 29
ldc r 0.0
str r 0 30
ldc a 0
lda 0 29
ldc i 0
chk 0 1
ixa 1
dpl a
lod r 0 28
sto r
ind r
sto r
ldc a 0
lda 0 29
ldc i 1
chk 0 1
ixa 1
dpl a
lod r 0 28
ldc r 1.000000
sub r
sto r
ind r
sto r
ldc a 0
lda 0 29
ldc i 2
chk 0 1
ixa 1
dpl a
lod r 0 28
ldc r 1.000000
add r
sto r
ind r
sto r
lda 0 29
str a 0 31
initialize element at depth 1 for array fltArr with 1.0
initialize element at depth 1 for array fltArr with 2.0
initialize element at depth 1 for array fltArr with 3.0
str a 0 32
ldc a 0
lda 0 31
dpl a
lda 0 32
sto a
ind a
sto a
ldc i 0
str i 0 0
retf
retf
