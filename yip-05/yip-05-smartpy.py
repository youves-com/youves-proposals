import smartpy as sp

def execute_accept_administrator_proposal(administrable_address):
    administrable_contract = sp.contract(
        sp.TUnit, administrable_address, entry_point="acceptAdminProposal"
    ).open_some()
    return sp.transfer_operation(sp.unit, sp.mutez(0), administrable_contract)

def execute_set_reward_recipient(flat_curve_address, reward_recipient):
    flat_curve_contract = sp.contract(
        sp.TAddress, flat_curve_address, entry_point="setRewardRecipient"
    ).open_some()

    return sp.transfer_operation(reward_recipient, sp.mutez(0), flat_curve_contract)

def wire_new_dao(unit):
    sp.set_type(unit, sp.TUnit)
    NEW_REWARD_RECIPIENT = sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")

    sp.result(sp.list([
        execute_accept_administrator_proposal(sp.address("KT1UJBvm4hv11Uvu6r4c8zE5K2EfmwiRVgsm")), # UUSD/USDT
        execute_set_reward_recipient(sp.address("KT1UJBvm4hv11Uvu6r4c8zE5K2EfmwiRVgsm"), NEW_REWARD_RECIPIENT), 

        execute_accept_administrator_proposal(sp.address("KT1NgbaaYhtXh3MwJoYYxrrKUwG3RX5LYVL6")), # USDCE/UUSD
        execute_set_reward_recipient(sp.address("KT1NgbaaYhtXh3MwJoYYxrrKUwG3RX5LYVL6"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1JeWiS8j1kic4PHx7aTnEr9p4xVtJNzk5b")), # WUSDC/UUSD
        execute_set_reward_recipient(sp.address("KT1JeWiS8j1kic4PHx7aTnEr9p4xVtJNzk5b"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1STLQKxiRtAh1e7DZhu1xUTAJ7KLpV9Rru")), # UUSD/UBTC
        execute_set_reward_recipient(sp.address("KT1STLQKxiRtAh1e7DZhu1xUTAJ7KLpV9Rru"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1T974a8qau4xP3RAAWPYCZM9xtwU9FLjPS")), # tzbtc/wwbtc
        execute_set_reward_recipient(sp.address("KT1T974a8qau4xP3RAAWPYCZM9xtwU9FLjPS"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1XvH5f2ja2jzdDbv6rxPmecZFU7s3obquN")), # tzbtc/ubtc
        execute_set_reward_recipient(sp.address("KT1XvH5f2ja2jzdDbv6rxPmecZFU7s3obquN"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1CkpDuwCFrnoqTam6upYiPBiFNsSEVbBei")), # wbtc.e/ubtc
        execute_set_reward_recipient(sp.address("KT1CkpDuwCFrnoqTam6upYiPBiFNsSEVbBei"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1AVbWyM8E7DptyBCu4B5J5B7Nswkq7Skc6")), # kusd/usd
        execute_set_reward_recipient(sp.address("KT1AVbWyM8E7DptyBCu4B5J5B7Nswkq7Skc6"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1Xbx9pykNd38zag4yZvnmdSNBknmCETvQV")), # usdtz/uusd
        execute_set_reward_recipient(sp.address("KT1Xbx9pykNd38zag4yZvnmdSNBknmCETvQV"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1SPUvH5khHtirTEVeECiKrnh4FFXxWZ6ui")), # xtz/uxtz v2
        execute_set_reward_recipient(sp.address("KT1SPUvH5khHtirTEVeECiKrnh4FFXxWZ6ui"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1WgguedKZWucrdRKQXaRECEPMZennaVPck")), # xxtz/uxtz
        execute_set_reward_recipient(sp.address("KT1WgguedKZWucrdRKQXaRECEPMZennaVPck"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1Ad5yJzoiRRdMJPvhJiPJ7Cq8WbJnCS7bg")), # uusd/uxau
        execute_set_reward_recipient(sp.address("KT1Ad5yJzoiRRdMJPvhJiPJ7Cq8WbJnCS7bg"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1BFXgczFte2zftCTg7tL6Qk2capsFg6UFS")),
        execute_set_reward_recipient(sp.address("KT1BFXgczFte2zftCTg7tL6Qk2capsFg6UFS"), NEW_REWARD_RECIPIENT),

        execute_accept_administrator_proposal(sp.address("KT1PkygK9CqgNLyuJ9iMFcgx1651BrTjN1Q9")), # usdt/xtz
        execute_set_reward_recipient(sp.address("KT1PkygK9CqgNLyuJ9iMFcgx1651BrTjN1Q9"), NEW_REWARD_RECIPIENT),
    ]))