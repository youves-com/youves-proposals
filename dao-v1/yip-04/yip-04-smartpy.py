import smartpy as sp

def execute_propose_flat_swap_administrator(administrable_address, new_admin):
    administrable_contract = sp.contract(
        sp.TAddress,
        administrable_address,
        entry_point="proposeNewAdmin",
    ).open_some()
    return sp.transfer_operation(new_admin, sp.mutez(0), administrable_contract)

def execute_update_max_release_period(contract_address, new_max_release_period):
    contract_ep = sp.contract(
        sp.TNat, contract_address, entry_point="update_max_release_period"
    ).open_some()

    return sp.transfer_operation(new_max_release_period, sp.mutez(0), contract_ep)

def execute_set_checker_admin(administrable_address, new_admin):
    administrable_contract = sp.contract(
        sp.TAddress,
        administrable_address,
        entry_point="set_admin",
    ).open_some()
    return sp.transfer_operation(new_admin, sp.mutez(0), administrable_contract)

def YIP_04(unit):
    sp.set_type(unit, sp.TUnit)

    NEW_YOUVES_DAO = sp.address("KT1T3BFEu9WSQyRuV9Fyd7SqTU4rW3ptJ3NN")
    sp.result(sp.list([
        execute_propose_flat_swap_administrator(sp.address("KT1UJBvm4hv11Uvu6r4c8zE5K2EfmwiRVgsm"), NEW_YOUVES_DAO), # UUSD/USDT
        execute_propose_flat_swap_administrator(sp.address("KT1NgbaaYhtXh3MwJoYYxrrKUwG3RX5LYVL6"), NEW_YOUVES_DAO), # USDCE/UUSD
        execute_propose_flat_swap_administrator(sp.address("KT1JeWiS8j1kic4PHx7aTnEr9p4xVtJNzk5b"), NEW_YOUVES_DAO), # WUSDC/UUSD
        execute_propose_flat_swap_administrator(sp.address("KT1STLQKxiRtAh1e7DZhu1xUTAJ7KLpV9Rru"), NEW_YOUVES_DAO), # UUSD/UBTC
        execute_propose_flat_swap_administrator(sp.address("KT1T974a8qau4xP3RAAWPYCZM9xtwU9FLjPS"), NEW_YOUVES_DAO), # tzbtc/wwbtc
        execute_propose_flat_swap_administrator(sp.address("KT1XvH5f2ja2jzdDbv6rxPmecZFU7s3obquN"), NEW_YOUVES_DAO), # tzbtc/ubtc
        execute_propose_flat_swap_administrator(sp.address("KT1CkpDuwCFrnoqTam6upYiPBiFNsSEVbBei"), NEW_YOUVES_DAO), # wbtc.e/ubtc
        execute_propose_flat_swap_administrator(sp.address("KT1AVbWyM8E7DptyBCu4B5J5B7Nswkq7Skc6"), NEW_YOUVES_DAO), # kusd/usd
        execute_propose_flat_swap_administrator(sp.address("KT1Xbx9pykNd38zag4yZvnmdSNBknmCETvQV"), NEW_YOUVES_DAO), # usdtz/uusd
        execute_propose_flat_swap_administrator(sp.address("KT1SPUvH5khHtirTEVeECiKrnh4FFXxWZ6ui"), NEW_YOUVES_DAO), # xtz/uxtz v2
        execute_propose_flat_swap_administrator(sp.address("KT1WgguedKZWucrdRKQXaRECEPMZennaVPck"), NEW_YOUVES_DAO), # xxtz/uxtz
        execute_propose_flat_swap_administrator(sp.address("KT1Ad5yJzoiRRdMJPvhJiPJ7Cq8WbJnCS7bg"), NEW_YOUVES_DAO), # uusd/uxau
        execute_propose_flat_swap_administrator(sp.address("KT1BFXgczFte2zftCTg7tL6Qk2capsFg6UFS"), NEW_YOUVES_DAO),

        execute_set_checker_admin(sp.address("KT1LrEJsaTR5vMdwjvASTtFPUbk2wnX3P166"), NEW_YOUVES_DAO),
        execute_update_max_release_period(sp.address("KT1UZcNDxTdkn33Xx5HRkqQoZedc3mEs11yV"), sp.nat(1)), 
    ]))