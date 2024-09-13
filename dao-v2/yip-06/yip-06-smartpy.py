import smartpy as sp
import utils.addresses as addresses

def set_target_swap_oracle(swap, oracle):
    swap_ep = sp.contract(
        sp.TAddress,
        swap,
        entry_point="setTargetOracle"
    ).open_some(message="Invalid entrypoint: setTargetOracle")
    return sp.transfer_operation(oracle, sp.mutez(0), swap_ep)

def execute_set_contracts_checker(
    engine_address,
    ctez,
    ctez_cfmm,
    governance,
    liquidation_tracker,
    oracle,
    reward_pool
):
    engine_contract = sp.contract(
        sp.TPair(
            sp.TPair(
                sp.TPair(sp.TAddress, sp.TAddress),
                sp.TPair(sp.TAddress, sp.TAddress)
            ),
            sp.TPair(sp.TAddress, sp.TAddress)),
        engine_address,
        entry_point="set_contracts"
    ).open_some()

    payload = sp.pair(
        sp.pair(
            sp.pair(ctez, ctez_cfmm),
            sp.pair(governance, liquidation_tracker)
        ),
        sp.pair(oracle, reward_pool)
    )
    return sp.transfer_operation(payload, sp.mutez(0), engine_contract)

def execute_set_reward_recipient(flat_curve_address, reward_recipient):
    flat_curve_contract = sp.contract(
        sp.TAddress, flat_curve_address, entry_point="setRewardRecipient"
    ).open_some()

    return sp.transfer_operation(reward_recipient, sp.mutez(0), flat_curve_contract)

def update_target_flat_curve_oracles(unit):
    sp.set_type(unit, sp.TUnit)
    sp.result(sp.list([
        set_target_swap_oracle(
            addresses.UUSD_UBTC_EXCHANGE,
            sp.address("KT1Cy1wwHbW1NMawnQCrfXMBtuwXSsidEDg2")
        ),
        execute_set_reward_recipient(
            sp.address("KT1CkpDuwCFrnoqTam6upYiPBiFNsSEVbBei"), 
            sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")),
        execute_set_reward_recipient(
            sp.address("KT1WgguedKZWucrdRKQXaRECEPMZennaVPck"), 
            sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")),
        execute_set_reward_recipient(
            sp.address("KT1Ad5yJzoiRRdMJPvhJiPJ7Cq8WbJnCS7bg"), 
            sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")),
        execute_set_reward_recipient(
            sp.address("KT1SPUvH5khHtirTEVeECiKrnh4FFXxWZ6ui"), 
            sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")),
        execute_set_reward_recipient(
            sp.address("KT1PkygK9CqgNLyuJ9iMFcgx1651BrTjN1Q9"), 
            sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")),
        execute_set_reward_recipient(
            sp.address("KT1STLQKxiRtAh1e7DZhu1xUTAJ7KLpV9Rru"),
            sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")),
        execute_set_reward_recipient(
            sp.address("KT1AVbWyM8E7DptyBCu4B5J5B7Nswkq7Skc6"), 
            sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")),
        execute_set_reward_recipient(
            sp.address("KT1Xbx9pykNd38zag4yZvnmdSNBknmCETvQV"), 
            sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")),
        execute_set_reward_recipient(
            sp.address("KT1XvH5f2ja2jzdDbv6rxPmecZFU7s3obquN"),
            sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")),
        execute_set_reward_recipient(
            sp.address("KT1UJBvm4hv11Uvu6r4c8zE5K2EfmwiRVgsm"),
            sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")),
        
        execute_set_contracts_checker(
            engine_address = sp.address("KT1LrEJsaTR5vMdwjvASTtFPUbk2wnX3P166"),
            ctez = sp.address("KT1SjXiUX63QvdNMcM2m492f7kuf8JxXRLp4"),
            ctez_cfmm = sp.address("KT1LpDGYxbpabK3A6rqpVW4TSwVjwg9Zjp7K"),
            governance = sp.address("KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4"),
            liquidation_tracker = sp.address("KT1PJkeVGVJAH4LRjWRbLU39D9EY7GkTfibQ"),
            oracle = sp.address("KT1TYSXHmkGu7QSsiQKCahWpKtG3JtFgN2kf"),
            reward_pool = sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB")
        )
    ]))
