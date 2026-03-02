CONFIG = {
    "secureauthdb_creds": {
        "DB_USER": "client_onboarding",
        "DB_PASS": "hemoswehi4ed9Tu7lcr",
        "DB_HOST": "ventura-dev-non-cash.c6yfnqlwrfuo.ap-south-1.rds.amazonaws.com",
        "DB_NAME": "secureauth_db",
        "DB_PORT": 5454,
        # "DB_USER": "sso",
        # "DB_PASS": "k2cE1oquHlthofr8$upr",
        # "DB_HOST": "ventura-dev-non-cash.c6yfnqlwrfuo.ap-south-1.rds.amazonaws.com",
        # "DB_NAME": "user_profile"
    }
}

def get_config(env):
    return CONFIG[env]