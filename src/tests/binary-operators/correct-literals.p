ldc i 0
ldc i 0
ldc i 0
ssp 9
lda 0 5
ldc c 'a'
sto c
lda 0 7
ldc c 'b'
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 5
ldc a 0
ldc i 0
ldc i 2
les i
conv b i
sto i
ldc a 0
ldc r 2.000000
ldc r 5.000000
les r
conv b i
sto i
ldc a 0
lda 1 0
lda 1 2
les c
conv b i
sto i
ldc a 0
ldc c 'B'
ldc c 'b'
les c
conv b i
sto i
ldc a 0
ldc i 0
ldc i 2
grt i
conv b i
sto i
ldc a 0
ldc r 2.000000
ldc r 5.000000
grt r
conv b i
sto i
ldc a 0
lda 1 0
lda 1 2
grt c
conv b i
sto i
ldc a 0
ldc c 'B'
ldc c 'b'
grt c
conv b i
sto i
ldc a 0
ldc i 0
ldc i 2
leq i
conv b i
sto i
ldc a 0
ldc r 2.000000
ldc r 5.000000
leq r
conv b i
sto i
ldc a 0
lda 1 0
lda 1 2
leq c
conv b i
sto i
ldc a 0
ldc c 'B'
ldc c 'b'
leq c
conv b i
sto i
ldc a 0
ldc i 0
ldc i 2
geq i
conv b i
sto i
ldc a 0
ldc r 2.000000
ldc r 5.000000
geq r
conv b i
sto i
ldc a 0
lda 1 0
lda 1 2
geq c
conv b i
sto i
ldc a 0
ldc c 'B'
ldc c 'b'
geq c
conv b i
sto i
ldc a 0
ldc i 0
ldc i 2
equ i
conv b i
sto i
ldc a 0
ldc r 2.000000
ldc r 5.000000
equ r
conv b i
sto i
ldc a 0
lda 1 0
lda 1 2
equ c
conv b i
sto i
ldc a 0
ldc c 'B'
ldc c 'b'
equ c
conv b i
sto i
ldc a 0
ldc i 0
ldc i 2
equ i
conv b i
sto i
ldc a 0
ldc r 2.000000
ldc r 5.000000
equ r
conv b i
sto i
ldc a 0
lda 1 0
lda 1 2
equ c
conv b i
sto i
ldc a 0
ldc c 'B'
ldc c 'b'
equ c
conv b i
sto i
ldc a 0
ldc i 0
ldc i 2
neq i
conv b i
sto i
ldc a 0
ldc r 2.000000
ldc r 5.000000
neq r
conv b i
sto i
ldc a 0
lda 1 0
lda 1 2
neq c
conv b i
sto i
ldc a 0
ldc c 'B'
ldc c 'b'
neq c
conv b i
sto i
ldc a 0
ldc i 0
ldc i 2
add i
sto i
ldc a 0
ldc r 2.000000
ldc r 5.000000
add r
sto r
ldc a 0
ldc c 'B'
ldc c 'b'
add c
sto c
ldc a 0
ldc i 0
ldc i 2
sub i
sto i
ldc a 0
ldc r 2.000000
ldc r 5.000000
sub r
sto r
ldc a 0
lda 1 0
lda 1 2
sub c
sto a
ldc a 0
ldc c 'B'
ldc c 'b'
sub c
sto c
ldc a 0
ldc i 0
ldc i 2
div i
sto i
ldc a 0
ldc r 2.000000
ldc r 5.000000
div r
sto r
ldc a 0
ldc c 'B'
ldc c 'b'
div c
sto c
ldc a 0
ldc i 0
ldc i 2
mul i
sto i
ldc a 0
ldc r 2.000000
ldc r 5.000000
mul r
sto r
ldc a 0
ldc c 'B'
ldc c 'b'
mul c
sto c
ldc a 0
ldc i 0
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
sto i
ldc a 0
ldc c 'B'
dpl i
ldc a 0
ldc c 'b'
sto i
ldc a 0
ind i
div i
ldc a 0
ind i
mul i
sub i
sto c
ldc a 0
ldc i 1
conv i b
ldc i 2
conv i b
or
conv b i
sto i
ldc a 0
ldc i 0
conv i b
ldc i 0
conv i b
or
conv b i
sto i
ldc a 0
ldc i 5
conv i b
ldc i 5
conv i b
or
conv b i
sto i
ldc a 0
ldc i 5
conv i b
ldc i 5
conv i b
or
conv b i
conv i b
ldc i 6
conv i b
ldc i 0
conv i b
and
conv b i
conv i b
or
conv b i
sto i
ldc a 0
ldc i 5
conv i b
ldc i 4
conv i b
and
conv b i
conv i b
ldc i 0
conv i b
or
conv b i
sto i
ldc i 1
str i 0 0
retf
retf
