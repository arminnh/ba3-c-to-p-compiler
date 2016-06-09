ldc i 0
ldc i 0
ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 9
ldc i 0
str i 0 5
lod i 0 5
conv i b
not
conv b i
ldc a 0
lda 0 5
dpl a
lod i 0 5
conv i b
ldc i 5
conv i b
and
conv b i
conv i b
ldc i 3
conv i b
not
conv b i
conv i b
or
conv b i
conv i b
not
conv b i
sto i
ind i
sto i
ldc a 0
lda 0 5
sto a
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
lda 0 5
str a 0 6
ldc a 0
lda 0 5
dpl a
lod a 0 6
ind i
sto i
ind i
sto i
ldc r 7.800000
str r 0 7
lda 0 7
str a 0 8
ldc a 0
lda 0 7
dpl a
lod a 0 8
ind r
sto r
ind r
sto r
retf
