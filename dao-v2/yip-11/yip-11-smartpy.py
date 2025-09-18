import smartpy as sp

def execute_set_script_stacy(administrable_address, script, script_hash):
    administrable_contract = sp.contract(
        sp.TPair(sp.TString, sp.TString), administrable_address, entry_point="set_script"
    ).open_some()
    return sp.transfer_operation(sp.pair(script, script_hash), sp.mutez(0), administrable_contract)

def DAO_V2_YIP_11(unit):
    sp.result(
        sp.list(
            [
                execute_set_script_stacy(
                    sp.address("KT198mB5VXfeftAXbo3dqkEMjR3oWShEoazY"),
                    "ipfs://QmR6toZqSUnqDxkRiNp2oeBUmHJRQD44PtmmCrcaeB15pX",
                    "1ba832f211d43c1b49dc61cf734ab89f1d08a1f101914b9302de9152f255457f"
                )
            ]
        )
    )

class LambdaBuilder(sp.Contract):
    def __init__(self, **kargs):
        self.init(**kargs)
    
    @sp.entry_point
    def builder(self, execution_payload):
        sp.set_type(execution_payload, sp.TLambda(sp.TUnit, sp.TList(sp.TOperation)))
        sp.local("execution", execution_payload)
        
if __name__ == "__main__":
    @sp.add_test(name="LambdaBuilder")
    def test():
        scenario = sp.test_scenario()
        lambda_builder = LambdaBuilder()
        scenario += lambda_builder
        lambda_builder.builder(sp.build_lambda(DAO_V2_YIP_11))