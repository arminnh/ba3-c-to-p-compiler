ldc i 0
ssp 9
lda 0 5
ldc c '%'
sto c
lda 0 6
ldc c 'c'
sto c
lda 0 7
ldc c ' '
sto c
lda 0 8
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 7
ldc i 0
str i 0 5
ldc c 0
str c 0 6
lda 0 5
dpl a
ldc i 0
sto i
ind i
l2_for_condition:
lod i 0 5
ldc i 256
les i
conv b i
conv i b
fjp l3_for_after
lod c 0 6
out c
ldc c ' '
out c
ldc a 0
lda 0 6
dpl a
lod c 0 6
conv c i
ldc i 1
add i
conv i c
sto c
ind c
sto c
l1_for_iteration:
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
ujp l2_for_condition
l3_for_after:
retp
