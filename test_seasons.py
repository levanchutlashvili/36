import seasons

def test_minutes_to_words():
    # test that function returns correct output for various input values
    assert seasons.minutes_to_words(0) == "zero minutes"
    assert seasons.minutes_to_words(1) == "one minutes"
    assert seasons.minutes_to_words(60) == "one hours zero minutes"
    assert seasons.minutes_to_words(90) == "one hours thirty minutes"
    assert seasons.minutes_to_words(121) == "two hours one minutes"