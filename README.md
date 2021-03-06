# minimalcryptocurrency

[![Travis CI build status](https://travis-ci.org/drodriguezperez/minimalcryptocurrency.svg?branch=master)](https://travis-ci.org/drodriguezperez/minimalcryptocurrency)
[![Requirements Status](https://requires.io/github/drodriguezperez/minimalcryptocurrency/requirements.svg?branch=develop)](https://requires.io/github/drodriguezperez/minimalcryptocurrency/requirements/?branch=develop)
[![Codecov Code Coverage](https://codecov.io/gh/drodriguezperez/minimalcryptocurrency/branch/master/graph/badge.svg)](https://codecov.io/gh/drodriguezperez/minimalcryptocurrency)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/drodriguezperez/minimalcryptocurrency/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/drodriguezperez/minimalcryptocurrency/?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/23fe4d509e9e4e68a14723ae808f8e10)](https://www.codacy.com/app/drodriguezperez/minimalcryptocurrency?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=drodriguezperez/minimalcryptocurrency&amp;utm_campaign=Badge_Grade)

This package implements a basic Blockchain and a Cryptocurrency.

## Description
In this package, a basic version of a Blockchain and a Cryptocurrency is
implemented in this Python language. The main purpose of this code is to offer
a simple implementation to understand the way in which works these two
technologies.

## Installation
You can install the last version form the git repository using `pip`

    pip install git+https://github.com/Aixa98/CryptoMaster.git

## Usage
Before creating a Blockchain it is necessary to create an account to which the
initial amount will be assigned. An account is a pair of private and public
keys that can be created using the `Wallet` constructor.

    wallet = Wallet()

The wallet obketc have to properties: `key`, the private key that is secreat,
and `account`, the public key which identifies the user account. Now it is
possible to initialize the blockchain using the BlockChain constructor:

    blockchain = BlockChain.new_cryptocurrency(wallet.account, 10,
                 timestamp=datetime(2018, 1, 1, 0, 0, 0), difficulty=4,
                 mining=True)

After that two users can be created: Alice and Bob. Alice???s account is the one
in which the initial amount has been assigned and Bob is a new one. It is
possible to check the initial balance in both accounts.

    alice = blockchain.get_wallet(wallet.key)
    bob = blockchain.get_wallet()
    
    assert alice.get_balance() == 10
    assert bob.get_balance() == 0

Users with currencies in their wallet can order transfers to another user
wallets. These transfers are saved in a block and the user that the mines
obtain a reward.

    assert blockchain.add_transaction(alice.key, bob.account, 5)

    blockchain.generate_candidate(alice.account, timestamp=datetime(2018, 1, 1, 0, 1, 0))
    blockchain.mining_candidate()

    assert alice.get_balance() == 15
    assert bob.get_balance() == 5

More users can access the and exchange coins.

    # New users
    carol = blockchain.get_wallet()
    dan = blockchain.get_wallet()
    eve = blockchain.get_wallet()

    # Alice transfer 3 to Carol and 4.5 to Dan
    blockchain.add_transaction(alice.key, carol.account, 3)
    blockchain.add_transaction(alice.key, dan.account, 4.5)

    # Bon transfer 2.2 to Dan
    blockchain.add_transaction(bob.key, dan.account, 2.2)

    # Eve mine the Block
    blockchain.generate_candidate(eve.account, timestamp=datetime(2018, 1, 1, 0, 2, 0))
    blockchain.mining_candidate()

    # The situation of each wallet is
    assert alice.get_balance() == 7.5
    assert bob.get_balance() == 2.8
    assert carol.get_balance() == 3
    assert dan.get_balance() == 6.7
    assert eve.get_balance() == 10

## References
The package implements the contents of the blog (only in Spanish
[Analytics Lane](https://www.analyticslane.com/2018/06/18/implementacion-criptomoneda/)

## Disclaimer
Copyright (C) 2021 Aixa Benitez

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.