from os import environ

SESSION_CONFIGS = [
    {
        'name': 'classroom_experiments_public',
        'display_name': "Classroom Survey",
        'num_demo_participants': 10,
        'app_sequence': ['classroom_experiments_public'],
        "use_conjunction_fallacy_linda": True,
        "use_base_rate_fallacy_medical_test": True,
        "use_anchoring_percentage_african_un": True,
        "use_availability_percentage_english_n_ing": True,
        "use_base_rate_vs_similarity_steve_profession": True,
        "use_loss_aversion_cruise_ship": True,
        "use_allais_paradox": True,
    },
    {
        'name': 'test',
        'num_demo_participants': 10,
        'app_sequence': ['classroom_experiments_public'],
        "use_conjunction_fallacy_linda": False,
        "use_base_rate_fallacy_medical_test": False,
        "use_anchoring_percentage_african_un": False,
        "use_availability_percentage_english_n_ing": False,
        "use_base_rate_vs_similarity_steve_profession": False,
        "use_loss_aversion_cruise_ship": False,
        "use_allais_paradox": False,
    },
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '2583614803917'
