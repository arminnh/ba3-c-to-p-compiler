ldc i 0
ldc i 0
ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_f:
ssp 6
lda 0 5
ind a
ldc i 0
ixa 1
ind i
lda 0 5
ind a
ldc i 1
ixa 1
ind i
add i
lda 0 5
ind a
ldc i 2
ixa 1
ind i
add i
str i 0 0
retf
retf

function_main:
ssp 8
initialize element at depth 1 for array a with 1
initialize element at depth 1 for array a with 2
initialize element at depth 1 for array a with 3
str a 0 5
ldc a 0
lda 0 5
ldc i 2
chk 0 2
ixa 1
dpl a
lda 0 5
lda 0 5
ldc i 1
chk 0 2
ixa 1
ind i
ldc i 1
sub i
chk 0 2
ixa 1
ind i
sto i
ind i
sto i
ldc a 0
lda 0 5
ldc i 1
chk 0 2
ixa 1
dpl a
mst 1
lda 0 5
cup 1 function_f
sto i
ind i
sto i
ldc i 0
str i 0 0
retf
retf