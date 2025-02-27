# This is the layout as of deploying the new addressprovider.
# The key is _id, the value is _description
ADDRESS_PROVIDER_MAPPING = {
    0: "Stableswap Custom Pool Registry",
    1: "PoolInfo Getters",
    2: "Exchange Router",
    3: "Stableswap Metapool Factory",
    4: "Fee Distributor",
    5: "Cryptoswap Custom Pool Registry",
    6: "Twocrypto Factory",
    7: "Metaregistry",
    8: "Stableswap crvUSD Factory",
    9: "",
    10: "",
    11: "TricryptoNG Factory",
    12: "StableswapNG Factory",
    13: "TwocryptoNG Factory",
    14: "Stableswap Calculations Contract",
    15: "Cryptoswap calculations Contract",
    16: "LLAMMA Factory crvUSD",
    17: "LLAMMA Factory OneWayLending",
    18: "Spot Rate Provider",
    19: "CRV Token",
    20: "Gauge Factory",
    21: "Ownership Admin",
    22: "Parameter Admin",
    23: "Emergency Admin",
    24: "CurveDAO Vault",  # Holds funds
}

# These are the addresses that will go into the addressprovider for each chain:

addresses = {
    "ethereum": {
        0: "0x90E00ACe148ca3b23Ac1bC8C240C2a7Dd9c2d7f5",
        1: "0xe64608E223433E8a03a1DaaeFD8Cb638C14B552C",
        2: "0xF0d4c12A5768D806021F80a262B4d39d26C58b8D",
        3: "0xB9fC157394Af804a3578134A6585C0dc9cc990d4",
        4: "0xA464e6DCda8AC41e03616F95f4BC98a13b8922Dc",
        5: "0x8F942C20D02bEfc377D41445793068908E2250D0",
        6: "0xF18056Bbd320E96A48e3Fbf8bC061322531aac99",
        7: "0xF98B45FA17DE75FB1aD0e7aFD971b0ca00e379fC",
        8: "0x4F8846Ae9380B90d2E71D5e3D042dff3E7ebb40d",
        11: "0x0c0e5f2fF0ff18a3be9b835635039256dC4B4963",  # Tricrypto NG
        12: "0x6A8cbed756804B16E05E741eDaBd5cB544AE21bf",  # Stableswap NG
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",  # Twocrypto NG
        14: "0xCA8d0747B5573D69653C3aC22242e6341C36e4b4",
        15: "0xA72C85C258A81761433B4e8da60505Fe3Dd551CC",
        16: "0xc9332fdcb1c491dcc683bae86fe3cb70360738bc",  # call controllerFactory.amm(id)
        17: "0xeA6876DDE9e3467564acBeE1Ed5bac88783205E0",  # same as (16)
        19: "0xD533a949740bb3306d119CC777fa900bA034cd52",
        21: "0x40907540d8a6C65c637785e8f8B742ae6b0b9968",  # CurveDAO Ownership Agent
        22: "0x4eeb3ba4f221ca16ed4a0cc7254e2e32df948c5f",  # CurveDAO Parameter Agent
        23: "0x00669DF67E4827FCc0E48A1838a8d5AB79281909",  # CurveDAO Emergency Agent
    },
    "arbitrum": {
        0: "0x445FE580eF8d70FF569aB36e80c647af338db351",
        1: "0x78CF256256C8089d68Cde634Cf7cDEFb39286470",
        2: "0xF0d4c12A5768D806021F80a262B4d39d26C58b8D",
        3: "0xb17b674D9c5CB2e441F8e196a2f048A81355d031",
        4: "0xd4F94D0aaa640BBb72b5EEc2D85F6D114D81a88E",
        5: "0x0E9fBb167DF83EdE3240D6a5fa5d40c6C6851e15",
        11: "0xbC0797015fcFc47d9C1856639CaE50D0e69FbEE8",
        12: "0x9AF14D26075f142eb3F292D5065EB3faa646167b",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        14: "0xCA8d0747B5573D69653C3aC22242e6341C36e4b4",
        15: "0xA72C85C258A81761433B4e8da60505Fe3Dd551CC",
        17: "0xcaEC110C784c9DF37240a8Ce096D352A75922DeA",
        19: "0x11cDb42B0EB46D95f990BeDD4695A6e3fA034978",
        20: "0xabC000d88f23Bb45525E447528DBF656A9D55bf5",
        21: "0x452030a5D962d37D97A9D65487663cD5fd9C2B32",
        22: "0x5ccbB27FB594c5cF6aC0670bbcb360c0072F6839",
        23: "0x2CB6E1Adf22Af1A38d7C3370441743a123991EC3",
        24: "0x25877b9413Cc7832A6d142891b50bd53935feF82",
    },
    "optimism": {
        0: "0xC5cfaDA84E902aD92DD40194f0883ad49639b023",
        1: "0x54e8A25d0Ac0E4945b697C80b8372445FEA17A62",
        2: "0xF0d4c12A5768D806021F80a262B4d39d26C58b8D",
        3: "0x2db0E83599a91b508Ac268a6197b8B14F5e72840",
        4: "0xbF7E49483881C76487b0989CD7d9A8239B20CA41",
        5: "0x7DA64233Fefb352f8F501B357c018158ED8aA455",
        11: "0xc6C09471Ee39C7E30a067952FcC89c8922f9Ab53",
        12: "0x5eeE3091f747E60a045a2E715a4c71e600e31F6E",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        14: "0xCA8d0747B5573D69653C3aC22242e6341C36e4b4",
        15: "0xA72C85C258A81761433B4e8da60505Fe3Dd551CC",
        19: "0x0994206dfE8De6Ec6920FF4D779B0d950605Fb53",
        20: "0xabC000d88f23Bb45525E447528DBF656A9D55bf5",
        21: "0x28c4A1Fa47EEE9226F8dE7D6AF0a41C62Ca98267",
        22: "0xE7F2B72E94d1c2497150c24EA8D65aFFf1027b9b",
        23: "0x9fF1ddE4BE9BbD891836863d227248047B3D881b",
        24: "0xD166EEdf272B860E991d331B71041799379185D5",
    },
    "polygon": {
        0: "0x094d12e5b541784701FD8d65F11fc0598FBC6332",
        1: "0x7544Fe3d184b6B55D6B36c3FCA1157eE0Ba30287",
        2: "0xF0d4c12A5768D806021F80a262B4d39d26C58b8D",
        3: "0x722272D36ef0Da72FF51c5A65Db7b870E2e8D4ee",
        4: "0x774D1Dba98cfBD1F2Bc3A1F59c494125e07C48F9",
        5: "0x47bB542B9dE58b970bA50c9dae444DDB4c16751a",
        6: "0xE5De15A9C9bBedb4F5EC13B131E61245f2983A69",
        11: "0xC1b393EfEF38140662b91441C6710Aa704973228",  # Tricrypto NG
        12: "0x1764ee18e8B3ccA4787249Ceb249356192594585",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        14: "0xCA8d0747B5573D69653C3aC22242e6341C36e4b4",
        15: "0xA72C85C258A81761433B4e8da60505Fe3Dd551CC",
        19: "0x172370d5cd63279efa6d502dab29171933a610af",
        20: "0xabC000d88f23Bb45525E447528DBF656A9D55bf5",
        21: "0x8cB05bFEd65b522a7cF98d590F1711A9Db43af71",
        22: "0x3CF7c393519ea55D1E1F2c55a6395be63b1A9F9C",
        23: "0x9FD6E204e08867170ddE54a8374083fF592eBD3E",
    },
    "base": {
        2: "0xd6681e74eEA20d196c15038C580f721EF2aB6320",
        3: "0x3093f9B57A428F3EB6285a589cb35bEA6e78c336",
        4: "0xe8269B33E47761f552E1a3070119560d5fa8bBD6",
        6: "0x5EF72230578b3e399E6C6F4F6360edF95e83BBfd",
        11: "0xA5961898870943c68037F6848d2D866Ed2016bcB",
        12: "0xd2002373543Ce3527023C75e7518C274A51ce712",
        13: "0xc9Fe0C63Af9A39402e8a5514f9c43Af0322b665F",
        14: "0x5552b631e2aD801fAa129Aacf4B701071cC9D1f7",
        15: "0xEfadDdE5B43917CcC738AdE6962295A0B343f7CE",
        19: "0x8Ee73c484A26e0A5df2Ee2a4960B789967dd0415",
        20: "0xabC000d88f23Bb45525E447528DBF656A9D55bf5",
        21: "0x2c163fe0f079d138b9c04f780d735289344C8B80",
        22: "0x7Ea4B72f04D8B02994F4EdB171Ce5F56eEdF457F",
        23: "0x95F0f720CAdDED982E6998b3390E6D3788c2CE5C",
        24: "0xA4c0eA0fb8eb652e11C8123E589197E18Ca78AA8",
    },
    "fraxtal": {
        2: "0x4f37A9d177470499A2dD084621020b023fcffc1F",
        4: "0x8b3EFBEfa6eD222077455d6f0DCdA3bF4f3F57A6",
        11: "0xc9Fe0C63Af9A39402e8a5514f9c43Af0322b665F",
        12: "0xd2002373543Ce3527023C75e7518C274A51ce712",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        14: "0xCA8d0747B5573D69653C3aC22242e6341C36e4b4",
        15: "0x69522fb5337663d3B4dFB0030b881c1A750Adb4f",
        19: "0x331B9182088e2A7d6D3Fe4742AbA1fB231aEcc56",
        20: "0xeF672bD94913CB6f1d2812a6e18c1fFdEd8eFf5c",
    },
    "bsc": {
        2: "0x69522fb5337663d3B4dFB0030b881c1A750Adb4f",
        3: "0xEfDE221f306152971D8e9f181bFe998447975810",
        4: "0x98B4029CaBEf7Fd525A36B0BF8555EC1d42ec0B6",
        6: "0xBd5fBd2FA58cB15228a9Abdac9ec994f79E3483C",
        11: "0x38f8D93406fA2d9924DcFcB67dB5B0521Fb20F7D",
        12: "0xd7E72f3615aa65b92A4DBdC211E296a35512988B",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        14: "0x0fE38dCC905eC14F6099a83Ac5C93BF2601300CF",
        15: "0xd6681e74eEA20d196c15038C580f721EF2aB6320",
        19: "0x8Ee73c484A26e0A5df2Ee2a4960B789967dd0415",
        20: "0xDb205f215f568ADf21b9573b62566f6d9a40bed6",
        21: "0xC97E2328c5701572C0DFB199b9f860d6ccD74199",
        22: "0x618a38a556B66FdDdcB5495Be412Df911D18eA1d",
        23: "0xC940CE179f1F1bdC1EA1c02A2d0481bfD84C3280",
        24: "0x44C927BacD65da570cB1F0A2F625367049525022",
    },
    "gnosis": {
        0: "0x55e91365697eb8032f98290601847296ec847210",
        1: "0xf1755aadb82dc7a45ab4e754f67412dc75576dc7",
        2: "0xF0d4c12A5768D806021F80a262B4d39d26C58b8D",
        3: "0xd19baeadc667cf2015e395f2b08668ef120f41f5",
        4: "0xB055EbbAcc8Eefc166c169e9Ce2886D0406aB49b",
        5: "0x8a4694401be8f8fccbc542a3219af1591f87ce17",
        11: "0xb47988ad49dce8d909c6f9cf7b26caf04e1445c8",
        12: "0xbC0797015fcFc47d9C1856639CaE50D0e69FbEE8",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        14: "0xCA8d0747B5573D69653C3aC22242e6341C36e4b4",
        15: "0xA72C85C258A81761433B4e8da60505Fe3Dd551CC",
        19: "0x712b3d230f3c1c19db860d80619288b1f0bdd0bd",
        20: "0xabC000d88f23Bb45525E447528DBF656A9D55bf5",
    },
    "fantom": {
        0: "0x0f854EA9F38ceA4B1c2FC79047E9D0134419D5d6",
        1: "0x8cC6e2144906e81F496429A1590Ef5f86bb7558f",
        2: "0xF0d4c12A5768D806021F80a262B4d39d26C58b8D",
        3: "0x686d67265703d1f124c45e33d47d794c566889ba",
        4: "0x2B039565B2b7a1A9192D4847fbd33B25b836B950",
        5: "0x4fb93D7d320E8A263F22f62C2059dFC2A8bCbC4c",
        11: "0x9AF14D26075f142eb3F292D5065EB3faa646167b",
        12: "0xe61Fb97Ef6eBFBa12B36Ffd7be785c1F5A2DE66b",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        14: "0xCA8d0747B5573D69653C3aC22242e6341C36e4b4",
        15: "0xA72C85C258A81761433B4e8da60505Fe3Dd551CC",
        19: "0x1E4F97b9f9F913c46F1632781732927B9019C68b",
        20: "0xDb205f215f568ADf21b9573b62566f6d9a40bed6",
        21: "0xd62Ade30F740de7ef766008258B4b2F574A084F7",
        22: "0x837814ba42c6f3B39f0A5060168F7027695DDAb1",
        23: "0x42113C6818ACb87ca3CaFDbBc6a6ae396f1548E6",
        24: "0x49C8De2D10C9A56DD9A59ab5Ca1216111276394C",
    },
    "avalanche": {
        0: "0x8474DdbE98F5aA3179B3B3F5942D724aFcdec9f6",
        1: "0xADf698e4d8Df08b3E2c79682891636eF00F6e205",
        2: "0xBff334F8D5912AC5c4f2c590A2396d1C5d990123",
        3: "0xb17b674D9c5CB2e441F8e196a2f048A81355d031",
        4: "0x06534b0BF7Ff378F162d4F348390BDA53b15fA35",
        11: "0x3d6cB2F6DcF47CDd9C13E4e3beAe9af041d8796a",
        12: "0x1764ee18e8B3ccA4787249Ceb249356192594585",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        14: "0xCA8d0747B5573D69653C3aC22242e6341C36e4b4",
        15: "0xA72C85C258A81761433B4e8da60505Fe3Dd551CC",
        20: "0xDb205f215f568ADf21b9573b62566f6d9a40bed6",
        21: "0xeD953C2849785A8AEd7bC2ee8cf5fdE776E1Dc07",
        22: "0x33F9A2F3B85e7D4Ff4f9286a9a8525060100D855",
        23: "0x1309DB123020F0533aFAfaF11D26286d5871bEB0",
        24: "0xad422855ac8010f82F08696CA7750EfE061aa6D6",
    },
    "aurora": {
        0: "0x5b5cfe992adac0c9d48e05854b2d91c73a003858",
        1: "0x0f9cb53ebe405d49a0bbdbd291a65ff571bc83e1",
        2: "0x6600e98b71dabfd4a8cac03b302b0189adb86afb",
        4: "0xf3A431008396df8A8b2DF492C913706BDB0874ef",
        11: "0x3d6cB2F6DcF47CDd9C13E4e3beAe9af041d8796a",
        12: "0x5eeE3091f747E60a045a2E715a4c71e600e31F6E",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        14: "0xCA8d0747B5573D69653C3aC22242e6341C36e4b4",
        15: "0xA72C85C258A81761433B4e8da60505Fe3Dd551CC",
    },
    "celo": {
        3: "0x5277A0226d10392295E8D383E9724D6E416d6e6C",
        4: "0x56bc95Ded2BEF162131905dfd600F2b9F1B380a4",
        11: "0x3d6cB2F6DcF47CDd9C13E4e3beAe9af041d8796a",
        12: "0x1764ee18e8B3ccA4787249Ceb249356192594585",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        14: "0xCA8d0747B5573D69653C3aC22242e6341C36e4b4",
        15: "0xA72C85C258A81761433B4e8da60505Fe3Dd551CC",
    },
    "kava": {
        0: "0xc1C49622b63B961ce1D352ecb7D8261Ab5556695",
        1: "0x4244eB811D6e0Ef302326675207A95113dB4E1F8",
        2: "0xF0d4c12A5768D806021F80a262B4d39d26C58b8D",
        3: "0x40bc62805471eF53DdD5C5cF99ed3d9e5aa81b48",
        4: "0x1f0e8445Ebe0D0F60A96A7cd5BB095533cb15B58",
        11: "0x3d6cB2F6DcF47CDd9C13E4e3beAe9af041d8796a",
        12: "0x1764ee18e8B3ccA4787249Ceb249356192594585",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        14: "0xCA8d0747B5573D69653C3aC22242e6341C36e4b4",
        15: "0xA72C85C258A81761433B4e8da60505Fe3Dd551CC",
        20: "0xabC000d88f23Bb45525E447528DBF656A9D55bf5",
        21: "0xeC6a886148B38C233B07cc6732142dccaBF1051D",
        22: "0x6e53131F68a034873b6bFA15502aF094Ef0c5854",
        23: "0xA177D2bd2BD723878bD95982c0855291953f74C9",
    },
    # No UI:
    "linea": {
        4: "0xf3A431008396df8A8b2DF492C913706BDB0874ef",
        11: "0xd125E7a0cEddF89c6473412d85835450897be6Dc",
        12: "0x5eeE3091f747E60a045a2E715a4c71e600e31F6E",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
    },
    "mantle": {
        4: "0xf3A431008396df8A8b2DF492C913706BDB0874ef",
        11: "0x0C9D8c7e486e822C29488Ff51BFf0167B4650953",
        12: "0x5eeE3091f747E60a045a2E715a4c71e600e31F6E",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
        21: "0xfe87a6cdca1eeb90987c6a196a1c5f5c76f5f2b0",
        22: "0x024d362f7aa162d8591304016fd60a209efc527e",
        23: "0x4339b53cf7f6eec1a997ceea81165e45c1244429",
        24: "0x77A214bd4ee3650e5608339BBbE04b09f5546ECF",
    },
    "scroll": {
        4: "0xf3A431008396df8A8b2DF492C913706BDB0874ef",
        11: "0xC1b393EfEF38140662b91441C6710Aa704973228",
        12: "0x5eeE3091f747E60a045a2E715a4c71e600e31F6E",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
    },
    "polygon-zkevm": {
        4: "0x8b3EFBEfa6eD222077455d6f0DCdA3bF4f3F57A6",
        11: "0x76303e4fDcA0AbF28aB3ee42Ce086E6503431F1D",
        12: "0xd2002373543Ce3527023C75e7518C274A51ce712",
        13: "0x98EE851a00abeE0d95D08cF4CA2BdCE32aeaAF7F",
    },
}
