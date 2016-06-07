ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 12
ldc i 0
str i 0 5
ldc i 0
str i 0 6
ldc a 0
str a 0 7
ldc i 0
str i 0 8
ldc r 0.0
str r 0 9
ldc r 0.0
str r 0 10
ldc r 0.0
str r 0 11
ldc a 0
lod r 0 9
sto r
ldc a 0
ldc i 1
sto i
ldc a 0
lod r 0 9
ldc r 1.0
add r
sto r
ldc a 0
lda 0 5
dpl a
lod i 0 6
sto i
ind i
sto i
ldc a 0
lda 0 9
dpl a
ldc r 1.0
ldc r 2.0
mul r
sto r
ind r
sto r
ldc a 0
lda 0 10
dpl a
lod r 0 9
ldc r 0.5
sub r
ldc r 1.0
add r
sto r
ind r
sto r
ldc a 0
ldc c 'c'
sto c
ldc a 0
lda 0 5
dpl a
ldc i 5
ldc i 5
add i
lod i 0 5
add i
lod i 0 8
add i
sto i
ind i
sto i
ldc a 0
lda 0 6
dpl a
ldc i 5
ldc i 5
ldc i 5
add i
lod i 0 6
add i
mul i
lod i 0 8
add i
sto i
ind i
sto i
ldc a 0
ldc r 5.5
sto r
ldc a 0
lda 0 11
dpl a
ldc r 5.5
ldc r 5.7
ldc r 5.4
add r
lod r 0 10
add r
mul r
lod r 0 11
add r
ldc r 7.0
mul r
ldc r 5.2
sub r
sto r
ind r
sto r
ldc a 0
lda 0 11
dpl a
ldc r 5.0
ldc r 5.5
ldc r 5.6
add r
lod r 0 10
add r
mul r
lod r 0 11
add r
ldc r 7.7
mul r
ldc r 5.8
sub r
ldc r 100.0
div r
sto r
ind r
sto r
ldc a 0
lda 0 8
dpl a
ldc i 2
dpl i
ldc a 0
ldc i 1
sto i
ldc a 0
ind i
div i
ldc a 0
ind i
mul i
sub i
ldc i 2
ldc i 5
mul i
add i
ldc i 3
ldc i 4
div i
sub i
sto i
ind i
sto i
ldc a 0
ldc i 1
ldc i 2
equ i
conv b i
sto i
ldc a 0
ldc i 1
ldc i 2
leq i
conv b i
sto i
ldc a 0
ldc i 1
ldc i 2
neq i
conv b i
sto i
ldc a 0
ldc i 3
ldc i 3
equ i
conv b i
ldc i 3
equ i
conv b i
sto i
ldc a 0
lod i 0 5
conv i b
fjp l1_else
lod r 0 9
ujp l2_after_if
l1_else:
lod r 0 10
l2_after_if:
sto r
ldc a 0
lda 0 5
dpl a
ldc i 1
ldc i 2
equ i
conv b i
conv i b
fjp l3_else
ldc i 0
ujp l4_after_if
l3_else:
ldc i 1
l4_after_if:
sto i
ind i
sto i
ldc a 0
lda 0 6
dpl a
ldc i 1
ldc i 1
equ i
conv b i
conv i b
fjp l5_else
ldc i 0
ldc i 3
ldc i 8
mul i
add i
ujp l6_after_if
l5_else:
ldc i 1
ldc i 3
add i
l6_after_if:
sto i
ind i
sto i
ldc i 1
conv i b
lod i 0 5
conv i b
and
conv b i
conv i b
fjp l7_else
ldc a 0
lda 0 5
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
l7_else:
ldc i 1
conv i b
lod i 0 5
conv i b
or
conv b i
conv i b
fjp l9_else
ldc a 0
lda 0 5
dpl a
dpl a
ind i
dec i 1
sto i
ind i
inc i 1
sto i
l9_else:
ldc a 0
lod i 0 5
conv i b
lod i 0 6
conv i b
lod i 0 8
conv i b
not
conv b i
conv i b
and
conv b i
conv i b
or
conv b i
conv i b
lod i 0 6
conv i b
lod i 0 8
conv i b
and
conv b i
conv i b
not
conv b i
conv i b
or
conv b i
sto i
ldc a 0
lda 0 5
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
ind i
dec i 1
sto i
ind i
sto i
ldc a 0
lda 0 5
dpl a
dpl a
ind i
inc i 1
sto i
ind i
sto i
ldc a 0
lda 0 5
dpl a
dpl a
ind i
dec i 1
sto i
ind i
inc i 1
sto i
ldc a 0
lda 0 5
sto a
ldc a 0
lod a 0 7
ind i
sto i
ldc a 0
lod i 0 5
conv i b
not
conv b i
conv i b
lod i 0 8
conv i b
not
conv b i
conv i b
and
conv b i
sto i
lod i 0 5
conv i b
lod i 0 8
conv i b
or
conv b i
conv i b
not
conv b i
ldc a 0
lod i 0 5
conv i b
not
conv b i
conv i b
lod i 0 8
conv i b
not
conv b i
conv i b
and
conv b i
sto i
lod i 0 5
conv i b
lod i 0 6
conv i b
or
conv b i
conv i b
not
conv b i
ldc i 1
str i 0 0
retf
retf
