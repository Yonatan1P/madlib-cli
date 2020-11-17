import pytest
from madlib_cli.madlib import read_file, parse_file, merge


def test_read_file_return_template():
    actual = read_file('madlib_cli/template_madlib.txt')
    expected = "Make Me A Video Game! I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}! What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."
    assert actual == expected


def test_parse_file_return_dissected_string_and_parts():
    actual = parse_file("Make Me A Video Game! I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}! What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.")
    expected_dissected = "Make Me A Video Game! I the {} and {} {} have {}{}'s {} sister and plan to steal her {} {}! What are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {} Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find."
    expected_parts = ["Adjective", "Adjective", "A First Name", "Past Tense Verb", "A First Name", "Adjective", "Adjective", "Plural Noun", "Large Animal", "Small Animal", "A Girl's Name", "Adjective", "Plural Noun", "Adjective", "Plural Noun", "Number 1-50", "First Name's", "Number", "Plural Noun", "Number", "Plural Noun"]
    assert actual == [expected_dissected, expected_parts]


def test_merge():
    actual = merge("Make Me A Video Game! I the {} and {} {} have {}{}'s {} sister and plan to steal her {} {}! What are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {} Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find.", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"])
    expected = "Make Me A Video Game! I the 1 and 2 3 have 45's 6 sister and plan to steal her 7 8! What are a 9 and backpacking 10 to do? Before you can help 11, you'll have to collect the 12 13 and 14 15 that open up the 16 worlds connected to A 17 Lair. There are 18 19 and 20 21 in the game, along with hundreds of other goodies for you to find."
    assert actual == expected
