import smartpy as sp

def yip7(unit):
    sp.set_type(unit, sp.TUnit)

    #############################
    # DAO new governance params #
    #############################
    dao_entrypoint = sp.contract(
        GOVERNANCE_PARAMS_TYPE,
        sp.address('KT1T3BFEu9WSQyRuV9Fyd7SqTU4rW3ptJ3NN'), # youves DAO V2
        entry_point="set_governance_params"
    ).open_some(message='DAO: Invalid entry point set_governance_params')

    # new governance params for DAO
    new_governance_params = sp.record(
        escrow_amount = sp.nat(1_000_000_000_000_000), # 1000 YOUs
        vote_delay_blocks = sp.nat(2700), # 6 hours
        vote_length_blocks = sp.nat(43200), # 4 days
        min_yes_votes_percentage_for_escrow_return = sp.nat(30), # 30% (remains unchanged)
        timelock_execution_delay_blocks = sp.nat(14400), # 2 days (remains unchanged)
        timelock_cancelation_delay_blocks = sp.nat(37800), # 3,5 days 
        super_majority_percentage = sp.nat(80), # 80% (remains unchanged)
        quorum_cap = sp.record(
            lower = sp.nat(800_000_000_000_000_000), # 0.8M (remains unchanged)
            upper = sp.nat(3_744_000_000_000_000_000) # 3.744M (remains unchanged)
        ),
    )
    sp.set_type_expr(new_governance_params, GOVERNANCE_PARAMS_TYPE)
    
    # DAO LAMBDA
    sp.result(sp.list([
        sp.transfer_operation(new_governance_params, sp.mutez(0), dao_entrypoint)
    ]))
