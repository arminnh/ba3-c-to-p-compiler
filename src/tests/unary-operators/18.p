ldc i 0
ldc i 0
ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 6
ldc i 0
str i 0 5
ldc a 0
lod i 0 5
sto i
ldc a 0
lod i 0 5
neg i
sto i
retf
