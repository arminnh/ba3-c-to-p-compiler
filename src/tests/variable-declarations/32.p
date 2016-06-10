ldc i 0
ldc i 0
ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 8
lod i 0 5
str i 0 5
lod i 0 6
lod i 0 6
add i
str i 0 6
lda 0 7
dpl a
dpl a
ind c
inc c 1
sto c
ind c
dec c 1
str c 0 7
retf
