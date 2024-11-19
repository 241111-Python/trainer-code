import unittest

# in baseball an inning has 3 outs (technically 6 because it is two half innings)
# a pitcher who has pitched 2 innings has been in the game for 6 outs
# in baseball record keeping, decimals are used if the pithcer is replaced mid inning
# a pitcher who pitched 3.2 innings has been in the game for 11 outs
# 3*3 +2 = 11         three full innings plus two extra outs = 11 total outs
# write a function that takes in the innings and gives back the total outs

class InvalidInnning(Exception):
    pass

def inning_to_outs(innings):
    valid_partial_innings = ["0", "1", "2"]
    total_innings = 0
    try:
        innings_str = str(innings)
        innings_split = innings_str.split('.')

        if len(innings_split) > 2:
            raise InvalidInnning

        full_innings = innings_split[0]
        total_innings += 3 * int(full_innings)

        if len(innings_split) == 2:

            partial_innings = innings_split[1]

            if partial_innings not in valid_partial_innings:
                raise InvalidInnning

            total_innings += int(partial_innings)
    except InvalidInnning as e:
        print("Invalid innings!")

    return total_innings


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_outs_1(self):
        outs = inning_to_outs(4.2)
        assert outs == 14

    def test_outs_2(self):
        outs = inning_to_outs(2)
        assert outs == 6

    def test_outs_3(self):
        outs = inning_to_outs(0.1)
        assert outs == 1

    def test_outs_4(self):
        try:
            inning_to_outs(4.15)
        except InvalidInnning as e:
            assert e.message == 'Invalid intermediary value: 4.15'
    
    def test_outs_5(self):
        try:
            inning_to_outs(-6)
        except InvalidInnning as e:
            assert e.message == 'Negative value not allowed'

if __name__ == '__main__':
    unittest.main()
