"""Unit tests for converting between Toman and Arabic numerals."""
import pytest
import roman_add.src.roman_maths as rm

# sample numbers
num_equiv = (('I',1),
            ('IV',4),
            ('XIX',19),
            ('CMXCIX',999),
            ('MMMCCX',3210))

@pytest.mark.parametrize("rom,ara", num_equiv)
def test_ara_to_rom(rom,ara):
    """Test Arabic -> Roman"""
    calc_rom = rm.ara_to_rom(ara)
    assert calc_rom == rom

@pytest.mark.parametrize("rom,ara", num_equiv)
def test_rom_to_ara(rom,ara):
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

def test_add_rom():
    """Test adding Roman numerals together"""
    # 19 + 36 = 55
    sum_rom = rm.rom_add('XIX', 'XXXVI')

    assert sum_rom == 'LV'
