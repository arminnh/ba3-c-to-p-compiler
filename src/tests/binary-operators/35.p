ldc i 0
ldc i 0
ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 10
ldc a 0
ldc i 5
sto i
ldc i 6
str i 0 5
ldc i 0
str i 0 6
ldc a 0
ldc a 0
ldc a 0
ldc i 1
sto i
ldc i 2
sto i
ldc i 3
sto i
ldc a 0
ldc a 0
ldc i 1
sto i
ldc a 0
ldc i 2
sto i
ldc i 3
sto i
ldc i 0
str i 0 7
ldc i 0
str i 0 8
ldc a 0
ldc a 0
lda 0 5
dpl a
ldc i 5
sto i
ind i
sto i
lda 0 8
dpl a
ldc i 6
sto i
ind i
sto i
ldc a 0
lod i 0 5
sto i
lod i 0 8
str i 0 9
ldc i 0
str i 0 0
retf
retf
