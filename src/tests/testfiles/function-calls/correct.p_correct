ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_a:
ssp 6
ldc i 0
str i 0 0
retf
retf

function_b:
ssp 5
ldc i 0
str i 0 0
retf
retf

function_c:
ssp 7
ldc i 0
str i 0 0
retf
retf

function_d:
ssp 7
ldc i 0
str i 0 0
retf
retf

function_e:
ssp 7
ldc i 0
str i 0 0
retf
retf

function_g:
ssp 10
ldc i 0
str i 0 0
retf
retf

function_main:
ssp 7
ldc a 0
mst 1
ldc i 5490
cup 1 function_a
sto i
ldc a 0
mst 1
cup 0 function_b
sto i
ldc a 0
mst 1
ldc i 5
ldc r 5e-36
cup 2 function_c
sto i
ldc a 0
mst 1
ldc i 3
ldc i 4
cup 2 function_d
sto i
ldc a 0
mst 1
ldc r 3.0
ldc r 7e-09
cup 2 function_e
sto i
ldc a 0
str a 0 5
ldc a 0
str a 0 6
ldc a 0
mst 1
ldc c 't'
ldc i 4
ldc i 3
sub i
ldc i 5
add i
dpl i
ldc a 0
ldc i 2
sto i
ldc a 0
ind i
div i
ldc a 0
ind i
mul i
sub i
lod a 0 6
ind r
lod a 0 5
ind a
lda 0 6
cup 5 function_g
sto i
retf
