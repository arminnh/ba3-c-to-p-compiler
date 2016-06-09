ldc i 0
ldc i 0
ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 8
ldc i 0
str i 0 5
ldc a 0
str a 0 6
ldc a 0
str a 0 7
ldc a 0
lod i 0 5
sto i
ldc a 0
lod a 0 6
sto a
ldc a 0
lod a 0 7
sto a
ldc i 0
str i 0 0
retf
retf
