from primes import is_prime

def test_is_prime():
    assert is_prime(2)
    assert is_prime(3) 
    assert not is_prime(4)
    assert is_prime(5) 
    assert not is_prime(6) 
    assert is_prime(7) 
    assert not is_prime(8)
    assert not is_prime(9) 
