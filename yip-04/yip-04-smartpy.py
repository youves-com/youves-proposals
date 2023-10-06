import smartpy as sp

def execute_set_contracts_engine_v2(
    engine_address,
    target_price_oracle,
    reward_pool_contract,
    savings_pool_contract,
    governance_token_contract,
    options_contract,
):

    engine_contract = sp.contract(
        sp.TPair(
            sp.TPair(sp.TAddress, sp.TAddress),
            sp.TPair(sp.TAddress, sp.TPair(sp.TAddress, sp.TAddress)),
        ),
        engine_address,
        entry_point="set_contracts",
    ).open_some()

    payload = sp.pair(
        sp.pair(governance_token_contract, options_contract),
        sp.pair(
            reward_pool_contract, sp.pair(savings_pool_contract, target_price_oracle)
        ),
    )

    return sp.transfer_operation(payload, sp.mutez(0), engine_contract)

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

def DAO_YIP_4(unit):
    sp.set_type(unit, sp.TUnit)
    
    savings_pool_entrypoint = sp.contract(
        sp.TNat,
        sp.address('KT1WT8hZsixALTmxcM3SDzCyh4UF8hYXVaUb'), # uBTC savings pool
        entry_point="update_max_release_period"
    ).open_some(message='Invalid ep: update_max_release_period')

    UBTC_TZBTC_FLAT_CURVE = sp.address('KT1HUrBzmWHAx5RTUGbhymd1YgycBMKEoHBF')
    #############################
    # DAO new governance params #
    #############################
    sp.result(sp.list([
        sp.transfer_operation(sp.nat(1), sp.mutez(0), savings_pool_entrypoint), # update savings pool release time.
        execute_set_contracts_engine_v2(
            engine_address=sp.address('KT1VjQoL5QvyZtm9m1voQKNTNcQLi5QiGsRZ'), # uBTC-XTZ engine V2
            target_price_oracle=sp.address('KT1CdMTeztkZJhVUYRDBBW7gaGQQq87jtjzk'),
            reward_pool_contract=sp.address('KT1UZcNDxTdkn33Xx5HRkqQoZedc3mEs11yV'),
            savings_pool_contract=UBTC_TZBTC_FLAT_CURVE,
            governance_token_contract=sp.address('KT1UkLkTtkePPfGjfd97Pj8eo7ogp3RCpuFk'),
            options_contract=sp.address('KT1WZY3DEBy6yTeXBe5BmMxMSV7RhDKDeS81'),
        ),
        execute_set_contracts_engine_v2(
            engine_address=sp.address('KT1NFWUqr9xNvVsz2LXCPef1eRcexJz5Q2MH'), # uBTC - SIRS engine V2
            target_price_oracle=sp.address('KT1GqQqgLji2T5QMfzoAXgDt9T7ur1LhqfpD'),
            reward_pool_contract=sp.address('KT1UZcNDxTdkn33Xx5HRkqQoZedc3mEs11yV'),
            savings_pool_contract=UBTC_TZBTC_FLAT_CURVE,
            governance_token_contract=sp.address('KT1UkLkTtkePPfGjfd97Pj8eo7ogp3RCpuFk'),
            options_contract=sp.address('KT1CHzk4vojAF1gakAjB1mXa2nVrtyoe57v6'),
        ),
        execute_set_contracts_engine_v3(
            engine_address=sp.address('KT1CP1C8afHqdNfBsSE3ggQhzM2iMHd4cRyt'), # uBTC - TEZ engine v3
            interest_rate_setter_contract=sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'),
            options_contract=sp.address('KT1H4h1VunWkVE9Cuq1QDVy9xRNLBSbqXsr9'),
            governance_token_contract=sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'),
            savings_pool_contract=UBTC_TZBTC_FLAT_CURVE,
            target_price_oracle=sp.address('KT1QDWxfzptWPooyqmf1pjsjGkGcfu8dM32z'),
            reward_pool_contract=sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'),
        ),
        execute_set_contracts_engine_v3(
            engine_address=sp.address('KT1G6RzVX25YnoU55Xb7Vve3zvuZKmouf24a'), # uBTC - SIRS engine v3
            interest_rate_setter_contract=sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'),
            options_contract=sp.address('KT1J217QyWoPSE8EtAySMyJjr8ptTsakBszP'),
            governance_token_contract=sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'),
            savings_pool_contract=UBTC_TZBTC_FLAT_CURVE,
            target_price_oracle=sp.address('KT1KpFkAKgrAJNXZxhahFaTduTAoEc8jFpmQ'),
            reward_pool_contract=sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'),
        ),
        execute_set_contracts_engine_v3(
            engine_address=sp.address('KT1XH5rKSd6Ae3DAMYi26gEZP1gxAoQRYRfS'), # uBTC - tzBTC engine v3
            interest_rate_setter_contract=sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'),
            options_contract=sp.address('KT1DnPwdvntBac7xFmdLqNakKcLHVjYfW1WU'),
            governance_token_contract=sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'),
            savings_pool_contract=UBTC_TZBTC_FLAT_CURVE,
            target_price_oracle=sp.address('KT19cZHwuaPvNY85Un5dtmKzGGaMgbvadSBg'),
            reward_pool_contract=sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'),
        ),
        execute_set_contracts_engine_v3(
            engine_address=sp.address('KT1SEjPmaeVPMu4Ep94ggF3tLqzFM83T3pBd'), # uBTC - SIRS engine v3 0% minting fee
            interest_rate_setter_contract=sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'),
            options_contract=sp.address('KT1NC8PcGG6QR6V2AezQTwd8xjgorDzkCzYy'),
            governance_token_contract=sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'),
            savings_pool_contract=UBTC_TZBTC_FLAT_CURVE,
            target_price_oracle=sp.address('KT1KpFkAKgrAJNXZxhahFaTduTAoEc8jFpmQ'),
            reward_pool_contract=sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'),
        ),
        execute_set_contracts_engine_v3(
            engine_address=sp.address('KT18x66448Gt3kYYkfvx4Cg2dP9cRPfjQwVv'), # uBTC - tzBTC engine v3 0% minting fee
            interest_rate_setter_contract=sp.address('KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab'),
            options_contract=sp.address('KT1Jf2UHSo6PbBfKYZiCzDq5UpeTKDQPeCJb'),
            governance_token_contract=sp.address('KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4'),
            savings_pool_contract=UBTC_TZBTC_FLAT_CURVE,
            target_price_oracle=sp.address('KT19cZHwuaPvNY85Un5dtmKzGGaMgbvadSBg'),
            reward_pool_contract=sp.address('KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo'),
        ),
    ]))
