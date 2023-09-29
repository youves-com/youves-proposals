import smartpy as sp

def execute_set_swap_fee_ratio(swap_address, fee_numerator, fee_denominator):
    change_fee_ep = sp.contract(
        sp.TPair(sp.TNat, sp.TNat), swap_address, entry_point="changeFee"
    ).open_some()
    payload = sp.pair(fee_numerator, fee_denominator)

    return sp.transfer_operation(payload, sp.mutez(0), change_fee_ep)

def execute_set_contracts_engine_v3(
    engine_address,
    interest_rate_setter_contract,
    options_contract,
    governance_token_contract,
    savings_pool_contract,
    target_price_oracle,
    reward_pool_contract,
):

    engine_contract = sp.contract(
        sp.TPair(
            sp.TPair(sp.TAddress, sp.TPair(sp.TAddress, sp.TAddress)),
            sp.TPair(sp.TAddress, sp.TPair(sp.TAddress, sp.TAddress)),
        ),
        engine_address,
        entry_point="set_contracts",
    ).open_some()

    payload = sp.pair(
        sp.pair(
            governance_token_contract,
            sp.pair(interest_rate_setter_contract, options_contract),
        ),
        sp.pair(
            reward_pool_contract, sp.pair(savings_pool_contract, target_price_oracle)
        ),
    )

    return sp.transfer_operation(payload, sp.mutez(0), engine_contract)
def DAO_YIP_3(unit):
    sp.set_type(unit, sp.TUnit)

    new_uxtz_xtz_pool = sp.address('KT1SPUvH5khHtirTEVeECiKrnh4FFXxWZ6ui') # Address of the new uXTZ/XTZ constant function market maker.
    sp.result(sp.list([
        execute_set_swap_fee_ratio(
            sp.address('KT1BFXgczFte2zftCTg7tL6Qk2capsFg6UFS'), # old uxtz-xtz pool
            100,
            100,
        ),
        execute_set_contracts_engine_v3(
            sp.address('KT1AnDFRcdB652Jy5JFtmu7SampSPAzDkK7g'), # uXTZ/USDt collateral engine
            sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'), # youves DAO as interest rate setter (remains the same)
            sp.address('KT1BUR5mjwBWzojKRqWrng8ASBh3N3LLV7NM'), # options contract (remains the same)
            sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'), # stake manager (remains the same)
            new_uxtz_xtz_pool, # interest receiver (previously was the old uxtz/xtz pool)
            sp.address('KT1PvKziQx7pJhfr3FdvkhMPwCwLxjd32HkZ'), # target price oracle (remains the same)
            sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'), # unified staking proxy as rewards receiver (remains the same)
        ),
        execute_set_contracts_engine_v3(
            sp.address('KT1Mf9Nr1KyGC6gUz9pGQnngzWbbZ6thShvc'), # uXTZ/XTZ collateral engine
            sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'), # youves DAO as interest rate setter (remains the same)
            sp.address('KT1GL6CBm93edDHogUVQzasUd6m7384eZk3J'), # options contract
            sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'), # stake manager (remains the same)
            new_uxtz_xtz_pool, # interest receiver (previously was the old uxtz/xtz pool)
            sp.address('KT1PuCU5UAoaX2Hjcns2SEmJWBC34tfLjzaS'), # target price oracle (remains the same)
            sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'), # unified staking proxy as rewards receiver (remains the same)
        ),
        execute_set_contracts_engine_v3(
            sp.address('KT1ByNrcyDxYLmamuJbeFJukYkLJaZ1W86Yr'), # uXTZ/SIRS collateral engine
            sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'), # youves DAO as interest rate setter (remains the same)
            sp.address('KT1CHL9XVrt3Avr1mHkCiZBANEeJzbUSGqGB'), # options contract
            sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'), # stake manager (remains the same)
            new_uxtz_xtz_pool, # interest receiver (previously was the old uxtz/xtz pool)
            sp.address('KT1TSwSAU1qUyRFYBv6ix5YzqLBparxJ3FAk'), # target price oracle (remains the same)
            sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'), # unified staking proxy as rewards receiver (remains the same)
        ),
    ]))
