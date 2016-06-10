ldc i 0
ldc i 0
ldc i 0
ssp 25
lda 0 13
ldc c '%'
sto c
lda 0 14
ldc c 'i'
sto c
lda 0 15
ldc c '\n'
sto c
lda 0 16
ldc c 27
sto c
lda 0 17
ldc c '%'
sto c
lda 0 18
ldc c 'i'
sto c
lda 0 19
ldc c ','
sto c
lda 0 20
ldc c ' '
sto c
lda 0 21
ldc c '%'
sto c
lda 0 22
ldc c 'i'
sto c
lda 0 23
ldc c '\n'
sto c
lda 0 24
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 218
ldc i 0
str i 0 5
ldc i 0
str i 0 6
ldc i 0
str i 0 7
ldc i 0
str i 0 8
ldc i 0
str i 0 9
ldc i 0
str i 0 10
ldc i 0
str i 0 11
ldc i 0
str i 0 12
ldc i 0
str i 0 13
ldc i 0
str i 0 14
ldc i 0
str i 0 15
ldc i 0
str i 0 16
ldc i 0
str i 0 17
ldc i 0
str i 0 18
ldc i 0
str i 0 19
ldc i 0
str i 0 20
ldc i 0
str i 0 21
ldc i 0
str i 0 22
ldc i 0
str i 0 23
ldc i 0
str i 0 24
ldc i 0
str i 0 25
ldc i 0
str i 0 26
ldc i 0
str i 0 27
ldc i 0
str i 0 28
ldc i 0
str i 0 29
ldc i 0
str i 0 30
ldc i 0
str i 0 31
ldc i 0
str i 0 32
ldc i 0
str i 0 33
ldc i 0
str i 0 34
ldc i 0
str i 0 35
ldc i 0
str i 0 36
ldc i 0
str i 0 37
ldc i 0
str i 0 38
ldc i 0
str i 0 39
ldc i 0
str i 0 40
ldc i 0
str i 0 41
ldc i 0
str i 0 42
ldc i 0
str i 0 43
ldc i 0
str i 0 44
ldc i 0
str i 0 45
ldc i 0
str i 0 46
ldc i 0
str i 0 47
ldc i 0
str i 0 48
ldc i 0
str i 0 49
ldc i 0
str i 0 50
ldc i 0
str i 0 51
ldc i 0
str i 0 52
ldc i 0
str i 0 53
ldc i 0
str i 0 54
ldc i 0
str i 0 55
ldc i 0
str i 0 56
ldc i 0
str i 0 57
ldc i 0
str i 0 58
ldc i 0
str i 0 59
ldc i 0
str i 0 60
ldc i 0
str i 0 61
ldc i 0
str i 0 62
ldc i 0
str i 0 63
ldc i 0
str i 0 64
ldc i 0
str i 0 65
ldc i 0
str i 0 66
ldc i 0
str i 0 67
ldc i 0
str i 0 68
ldc i 0
str i 0 69
ldc i 0
str i 0 70
ldc i 0
str i 0 71
ldc i 0
str i 0 72
ldc i 0
str i 0 73
ldc i 0
str i 0 74
ldc i 0
str i 0 75
ldc i 0
str i 0 76
ldc i 0
str i 0 77
ldc i 0
str i 0 78
ldc i 0
str i 0 79
ldc i 0
str i 0 80
ldc i 0
str i 0 81
ldc i 0
str i 0 82
ldc i 0
str i 0 83
ldc i 0
str i 0 84
ldc i 0
str i 0 85
ldc i 0
str i 0 86
ldc i 0
str i 0 87
ldc i 0
str i 0 88
ldc i 0
str i 0 89
ldc i 0
str i 0 90
ldc i 0
str i 0 91
ldc i 0
str i 0 92
ldc i 0
str i 0 93
ldc i 0
str i 0 94
ldc i 0
str i 0 95
ldc i 0
str i 0 96
ldc i 0
str i 0 97
ldc i 0
str i 0 98
ldc i 0
str i 0 99
ldc i 0
str i 0 100
str a 0 101
str a 0 125
str a 0 131
str a 0 135
lda 0 131
ind a
ind a
ldc i 1
add i
ind i
out i
ldc c '\n'
out c
lda 0 131
ldc i 0
chk 0 3
ixa 2
ldc i 1
chk 0 1
ixa 1
ldc i 0
chk 0 0
ixa 1
ind i
out i
ldc c '\n'
out c
lda 0 135
ldc i 1
add i
ind i
ldc i 1
add i
out i
ldc c '\n'
out c
ldc i 5
str i 0 138
lda 0 138
str a 0 139
lda 0 139
str a 0 140
str a 0 141
str a 0 151
ldc a 0
lda 0 151
ldc i 0
chk 0 1
ixa 1
dpl a
lda 0 141
sto a
ind a
sto a
ldc a 0
str a 0 153
ldc a 0
str a 0 154
str a 0 155
lda 0 131
ldc i 0
chk 0 3
ixa 2
ldc i 1
chk 0 1
ixa 1
ldc i 0
chk 0 0
ixa 1
ind i
out i
ldc c ','
out c
ldc c ' '
out c
lda 0 131
ldc i 0
chk 0 3
ixa 2
ldc i 1
chk 0 1
ixa 1
ldc i 1
chk 0 0
ixa 1
ind i
out i
ldc c '\n'
out c
ldc i 1
str i 0 205
ldc i 2
str i 0 206
str a 0 207
str a 0 209
str a 0 218
retf
