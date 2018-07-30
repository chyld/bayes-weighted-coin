from src.bayescoin import BayesCoin

bc = BayesCoin()
bc.choose_coin()

for i in range(10):
    side = bc.flip_coin()
    bc.update_priors(side)
