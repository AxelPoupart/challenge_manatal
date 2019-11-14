import random


class Lottery(object):

    def __init__(self, total_balls=50, total_draw=10):
        self.total_balls = total_balls
        self.total_draw = total_draw
        self.balls = list(range(1, total_balls + 1))

    def make_draws(self):
        draws = random.sample(self.balls, k=self.total_draw)
        draws.sort()
        return draws


lot = Lottery()
print(lot.make_draws())


def test_lottery(total_balls=50, total_draw=10):
    lot = Lottery(total_balls, total_draw)
    sorted_draws = lot.make_draws()
    if len(sorted_draws) != total_draw:
        raise ValueError('The number of draws is incorrect')
    if total_draw == 1:
        return 'Test passed successfully'
    else:
        e = sorted_draws[0]
        for k in sorted_draws[1:]:
            if e > k:
                raise ValueError(
                    'The list is not sorted or there is repeated values')
            e = k
        return 'Test passed successfully'


print(test_lottery())

# To check if the randomness is good we could do a statistics survey on a high number of draws.
