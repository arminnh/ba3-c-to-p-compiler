ldc i 0
ldc i 0
ldc i 0
ssp 65
lda 0 11
ldc c '5'
sto c
lda 0 12
ldc c 27
sto c
lda 0 7
ldc c 'a'
sto c
lda 0 8
ldc c 'a'
sto c
lda 0 9
ldc c 'a'
sto c
lda 0 10
ldc c 27
sto c
lda 0 59
ldc c 'a'
sto c
lda 0 60
ldc c 'b'
sto c
lda 0 61
ldc c 'c'
sto c
lda 0 62
ldc c 27
sto c
lda 0 20
ldc c 'h'
sto c
lda 0 21
ldc c 'e'
sto c
lda 0 22
ldc c 'l'
sto c
lda 0 23
ldc c 'l'
sto c
lda 0 24
ldc c 'o'
sto c
lda 0 25
ldc c 27
sto c
lda 0 26
ldc c 'h'
sto c
lda 0 27
ldc c 'i'
sto c
lda 0 28
ldc c 'e'
sto c
lda 0 29
ldc c 'r'
sto c
lda 0 30
ldc c ' '
sto c
lda 0 31
ldc c 'h'
sto c
lda 0 32
ldc c 'e'
sto c
lda 0 33
ldc c 'b'
sto c
lda 0 34
ldc c 'b'
sto c
lda 0 35
ldc c 'e'
sto c
lda 0 36
ldc c 'n'
sto c
lda 0 37
ldc c ' '
sto c
lda 0 38
ldc c 'w'
sto c
lda 0 39
ldc c 'e'
sto c
lda 0 40
ldc c ' '
sto c
lda 0 41
ldc c 'a'
sto c
lda 0 42
ldc c 'a'
sto c
lda 0 43
ldc c 'n'
sto c
lda 0 44
ldc c ' '
sto c
lda 0 45
ldc c 'g'
sto c
lda 0 46
ldc c 'e'
sto c
lda 0 47
ldc c 'd'
sto c
lda 0 48
ldc c 'a'
sto c
lda 0 49
ldc c 'c'
sto c
lda 0 50
ldc c 'h'
sto c
lda 0 51
ldc c 't'
sto c
lda 0 52
ldc c 27
sto c
lda 0 53
ldc c 'n'
sto c
lda 0 54
ldc c 'e'
sto c
lda 0 55
ldc c 'w'
sto c
lda 0 56
ldc c 's'
sto c
lda 0 57
ldc c 't'
sto c
lda 0 58
ldc c 27
sto c
lda 0 13
ldc c 's'
sto c
lda 0 14
ldc c 't'
sto c
lda 0 15
ldc c 'r'
sto c
lda 0 16
ldc c 'i'
sto c
lda 0 17
ldc c 'n'
sto c
lda 0 18
ldc c 'g'
sto c
lda 0 19
ldc c 27
sto c
ldc i 10
str i 0 5
ldc i 11
str i 0 6
ldc i 1
str i 0 63
ldc i 2
str i 0 64
mst 0
cup 0 function_main
hlt

function_func:
ssp 5
ldc i 1
str i 0 0
retf
retf

function_main:
ssp 137
mst 1
cup 0 function_func
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
ldc i 1
ldc i 6
str i 0 15
lod r 0 16
str r 0 16
ldc r 3.000000
str r 0 17
ldc r 1.000000
str r 0 18
ldc r 7.000000
str r 0 19
ldc r 8.000000
str r 0 20
ldc c 'a'
str c 0 21
str a 0 22
ldc i 1
str i 0 23
ldc i 2
str i 0 24
ldc i 3
str i 0 25
ldc i 5
str i 0 26
ldc i 1
str i 0 27
ldc i 2
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
ldc i 1
str i 0 34
ldc i 2
str i 0 35
ldc i 3
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
ldc i 1
str i 0 48
ldc i 2
str i 0 49
ldc i 6
str i 0 50
ldc i 0
str i 0 51
ldc i 2
str i 0 52
ldc i 1
str i 0 53
ldc i 1
str i 0 54
ldc i 2
lod i 0 15
mul i
str i 0 55
ldc i 3
str i 0 56
ldc i 4
lod i 0 51
mul i
ldc i 4
add i
str i 0 57
ldc i 5
str i 0 58
lod i 1 5
str i 0 59
lod i 1 6
str i 0 60
ldc i 0
str i 0 61
ldc a 0
str a 0 62
ldc a 0
str a 0 63
ldc i 0
str i 0 64
ldc a 0
str a 0 65
ldc a 0
str a 0 66
ldc a 0
str a 0 67
ldc a 0
str a 0 68
ldc a 0
str a 0 69
lda 0 70
ldc c '5'
sto c
lda 0 71
ldc c 27
sto c
ldc c 'c'
str c 0 72
str a 0 73
ldc a 0
lda 0 70
dpl a
ldc c 'u'
sto c
ind c
sto c
lda 0 15
str i 0 74
ldc c '5'
str c 0 75
lda 0 76
ldc c 'h'
sto c
lda 0 77
ldc c 'e'
sto c
lda 0 78
ldc c 'l'
sto c
lda 0 79
ldc c 'l'
sto c
lda 0 80
ldc c 'o'
sto c
ldc c 'c'
str c 0 81
str a 0 82
lda 0 83
ldc c 'h'
sto c
lda 0 84
ldc c 'i'
sto c
lda 0 85
ldc c 'e'
sto c
lda 0 86
ldc c 'r'
sto c
lda 0 87
ldc c ' '
sto c
lda 0 88
ldc c 'h'
sto c
lda 0 89
ldc c 'e'
sto c
lda 0 90
ldc c 'b'
sto c
lda 0 91
ldc c 'b'
sto c
lda 0 92
ldc c 'e'
sto c
lda 0 93
ldc c 'n'
sto c
lda 0 94
ldc c ' '
sto c
lda 0 95
ldc c 'w'
sto c
lda 0 96
ldc c 'e'
sto c
lda 0 97
ldc c ' '
sto c
lda 0 98
ldc c 'a'
sto c
lda 0 99
ldc c 'a'
sto c
lda 0 100
ldc c 'n'
sto c
lda 0 101
ldc c ' '
sto c
lda 0 102
ldc c 'g'
sto c
lda 0 103
ldc c 'e'
sto c
lda 0 104
ldc c 'd'
sto c
lda 0 105
ldc c 'a'
sto c
lda 0 106
ldc c 'c'
sto c
lda 0 107
ldc c 'h'
sto c
lda 0 108
ldc c 't'
sto c
lda 0 109
ldc c 27
sto c
ldc i 5
str i 0 110
lda 0 110
str i 0 111
lda 0 76
str a 0 112
ldc a 0
lda 0 112
dpl a
dpl a
ind a
conv a i
inc i 1
conv i a
sto a
ind a
conv a i
dec i 1
conv i a
sto a
ldc a 0
lda 0 76
dpl a
ldc c 'u'
sto c
ind c
sto c
ldc i 1
str i 0 113
ldc i 2
str i 0 114
ldc i 1
str i 0 115
ldc i 2
str i 0 116
ldc a 0
lda 0 112
dpl a
lda 1 53
sto a
ind a
sto a
ldc a 0
str a 0 117
ldc i 1
str i 0 118
ldc i 2
str i 0 119
ldc i 3
str i 0 120
ldc a 0
lda 0 117
dpl a
lda 0 118
sto a
ind a
sto a
ldc a 0
str a 0 121
ldc i 0
str i 0 122
ldc i 0
str i 0 123
ldc i 0
str i 0 124
ldc i 1
str i 0 125
ldc i 2
str i 0 126
ldc i 3
str i 0 127
ldc i 1
str i 0 128
ldc i 2
str i 0 129
ldc i 3
str i 0 130
lda 0 131
ldc c 'a'
sto c
lda 0 132
ldc c 'b'
sto c
lda 0 133
ldc c 'c'
sto c
lda 0 134
ldc c 27
sto c
lda 0 135
ldc c 27
sto c
str a 0 136
ldc i 0
str i 0 0
retf
retf
