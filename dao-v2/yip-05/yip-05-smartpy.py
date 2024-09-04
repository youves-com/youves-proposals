import smartpy as sp
import utils.addresses as addresses

def execute_set_administrator_unit(administrable_address):
    administrable_contract = sp.contract(
        sp.TUnit, administrable_address, entry_point="set_administrator"
    ).open_some()
    return sp.transfer_operation(sp.unit, sp.mutez(0), administrable_contract)

def execute_update_max_release_period(contract_address, new_max_release_period):
    contract_ep = sp.contract(
        sp.TNat, contract_address, entry_point="update_max_release_period"
    ).open_some()

    return sp.transfer_operation(new_max_release_period, sp.mutez(0), contract_ep)

def execute_set_reference_interest_rate(engine, new_interest_rate):
    engine_contract = sp.contract(
        sp.TNat, engine, entry_point="set_reference_interest_rate"
    ).open_some()

    return sp.transfer_operation(new_interest_rate, sp.mutez(0), engine_contract)

def yip5(unit):
    sp.set_type(unit, sp.TUnit)

    sp.result(sp.list([
        # Pools and farms admin
        execute_set_administrator_unit(addresses.UUSD_SAVINGS_POOL),
        execute_set_administrator_unit(addresses.UBTC_SAVINGS_POOL),
        execute_update_max_release_period(addresses.UBTC_SAVINGS_POOL, sp.nat(1)),
        execute_set_reference_interest_rate(addresses.UBTC_TEZ_ENGINE, 196),
        execute_set_reference_interest_rate(addresses.UBTC_SIRS_ENGINE, 196),
        execute_set_reference_interest_rate(addresses.UBTC_TZBTC_ENGINE, 196),
        execute_set_reference_interest_rate(addresses.UBTC_SIRS_ZERO_MINTING_FEE_ENGINE, 196),
        execute_set_reference_interest_rate(addresses.UBTC_TZBTC_ZERO_MINTING_FEE_ENGINE, 196),
    ]))