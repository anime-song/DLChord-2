from dlchord2.parser.quality_parser import QualityParser

test_quality_pattern = {
    # qualities, tensions, tensions_parentheses, add_tensions
    '5': ([], ["5"], [], []),
    # 3 notes
    '': ([], [], [], []),
    'm': (["m"], [], [], []),
    'dim': (["dim"], [], [], []),
    'aug': (["aug"], [], [], []),
    'sus2': (["sus"], ["2"], [], []),
    'sus4': (["sus"], ["4"], [], []),
    # 4 notes
    '6': ([], ["6"], [], []),
    '7': ([], ["7"], [], []),
    'M7': (["M"], ["7"], [], []),
    'm6': (["m"], ["6"], [], []),
    'm7': (["m"], ["7"], [], []),
    'mM7': (["m", "M"], ["7"], [], []),
    '7-5': ([], ["7", "-5"], [], []),
    'M7-5': (["M"], ["7", "-5"], [], []),
    'm7-5': (["m"], ["7", "-5"], [], []),
    'mM7-5': (["m", "M"], ["7", "-5"], [], []),
    'aug7': (["aug"], ["7"], [], []),
    'augM7': (["aug", "M"], ["7"], [], []),
    'aug(b9)': (["aug"], [], ["b9"], []),
    '7sus4': (["sus"], ["7", "4"], [], []),
    'dim7': (["dim"], ["7"], [], []),
    'add9': ([], [], [], ["9"]),
    'add11': ([], [], [], ["11"]),
    'madd9': (["m"], [], [], ["9"]),

    # 5 notes
    '69': ([], ["6", "9"], [], []),
    '7(9)': ([], ["7"], ["9"], []),
    '7(13)': ([], ["7"], ["13"], []),
    '7(b9)': ([], ["7"], ["b9"], []),
    '7(#9)': ([], ["7"], ["#9"], []),
    '7(#11)': ([], ["7"], ["#11"], []),
    '7(b13)': ([], ["7"], ["b13"], []),
    '7-5(9)': ([], ["7", "-5"], ["9"], []),
    '7-5(#9)': ([], ["7", "-5"], ["#9"], []),
    '7-5(b13)': ([], ["7", "-5"], ["b13"], []),
    'M7(9)': (["M"], ["7"], ["9"], []),
    'M7(13)': (["M"], ["7"], ["13"], []),
    'M7(#11)': (["M"], ["7"], ["#11"], []),
    'M7(b9)': (["M"], ["7"], ["b9"], []),
    'm69': (["m"], ["6", "9"], [], []),
    'm7(9)': (["m"], ["7"], ["9"], []),
    'm7(11)': (["m"], ["7"], ["11"], []),
    'm7(13)': (["m"], ["7"], ["13"], []),
    'm7(b9)': (["m"], ["7"], ["b9"], []),
    'm7-5(9)': (["m"], ["7", "-5"], ["9"], []),
    'm7-5(11)': (["m"], ["7", "-5"], ["11"], []),
    'mM7(9)': (["m", "M"], ["7"], ["9"], []),
    'mM7(13)': (["m", "M"], ["7"], ["13"], []),
    'aug7(9)': (["aug"], ["7"], ["9"], []),
    'augM7(#9)': (["aug", "M"], ["7"], ["#9"], []),

    # 6 notes
    '7(9, 11)': ([], ["7"], ["9", "11"], []),
    '7(9, 13)': ([], ["7"], ["9", "13"], []),
    '7(9, b13)': ([], ["7"], ["9", "b13"], []),
    '7(9, #11)': ([], ["7"], ["9", "#11"], []),
    '7(b9, 13)': ([], ["7"], ["b9", "13"], []),
    '7(b9, b13)': ([], ["7"], ["b9", "b13"], []),
    '7(b9, #9)': ([], ["7"], ["b9", "#9"], []),
    '7(b9, #11)': ([], ["7"], ["b9", "#11"], []),
    '7(#9, 13)': ([], ["7"], ["#9", "13"], []),
    '7(#9, b13)': ([], ["7"], ["#9", "b13"], []),
    '7(#9, #11)': ([], ["7"], ["#9", "#11"], []),
    '7(#11, 13)': ([], ["7"], ["#11", "13"], []),
    'm7(9, 11)': (["m"], ["7"], ["9", "11"], []),
    'm7(9, 13)': (["m"], ["7"], ["9", "13"], []),
    'M7(9, 11)': (["M"], ["7"], ["9", "11"], []),
    'M7(9, 13)': (["M"], ["7"], ["9", "13"], []),
    # 7 notes
    '7(9, 11, 13)': ([], ["7"], ["9", "11", "13"], []),
    '7(9, #11, 13)': ([], ["7"], ["9", "#11", "13"], []),
    '7(b9, #11, 13)': ([], ["7"], ["b9", "#11", "13"], []),
    'm7(9, 11, 13)': (["m"], ["7"], ["9", "11", "13"], []),
    'M7(9, 11, 13)': (["M"], ["7"], ["9", "11", "13"], []),
}


def test_parse():
    parser = QualityParser()

    for quality in test_quality_pattern:
        quality_data = parser.parse(quality)

        qualities, tensions, tensions_parentheses, add_tensions = test_quality_pattern[quality]
        assert set(qualities) == set(quality_data.qualities)
        assert set(tensions) == set(quality_data.tensions)
        assert set(tensions_parentheses) == set(quality_data.tensions_parentheses)
        assert set(add_tensions) == set(quality_data.add_tensions)