import smartpy as sp

def execute_set_token_metadata(token_address, token_id, token_info):
    token_contract = sp.contract(
        sp.TPair(sp.TNat, sp.TMap(sp.TString, sp.TBytes)),
        token_address,
        entry_point="set_token_metadata",
    ).open_some()
    payload = sp.pair(token_id, token_info)
    return sp.transfer_operation(payload, sp.mutez(0), token_contract)

def set_uxau_token_metadata(unit):
    sp.set_type(unit, sp.TUnit)
    sp.result(
        sp.list([
            execute_set_token_metadata(
                sp.address("KT1XRPEPXbZK25r3Htzp2o1x7xdMMmfocKNW"),
                sp.nat(4),
                sp.map(
                    l={ "" : sp.bytes("0x697066733a2f2f516d553972507434354b51466d35315a46467a65727a6231586645726f7a6d31734d4678443478705851394e526e")},
                    tkey=sp.TString,
                    tvalue = sp.TBytes
                )
            )
        ])
    )

def execute_execute(administrable_address, executable_lambda):
    administrable_contract = sp.contract(
        sp.TLambda(sp.TUnit, sp.TList(sp.TOperation)),
        administrable_address,
        entry_point="execute",
    ).open_some()
    return sp.transfer_operation(
        sp.build_lambda(executable_lambda), sp.mutez(0), administrable_contract
    )

def execute_add_administrator(administrable_address, new_admin, token_id):
    administrable_contract = sp.contract(
        sp.TPair(sp.TAddress, sp.TNat),
        administrable_address,
        entry_point="set_administrator",
    ).open_some()
    payload = sp.pair(new_admin, token_id)
    return sp.transfer_operation(payload, sp.mutez(0), administrable_contract)

def add_administrator_to_contract(unit, administrable_address, admin_to_add, token_id):
    sp.set_type(unit, sp.TUnit)
    sp.result(
        sp.list(
            [execute_add_administrator(administrable_address, admin_to_add, token_id)]
        )
    )

def execute_set_stake_factor(administrable_address, address, factor):
    administrable_contract = sp.contract(
        sp.TPair(sp.TAddress, sp.TNat),
        administrable_address,
        entry_point="set_stake_factor",
    ).open_some()
    payload = sp.pair(address, factor)
    return sp.transfer_operation(payload, sp.mutez(0), administrable_contract)

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

def DAO_YIP_02(unit):
    sp.set_type(unit, sp.TUnit)

    #############################
    # DAO new governance params #
    #############################
    dao_entrypoint = sp.contract(
        GOVERNANCE_PARAMS_TYPE,
        sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'), # youves DAO 
        entry_point="set_governance_params"
    ).open_some(message='DAO: Invalid entry point set_governance_params')

    # new governance params for DAO
    new_governance_params = sp.record(
        escrow_amount = sp.nat(1_000_000_000_000_000), # 1000 YOUs
        vote_delay_blocks = sp.nat(1440), # 6 hours
        vote_length_blocks = sp.nat(28800), # 5 days (remains the same)
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
    
    # DAO LAMBDA
    sp.result(sp.list([
        execute_execute(sp.address("KT1FFE2LC5JpVakVjHm5mM36QVp2p3ZzH4hH"), set_uxau_token_metadata), # add uXAU token to the synthetic contract
        execute_execute(
            sp.address("KT1FFE2LC5JpVakVjHm5mM36QVp2p3ZzH4hH"),
            lambda unit: add_administrator_to_contract(
                unit,
                sp.address("KT1XRPEPXbZK25r3Htzp2o1x7xdMMmfocKNW"),
                sp.address('KT1VhU47n633rqJeAZESfbejnxeJmpXVx3AA'),
                sp.nat(4)
            )
        ), # add the uXAU engine as admin to the uXAU token
        execute_add_administrator(sp.address("KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4"), sp.address('KT1VhU47n633rqJeAZESfbejnxeJmpXVx3AA'), 0), # add the uXAU engine as admin to the stake manager
        # for the price 1oz gold = 1931.16 usd and 1 tez = 0.791470 usd the stake factor is 2439.96613896 * 10^18.
        execute_set_stake_factor(sp.address("KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4"), sp.address('KT1VhU47n633rqJeAZESfbejnxeJmpXVx3AA'), 2_439_966_138_960_000_000_000), # set the stake factor of the uXAU token.
        
        sp.transfer_operation(new_governance_params, sp.mutez(0), dao_entrypoint),

        execute_set_contracts_engine_v3(
            sp.address('KT1Mf9Nr1KyGC6gUz9pGQnngzWbbZ6thShvc'), # uXTZ/XTZ collateral engine
            sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'), # youves DAO as interest rate setter (remains the same)
            sp.address('KT1GL6CBm93edDHogUVQzasUd6m7384eZk3J'), # options contract
            sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'), # stake manager (remains the same)
            sp.address('KT1BFXgczFte2zftCTg7tL6Qk2capsFg6UFS'), # savings_pool (remains the same)
            sp.address('KT1PuCU5UAoaX2Hjcns2SEmJWBC34tfLjzaS'), # target price oracle (remains the same)
            sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'), # unified staking proxy as rewards receiver (remains the same)
        ),
        execute_set_contracts_engine_v3(
            sp.address('KT1ByNrcyDxYLmamuJbeFJukYkLJaZ1W86Yr'), # uXTZ/SIRS collateral engine
            sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'), # youves DAO as interest rate setter (remains the same)
            sp.address('KT1CHL9XVrt3Avr1mHkCiZBANEeJzbUSGqGB'), # options contract
            sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'), # stake manager (remains the same)
            sp.address('KT1BFXgczFte2zftCTg7tL6Qk2capsFg6UFS'), # savings_pool (remains the same)
            sp.address('KT1TSwSAU1qUyRFYBv6ix5YzqLBparxJ3FAk'), # target price oracle (remains the same)
            sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'), # unified staking proxy as rewards receiver (remains the same)
        ),
    ]))