from utils import addresses as addresses
from yip-01 import yip-01-smartpy as YIP01

if __name__ == "__main__":
    @sp.add_test(name="LambdaBuilder")
    def test():
        scenario = sp.test_scenario()
        lambda_builder = LambdaBuilder()
        scenario += lambda_builder

        lambda_to_send = YIP01.DAO_YIP_01
        execution_payload = MultiSigPayload.make_lambda(
            chain_id=addresses.CHAINID,
            multisig_contract_address=settings.MULTISIG,
            counter=settings.COUNTER,
            _lambda=lambda_to_send,
        )
        lambda_builder.builder(sp.build_lambda(lambda_to_send))
        lambda_builder.multisig_builder(execution_payload)
