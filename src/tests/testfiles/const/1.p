ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 9
ldc i 5
str i 0 5
lod i 0 5
ldc i 2
add i
str i 0 6
ldc a 0
lda 0 5
dpl a
ldc i 6
sto i
ind i
sto i
ldc a 0
lda 0 5
dpl a
lod i 0 6
sto i
ind i
sto i
lda 0 5
str a 0 7
ldc a 0
lda 0 5
dpl a
lod a 0 7
ind i
sto i
ind i
sto i
lda 0 5
str a 0 8
ldc a 0
lda 0 7
dpl a
lod a 0 8
sto a
ind a
sto a
ldc a 0
lod a 0 8
dpl a
lod i 0 6
sto i
ind i
sto i
retf
