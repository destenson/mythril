import unittest
from mythril.disassembler.callgraph import generate_callgraph
from mythril.disassembler.disassembly import Disassembly


class SVMTestCase(unittest.TestCase):

    def runTest(self):

        modules = {}
        modules['0x0000000000000000000000000000000000000000'] = {'name': 'metaCoin', 'address': '0x0000000000000000000000000000000000000000', 'creation_code': '', 'code': '60606040526004361061004c576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806327e235e314610051578063412664ae1461009e575b600080fd5b341561005c57600080fd5b610088600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506100f8565b6040518082815260200191505060405180910390f35b34156100a957600080fd5b6100de600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610110565b604051808215151515815260200191505060405180910390f35b60006020528060005260406000206000915090505481565b6000816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054101561016157600090506101fe565b816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540392505081905550816000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550600090505b929150505600a165627a7a72305820fd4fa106da498514e90965a45ffecc1da53a0cd8bb7a7135910f8612245a46370029'}
        modules['0x0000000000000000000000000000000000000000']['disassembly'] = Disassembly(modules['0x0000000000000000000000000000000000000000']['code'])

        html = generate_callgraph(modules, False)

        self.assertTrue("var nodes = [\n{id: 0, size: 150" in html)
