import smartpy as sp

def DAO_V2_YIP_8(unit):
    sp.result(
        sp.list([
            # pool
            # set DAO admin in pool
            execute_add_single_administrator(sp.address('KT1SxVFG82J9v1REDuMUiGYWzzyqF5BK2qay'), sp.address('KT1T3BFEu9WSQyRuV9Fyd7SqTU4rW3ptJ3NN')),
            # remove deployer from pool's admins
            execute_remove_admin(
                sp.address("KT1SxVFG82J9v1REDuMUiGYWzzyqF5BK2qay"), sp.address("tz1LZPp4akY2Cphth1WeXsmXDC8bCt9LrrLG")
            ),
            # set reward recipient (pool)
            execute_set_new_reward_recipient(sp.address('KT1SxVFG82J9v1REDuMUiGYWzzyqF5BK2qay'), sp.address('KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB')),
            # token
            # remove deployer
            execute_remove_administrator(
                sp.address("KT1XLoJX3JBi27j4Vd21zRrgPwnnyTnpExHR"),
                sp.address("tz1LZPp4akY2Cphth1WeXsmXDC8bCt9LrrLG"),
                sp.nat(0),
            ),
            # cpmm
            # set DAO as admin
            execute_propose_administrator(sp.address('KT1B32BXtgHzNevXDeXbXcA63SDCxfPRAiWb'), sp.address('KT1T3BFEu9WSQyRuV9Fyd7SqTU4rW3ptJ3NN')),
            execute_add_single_administrator(sp.address('KT1B32BXtgHzNevXDeXbXcA63SDCxfPRAiWb'), sp.address('KT1T3BFEu9WSQyRuV9Fyd7SqTU4rW3ptJ3NN')),
            # set reward recipient (cpmm)
            execute_set_new_reward_recipient(sp.address('KT1B32BXtgHzNevXDeXbXcA63SDCxfPRAiWb'), sp.address('KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB')),
            # gas station
            # set DAO as admin
            execute_add_single_administrator(sp.address('KT1FThqponAJi56EAiotSS64egW2eThGxDA6'), sp.address('KT1T3BFEu9WSQyRuV9Fyd7SqTU4rW3ptJ3NN')),
            # remove deployer from gas station's admins
            execute_remove_admin(
                sp.address("KT1FThqponAJi56EAiotSS64egW2eThGxDA6"), sp.address("tz1LZPp4akY2Cphth1WeXsmXDC8bCt9LrrLG")
            ),
            # script updater
            # set DAO as admin
            execute_add_single_administrator(sp.address('KT198mB5VXfeftAXbo3dqkEMjR3oWShEoazY'), sp.address('KT1T3BFEu9WSQyRuV9Fyd7SqTU4rW3ptJ3NN')),
            # remove deployer from gas station's admins
            execute_remove_admin(
                sp.address("KT198mB5VXfeftAXbo3dqkEMjR3oWShEoazY"), sp.address("tz1LZPp4akY2Cphth1WeXsmXDC8bCt9LrrLG")
            ),
        ])
    )