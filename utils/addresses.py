import smartpy as sp

####################################### MULTISIG ########################################
CHAINID = "0x7a06a770"
MULTISIG = sp.address("KT1Q8yKdJaU5VcBL8JcxUT9PU99m53ubERk4")

####################################### ORACLES #########################################
GENERIC_ORACLE = sp.address("KT1KzdDAVkEwLUhemZBp8asMJ9nvfbp6eV9C")

################################### TOKENS CONTRACTS #################################### 
GOVERNANCE_TOKEN_ADDRESS = sp.address("KT1Xobej4mc6XgEjDoJoHtTKgbD1ELMvcQuL")
YOU_TOKEN_ID = 0
SYNTHETIC_ASSETS_TOKEN_ADDRESS = sp.address("KT1XRPEPXbZK25r3Htzp2o1x7xdMMmfocKNW")
UUSD_TOKEN_ID = 0
UDEFI_TOKEN_ID = 1
UBTC_TOKEN_ID = 2
UXTZ_TOKEN_ID = 3

################################## YOU STAKES MANAGER ################################### 
LEGACY_STAKE_MANAGER = sp.address("KT1QxGP2FphgSQ3Duaj74JFPWAa2LqsHwNyo")
STAKE_MANAGER = sp.address("KT1Ge5usHwAAH12PDxwP8FFYMdbMbXSRXSz4")

################################### REWARD_POOL #########################################
UNIFIED_STAKING_POOL = sp.address("KT1UZcNDxTdkn33Xx5HRkqQoZedc3mEs11yV")
UNIFIED_STAKING_POOL_PROXY = sp.address("KT1KXvsh7vnPUkBj1oG1E3LUoFnKHsf7Wixo")

################################### YOUVES DAO  #########################################
YOUVES_DAO = sp.address("KT1C3T98TqCm38cHPauZ4SopkQ4torCsxgab")

################################## SAVINGS POOL #########################################
LEGACY_UUSD_SAVINGS_POOL = sp.address("KT1TMfRfmJ5mkJEXZGRCsqLHn2rgnV1SdUzb")
LEGACY_UDEFI_SAVINGS_POOL = sp.address("KT1Kvg5eJVuYfTC1bU1bwWyn4e1PRGKAf6sy")
LEGACY_UBTC_SAVINGS_POOL = sp.address("KT1KNbtEBKumoZoyp5uq6A4v3ETN7boJ9ArF")
UUSD_SAVINGS_POOL = sp.address("KT18bG4ctcB6rh7gPEPjNsWF8XkQXL2Y1pJe")
UBTC_SAVINGS_POOL = sp.address("KT1WT8hZsixALTmxcM3SDzCyh4UF8hYXVaUb")
UXTZ_SAVINGS_POOL = sp.address("KT1KShHvxW69YukaGetdgYRTw31d9BX8ijfF")

################################### ENGINES ############################################# 
LEGACY_UUSD_TEZ_ENGINE = sp.address("KT1FFE2LC5JpVakVjHm5mM36QVp2p3ZzH4hH")
LEGACY_UUSD_SIRS_ENGINE = sp.address("KT1FzcHaNhmpdYPNTgfb8frYXx7B5pvVyowu")
LEGACY_UUSD_TZBTC_ENGINE = sp.address("KT1HxgqnVjGy7KsSUTEsQ6LgpD5iKSGu7QpA")
UUSD_USDT_ENGINE = sp.address("KT1JmfujyCYTw5krfu9bSn7YbLYuz2VbNaje")
UUSD_TEZ_ENGINE = sp.address("KT1DHndgk8ah1MLfciDnCV2zPJrVbnnAH9fd")
UUSD_TZBTC_ENGINE = sp.address("KT1V9Rsc4ES3eeQTr4gEfJmNhVbeHrAZmMgC")
UUSD_SIRS_ENGINE = sp.address("KT1F1JMgh6SfqBCK6T6o7ggRTdeTLw91KKks")
UUSD_TEZ_ZERO_MINTING_FEE = sp.address("KT1TcCSR24TmDvwTfHkyWbwMB111gtNYxEcA")
UUSD_SIRS_ZERO_MINTING_FEE = sp.address("KT1H2514Wb6G38fmgU3vpAwkWEpFC9sq7HPH")

LEGACY_UDEFI_UUSD_ENGINE = sp.address("KT1B2GSe47rcMCZTRk294havTpyJ36JbgdeB")
LEGACY_UDEFI_TEZ_ENGINE = sp.address("KT1LQcsXGpmLXnwrfftuQdCLNvLRLUAuNPCV")
LEGACY_UDEFI_SIRS_ENGINE = sp.address("KT1E45AvpSr7Basw2bee3g8ri2LK2C2SV2XG")

LEGACY_UBTC_TEZ_ENGINE = sp.address("KT1VjQoL5QvyZtm9m1voQKNTNcQLi5QiGsRZ")
LEGACY_UBTC_SIRS_ENGINE = sp.address("KT1NFWUqr9xNvVsz2LXCPef1eRcexJz5Q2MH")
UBTC_TEZ_ENGINE = sp.address("KT1CP1C8afHqdNfBsSE3ggQhzM2iMHd4cRyt")
UBTC_SIRS_ENGINE = sp.address("KT1G6RzVX25YnoU55Xb7Vve3zvuZKmouf24a")
UBTC_TZBTC_ENGINE = sp.address("KT1XH5rKSd6Ae3DAMYi26gEZP1gxAoQRYRfS")
UBTC_TZBTC_ZERO_MINTING_FEE_ENGINE = sp.address("KT18x66448Gt3kYYkfvx4Cg2dP9cRPfjQwVv")
UBTC_SIRS_ZERO_MINTING_FEE_ENGINE = sp.address("KT1SEjPmaeVPMu4Ep94ggF3tLqzFM83T3pBd")

UXTZ_USDT_ENGINE = sp.address("KT1AnDFRcdB652Jy5JFtmu7SampSPAzDkK7g")
UXTZ_TEZ_ENGINE = sp.address("KT1Mf9Nr1KyGC6gUz9pGQnngzWbbZ6thShvc")
UXTZ_SIRS_ENGINE = sp.address("KT1ByNrcyDxYLmamuJbeFJukYkLJaZ1W86Yr")

CCHF_TEZ_ENGINE = sp.address("KT1LrEJsaTR5vMdwjvASTtFPUbk2wnX3P166")

############################ INTEREST RATE SETTERS ###################################### 
UUSD_INTEREST_RATE_SETTER = sp.address("KT1ULhdEg9hPJQwmL88VU1tr43pW6BVieJDr")
UBTC_INTEREST_RATE_SETTER = sp.address("KT1NBvjQqwZ9tiWsre4PfynexcA3XhBBy2uZ")
LEGACY_UBTC_INTEREST_RATE_SETTER = sp.address("KT1EDej7V87Sduu3Go6P2YYkbbaGeYXyxDkD")

###################################### FARMS ############################################
UUSD_USDT_FARM = sp.address("KT1USKq4gHFVs7WJSVsqKn8j8P4tmqZcgSbd")
UUSD_UBTC_FARM = sp.address("KT1KGfEyxBeCU873RfuwrU1gy8sjC1s82WZV")
UUSD_KUSD_FARM = sp.address("KT1HaWDWv7XPsZ54JbDquXV6YgyazQr9Jkp3")

UUSD_USDCE_FARM = sp.address("KT1CpXvNd293VvHkY7M9krjBvwEFuvura65Q")
UXTZ_XTZ_FARM = sp.address("KT1HbzGokeEZ4hu1KRAAw2fyB61RCpBhQXKA")

#################################### EXCHANGES ##########################################
UUSD_USDT_EXCHANGE = sp.address("KT1UJBvm4hv11Uvu6r4c8zE5K2EfmwiRVgsm")
UUSD_USDCE_EXCHANGE = sp.address("KT1NgbaaYhtXh3MwJoYYxrrKUwG3RX5LYVL6")
UUSD_WUSDC_EXCHANGE = sp.address("KT1JeWiS8j1kic4PHx7aTnEr9p4xVtJNzk5b")
TZBTC_WWBTC_EXCHANGE = sp.address("KT1T974a8qau4xP3RAAWPYCZM9xtwU9FLjPS")
TZBTC_UBTC_EXCHANGE = sp.address("KT1XvH5f2ja2jzdDbv6rxPmecZFU7s3obquN")
WBTCE_UBTC_EXCHANGE = sp.address("KT1CkpDuwCFrnoqTam6upYiPBiFNsSEVbBei")
UUSD_KUSD_EXCHANGE = sp.address("KT1AVbWyM8E7DptyBCu4B5J5B7Nswkq7Skc6")
UUSD_USDTZ_EXCHANGE = sp.address("KT1Xbx9pykNd38zag4yZvnmdSNBknmCETvQV")
UXTZ_XTZ_EXCHANGE = sp.address("KT1WgguedKZWucrdRKQXaRECEPMZennaVPck")
UUSD_UBTC_EXCHANGE = sp.address("KT1STLQKxiRtAh1e7DZhu1xUTAJ7KLpV9Rru")