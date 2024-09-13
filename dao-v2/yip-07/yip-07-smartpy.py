import smartpy as sp
import utils.addresses as addresses

def set_target_swap_oracle(swap, oracle):
    swap_ep = sp.contract(
        sp.TAddress,
        swap,
        entry_point="setTargetOracle"
    ).open_some(message="Invalid entrypoint: setTargetOracle")
    return sp.transfer_operation(oracle, sp.mutez(0), swap_ep)

def DAO_YIP_7(unit):
    sp.set_type(unit, sp.TUnit)
    sp.result(sp.list([
        set_target_swap_oracle(
            addresses.UUSD_UBTC_EXCHANGE,
            sp.address("KT1Cy1wwHbW1NMawnQCrfXMBtuwXSsidEDg2")
        )
    ]))
