import smartpy as sp

def DAO_V2_YIP_10(unit):
    sp.result(
        sp.list(
            [
            # pool
            # set DAO admin in pool
            execute_set_administrator_unit(
                sp.address("KT1FRN2RmitUkyyovtjRMrU1G9zwKzgESXm8"),
            ),
            # pool
            # set reward recipient (pool)
            execute_set_new_reward_recipient(
                sp.address("KT1FRN2RmitUkyyovtjRMrU1G9zwKzgESXm8"),
                sp.address("KT1FPmpucXoiX7ZLahj1V1E5tRah1XvcnkZB"),
            ),
            # pool
            # remove deployer from pool's admins
            execute_remove_admin(
                sp.address("KT1FRN2RmitUkyyovtjRMrU1G9zwKzgESXm8"),
                sp.address("tz1LZPp4akY2Cphth1WeXsmXDC8bCt9LrrLG"),
            ),
            # token
            # remove deployer
            execute_remove_administrator(
                sp.address("KT1KXKhkxDezoa8G3WvPtsrgNTs5ZQwhpYZN"),
                sp.address("tz1LZPp4akY2Cphth1WeXsmXDC8bCt9LrrLG"),
                sp.nat(0),
            ),
            # gas station
            # set DAO as admin
            execute_set_administrator_unit(
                sp.address("KT1FThqponAJi56EAiotSS64egW2eThGxDA6"),
            ),
            # gas station
            # remove deployer from gas station's admins
            execute_remove_admin(
                sp.address("KT1FThqponAJi56EAiotSS64egW2eThGxDA6"),
                sp.address("tz1LZPp4akY2Cphth1WeXsmXDC8bCt9LrrLG"),
            ),
            # script updater
            # set DAO as admin
            execute_set_administrator_unit(
                sp.address("KT198mB5VXfeftAXbo3dqkEMjR3oWShEoazY"),
            ),
            # script updater
            # remove deployer from script updater's admins
            execute_remove_admin(
                sp.address("KT198mB5VXfeftAXbo3dqkEMjR3oWShEoazY"),
                sp.address("tz1LZPp4akY2Cphth1WeXsmXDC8bCt9LrrLG"),
            ),
        ]
        )
    )