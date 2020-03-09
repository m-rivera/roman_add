"""
Module compiling functions to convert between Arabic and Roman numerals.

Here, we adhere to the subtractive Roman numeral syntax (the one where IV
corresponds to 4, IX to 9 and so on).

"""

# conversion chart between reference Roman numerals and Arabic equivalents
# not using just a dictionary since they are unordered before Python 3.7
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
