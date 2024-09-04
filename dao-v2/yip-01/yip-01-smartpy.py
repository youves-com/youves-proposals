import smartpy as sp

def execute_accept_administrator_proposal(administrable_address):
    administrable_contract = sp.contract(
        sp.TUnit, administrable_address, entry_point="acceptAdminProposal"
    ).open_some()
    return sp.transfer_operation(sp.unit, sp.mutez(0), administrable_contract)

def YIP5(unit):
    sp.set_type(unit, sp.TUnit)

    sp.result(sp.list([
        execute_accept_administrator_proposal(sp.address("KT1UJBvm4hv11Uvu6r4c8zE5K2EfmwiRVgsm")), # UUSD/USDT
        execute_accept_administrator_proposal(sp.address("KT1NgbaaYhtXh3MwJoYYxrrKUwG3RX5LYVL6")), # USDCE/UUSD
        execute_accept_administrator_proposal(sp.address("KT1JeWiS8j1kic4PHx7aTnEr9p4xVtJNzk5b")), # WUSDC/UUSD
        execute_accept_administrator_proposal(sp.address("KT1STLQKxiRtAh1e7DZhu1xUTAJ7KLpV9Rru")), # UUSD/UBTC
        execute_accept_administrator_proposal(sp.address("KT1T974a8qau4xP3RAAWPYCZM9xtwU9FLjPS")), # tzbtc/wwbtc
        execute_accept_administrator_proposal(sp.address("KT1XvH5f2ja2jzdDbv6rxPmecZFU7s3obquN")), # tzbtc/ubtc
        execute_accept_administrator_proposal(sp.address("KT1CkpDuwCFrnoqTam6upYiPBiFNsSEVbBei")), # wbtc.e/ubtc
        execute_accept_administrator_proposal(sp.address("KT1AVbWyM8E7DptyBCu4B5J5B7Nswkq7Skc6")), # kusd/usd
        execute_accept_administrator_proposal(sp.address("KT1Xbx9pykNd38zag4yZvnmdSNBknmCETvQV")), # usdtz/uusd
        execute_accept_administrator_proposal(sp.address("KT1SPUvH5khHtirTEVeECiKrnh4FFXxWZ6ui")), # xtz/uxtz v2
        execute_accept_administrator_proposal(sp.address("KT1WgguedKZWucrdRKQXaRECEPMZennaVPck")), # xxtz/uxtz
        execute_accept_administrator_proposal(sp.address("KT1Ad5yJzoiRRdMJPvhJiPJ7Cq8WbJnCS7bg")), # uusd/uxau
        execute_accept_administrator_proposal(sp.address("KT1BFXgczFte2zftCTg7tL6Qk2capsFg6UFS")),
        execute_accept_administrator_proposal(sp.address("KT1PkygK9CqgNLyuJ9iMFcgx1651BrTjN1Q9")), # usdt/xtz
    ]))
