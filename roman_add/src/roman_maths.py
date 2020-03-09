"""Module compiling functions to convert between arabic and roman numerals."""

# conversion chart between atomic Roman numerals and Arabic equivalents
# not using just a dictionary since they are unordered before Python 3.7
conv_chart = (('M',1000),
                ('CM',900),
                ('D',500),
                ('CD',400),
                ('C',100),
                ('XC',90),
                ('L',50),
                ('XL',40),
                ('X',10),
                ('IX',9),
                ('V',5),
                ('IV',4),
                ('I',1))
