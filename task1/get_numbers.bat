python main.py /g:lc /f:out1.txt /n:10000 /i: 3 10 764 1 /m:100
python main.py /g:add /n:10000 /f:out2.txt /i: 7 107 1 3 5 2 4 6 /m:100
python main.py /g:5p /f:out3.txt  /n:10000 /i: 8 5 1 3 7 12 /m:100
python main.py /g:lfsr /f:out4.txt /n:10000 /i: 100000001001001 0011000000 /m:10000
python main.py /g:nfsr /f:out5.txt /n:10000 /i: 00000001 00000001 00000001 8 00000011 00000011 00000011 /m:10000
python main.py /g:mt /f:out6.txt /n:10000 /i: 1024 17461461673 /m:10000
python main.py /g:rc4 /f:out7.txt /n:10000 /i: 9 86 114 217 41 207 80 50 231 180 228 211 103 48 90 105 120 237 240 253 118 187 230 21 144 117 26 252 226 87 191 19 65 71 236 147 248 36 84 245 178 208 210 64 176 42 66 166 51 7 12 222 206 162 229 18 129 9 13 34 213 101 216 20 89 112 56 215 171 95 239 72 94 30 106 141 63 33 235 138 93 212 85 104 61 238 44 10 193 70 124 116 81 68 243 99 155 74 24 196 160 125 158 165 122 205 29 223 140 186 254 249 188 137 123 174 173 185 214 246 115 46 14 17 11 60 37 164 3 97 6 35 108 119 43 153 146 255 200 136 31 58 5 27 151 57 242 22 190 109 47 224 143 184 232 227 149 163 96 110 142 82 111 49 203 69 98 126 38 113 28 15 195 55 67 40 159 88 152 100 194 102 52 250 218 1 167 169 0 83 189 179 247 177 181 168 75 198 92 91 134 148 161 241 32 183 130 77 175 78 2 133 127 39 244 221 54 234 8 139 201 251 62 4 192 16 107 157 59 121 204 156 25 145 73 202 172 154 131 128 220 79 209 219 197 132 225 45 23 135 233 53 199 76 150 170 182 /m:100
python main.py /g:rsa /f:out8.txt /n:10000 /i: 12709189 53 245 10 /m:10000
python main.py /g:bbs /f:out9.txt /n:10000 /i:21 /m:10000


