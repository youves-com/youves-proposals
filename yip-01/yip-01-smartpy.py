import smartpy as sp

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

def DAO_YIP_2(unit):
    sp.set_type(unit, sp.TUnit)

    ###############################################################################
    # Update the release period for uXTZ/XTZ farm and uXTZ savings pool constants #
    ###############################################################################
    farm_entrypoint = sp.contract(
        sp.TNat,
        sp.address('KT1HbzGokeEZ4hu1KRAAw2fyB61RCpBhQXKA'), # uXTZ/XTZ youves farm
        entry_point="set_max_release_period"
    ).open_some(message='Farm: Invalid entry point set_max_release_period')
    
    savings_pool_entrypoint = sp.contract(
        sp.TNat,
        sp.address('KT1KShHvxW69YukaGetdgYRTw31d9BX8ijfF'), # uXTZ savings pool
        entry_point="update_max_release_period"
    ).open_some(message='Savings pool: Invalid entry point update_max_release_period')

    # 1 second release period (0 is not allowed to avoid divisions by 0)
    new_max_release_period = sp.nat(1)


    ###################################
    # DAO new voting period constants #
    ###################################
    dao_entrypoint = sp.contract(
        GOVERNANCE_PARAMS_TYPE,
        sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'), # youves DAO 
        entry_point="set_governance_params"
    ).open_some(message='DAO: Invalid entry point set_governance_params')

    # new governance params for DAO
    new_governance_params = sp.record(
        escrow_amount = sp.nat(500_000_000_000_000), # 500 YOUs (remains the same)
        vote_delay_blocks = sp.nat(11520), # 2 days (remains unchanged)
        vote_length_blocks = sp.nat(28800), # from 7 days to 5 days
        min_yes_votes_percentage_for_escrow_return = sp.nat(30), # 30% (remains unchanged)
        timelock_execution_delay_blocks = sp.nat(11520), # 2 days (remains unchanged)
        timelock_cancelation_delay_blocks = sp.nat(23040), # 4 days (remains unchanged)
        super_majority_percentage = sp.nat(80), # 80% (remains unchanged)
        quorum_cap = sp.record(
            lower = sp.nat(800_000_000_000_000_000), # 0.8M (remains unchanged)
            upper = sp.nat(3_744_000_000_000_000_000) # 3.744M (remains unchanged)
        ),
    )
    sp.set_type_expr(new_governance_params, GOVERNANCE_PARAMS_TYPE)
    
    
    #######################################################
    # New minting fee receiver for uXTZ engines constants #
    #######################################################
    new_uxtz_xtz_pool = sp.address('KT1FPkNVZESuoLbKxgvhtqb6uyZ3fY5oG5VJ') # Address of the new uXTZ/XTZ constant function market maker.

    # DAO LAMBDA
    sp.result(sp.list([
        sp.transfer_operation(new_max_release_period, sp.mutez(0), farm_entrypoint),
        sp.transfer_operation(new_max_release_period, sp.mutez(0), savings_pool_entrypoint),
        sp.transfer_operation(new_governance_params, sp.mutez(0), dao_entrypoint),

        execute_set_contracts_engine_v3(
            sp.address('KT1AnDFRcdB652Jy5JFtmu7SampSPAzDkK7g'), # uXTZ/USDt collateral engine
            sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'), # youves DAO as interest rate setter (remains the same)
            sp.address('KT1BUR5mjwBWzojKRqWrng8ASBh3N3LLV7NM'), # options contract (remains the same)
            sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'), # stake manager (remains the same)
            new_uxtz_xtz_pool, # mint fee rewards receiver (previously was savings pool)
            sp.address('KT1PvKziQx7pJhfr3FdvkhMPwCwLxjd32HkZ'), # target price oracle (remains the same)
            sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'), # unified staking proxy as rewards receiver (remains the same)
        ),
        execute_set_contracts_engine_v3(
            sp.address('KT1Mf9Nr1KyGC6gUz9pGQnngzWbbZ6thShvc'), # uXTZ/XTZ collateral engine
            sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'), # youves DAO as interest rate setter (remains the same)
            sp.address('KT1CHL9XVrt3Avr1mHkCiZBANEeJzbUSGqGB'), # options contract (remains the same)
            sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'), # stake manager (remains the same)
            new_uxtz_xtz_pool, # mint fee rewards receiver (previously was savings pool)
            sp.address('KT1PuCU5UAoaX2Hjcns2SEmJWBC34tfLjzaS'), # target price oracle (remains the same)
            sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'), # unified staking proxy as rewards receiver (remains the same)
        ),
        execute_set_contracts_engine_v3(
            sp.address('KT1ByNrcyDxYLmamuJbeFJukYkLJaZ1W86Yr'), # uXTZ/SIRS collateral engine
            sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'), # youves DAO as interest rate setter (remains the same)
            sp.address('KT1BUR5mjwBWzojKRqWrng8ASBh3N3LLV7NM'), # options contract (remains the same)
            sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'), # stake manager (remains the same)
            new_uxtz_xtz_pool, # mint fee rewards receiver (previously was savings pool)
            sp.address('KT1TSwSAU1qUyRFYBv6ix5YzqLBparxJ3FAk'), # target price oracle (remains the same)
            sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'), # unified staking proxy as rewards receiver (remains the same)
        ),
    ]))