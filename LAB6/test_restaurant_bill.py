
import pytest
from restaurant_bill import bill_total, split_bill, table_wait

# ---------------- BILL TOTAL TESTS ----------------

def test_dine_in_bill():
    assert bill_total("dine_in", 1000, 2, False) == 1155

def test_takeaway_bill():
    assert bill_total("takeaway", 500, 2, False) == 525

def test_rooftop_bill():
    assert bill_total("rooftop", 1000, 2, False) == 1207

def test_happy_hour():
    assert bill_total("dine_in", 1000, 2, True) == 924

def test_happy_hour_takeaway():
    assert bill_total("takeaway", 500, 2, True) == 525

def test_large_group():
    assert bill_total("dine_in", 1000, 8, False) == 1365

def test_invalid_section():
    with pytest.raises(ValueError):
        bill_total("garden", 100, 2, False)

def test_negative_food_total():
    with pytest.raises(ValueError):
        bill_total("dine_in", -100, 2, False)

def test_invalid_guests():
    with pytest.raises(ValueError):
        bill_total("dine_in", 100, 0, False)


# ---------------- SPLIT BILL TESTS ----------------

def test_even_split():
    assert split_bill(1000, 4, 10) == 275

def test_uneven_split():
    assert split_bill(100, 3, 0) == 34

def test_invalid_people():
    with pytest.raises(ValueError):
        split_bill(100, 0, 10)

def test_negative_tip():
    with pytest.raises(ValueError):
        split_bill(100, 2, -5)


# ---------------- TABLE WAIT TESTS ----------------

def test_large_party():
    assert table_wait(13, 5, False) == "call ahead"

def test_reservation():
    assert table_wait(4, 0, True) == "seat now"

def test_no_free_tables():
    assert table_wait(4, 0, False) == "waitlist"

def test_large_party_limited_tables():
    assert table_wait(8, 1, False) == "waitlist"

def test_small_party_available_table():
    assert table_wait(4, 1, False) == "seat now"
