"""
Module compiling functions to convert between Arabic and Roman numerals.

Here, we adhere to the subtractive Roman numeral syntax (the one where IV
corresponds to 4, IX to 9 and so on). Additionally, since there is no
reference Roman numeral above M:1000, for numbers larger than 3999, we adopt
the convention that additional 'M's represent further multiples of 1000, thus
departing from the strict subtractive style.

"""

# conversion chart between reference Roman numerals and Arabic equivalents
# not using just a dictionary since they are unordered before Python 3.7
# in future, if the required compatibility changes from 3.X to 3.7+, we can get
# away with a single dictionary
conv_chart = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))

# still need a dictionary for easier lookup
dic_conv_chart = dict(conv_chart)

def ara_to_rom(ara_in):
    """
    Convert an Arabic number to its Roman equivalent.

    Parameters
    ----------
    ara_in : int
        The input Arabic numeral (standard in English)
    Returns
    -------
    rom_out : str
        The corresponding Roman numeral

    """

    rom_out = ''

    # cycle through reference Roman nums starting from the largest and
    # progressively convert the input
    for entry in conv_chart:
        # while the reference Roman num can still be subtracted from the input
        while ara_in >= entry[1]:
            # converting to int ensures compatibility with Python 3
            count = int(ara_in / entry[1])
            # append the Roman numeral as many times as required
            rom_out += count * entry[0]
            # update the input number
            ara_in -= count * entry[1]
    return rom_out

def rom_to_ara(rom_in):
    """
    Convert a Roman number to its Arabic equivalent.

    Parameters
    ----------
    rom_in : str
        The input Roman numeral
    Returns
    -------
    ara_out : int
        The corresponding Arabic numeral

    """

    # check that all of the characters in the string are Roman style
    for char in rom_in:
        if char not in dic_conv_chart.keys():
            raise ValueError("Non-Roman characters in: " + rom_in)

    ara_out = 0

    # cycle through all characters except the last one
    for i,char in enumerate(rom_in[:-1]):
        current_num = dic_conv_chart[char]
        next_num = dic_conv_chart[rom_in[i+1]]
        # if the following number is larger than the current, subtract current
        if current_num < next_num:
            ara_out -= current_num
        # else add it
        else:
            ara_out += current_num
    # add the final number regardless
    ara_out += dic_conv_chart[rom_in[-1]]

    # check if the characters were in a sensible order in the first place by
    # converting back to Roman
    if ara_to_rom(ara_out) != rom_in:
        raise ValueError("Non-standard character order in: " + rom_in)

    return ara_out
