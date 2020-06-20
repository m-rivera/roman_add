"""Unit tests for converting between Roman and Arabic numerals."""
import pytest
import subprocess
import roman_add.src.roman_maths as rm
# sample numbers and their equivalents
num_equiv = (('I', 1),
             ('IV', 4),
             ('XIX', 19),
             ('CMXCIX', 999),
             ('MMMCCX', 3210))

# sample Roman sums in the format (A,B,A+B)
sums = (('I', 'II', 'III'),  # 1 + 2 = 3
        ('IV', 'V', 'IX'),  # 4 + 5 = 9
        ('V', 'IV', 'IX'),  # 5 + 4 = 9
        ('XIX', 'CMXCIX', 'MXVIII'))  # 19 + 999 = 1018


@pytest.mark.parametrize("rom,ara", num_equiv)
def test_ara_to_rom(rom, ara):
    """Test Arabic -> Roman"""
    calc_rom = rm.ara_to_rom(ara)
    assert calc_rom == rom


@pytest.mark.parametrize("rom,ara", num_equiv)
def test_rom_to_ara(rom, ara):
    """Test Roman -> Arabic"""
    calc_ara = rm.rom_to_ara(rom)
    assert calc_ara == ara


def test_rom_to_ara_wrong_char():
    """Test exception catch for non-Roman character input"""
    with pytest.raises(ValueError) as e_info:
        rm.rom_to_ara("Not Roman letters")
    assert "Non-Roman characters" in str(e_info.value)


def test_rom_to_ara_wrong_order():
    """Test exception catch for non-standard character order"""
    with pytest.raises(ValueError) as e_info:
        rm.rom_to_ara("IIX")
    assert "Non-standard character order" in str(e_info.value)


@pytest.mark.parametrize("rom_a,rom_b,rom_ab", sums)
def test_add_rom(rom_a, rom_b, rom_ab):
    """Test adding Roman numerals together"""
    sum_rom = rm.rom_add(rom_a, rom_b)
    assert sum_rom == rom_ab


@pytest.mark.parametrize("rom_a,rom_b,rom_ab", sums)
def test_functional(capfd, rom_a, rom_b, rom_ab):
    """Test the program from end to end"""
    proc = subprocess.Popen('add_roman.py ' + rom_a + ' ' + rom_b, shell=True)
    proc.wait()
    result = capfd.readouterr().out.rstrip()
    assert result == rom_ab
