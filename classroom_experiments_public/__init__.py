from otree.api import *
import itertools, random
from .admin_report_functions import *
author = 'Your name here'
doc = """
A set of classic behavioural experiment to be used in teaching.
"""


class Constants(BaseConstants):
    name_in_url = 'classroom_experiments'
    players_per_group = None
    num_rounds = 1
    header_template = 'classroom_experiments_public/Header.html'


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    players = subsession.get_players()
    # balanced treatment randomisation
    list_true_false = [True, False]
    random.shuffle(list_true_false)
    africa_un_cycle = itertools.cycle(list_true_false)
    random.shuffle(list_true_false)
    english_n_ing_cycle = itertools.cycle(list_true_false)
    random.shuffle(list_true_false)
    steve_probability_cycle = itertools.cycle(list_true_false)
    random.shuffle(list_true_false)
    loss_aversion_cruise_ship_cycle = itertools.cycle(list_true_false)
    random.shuffle(list_true_false)
    allais_cycle = itertools.cycle(list_true_false)
    for p in players:
        p.africa_un_is_treatment_anchor_10 = next(africa_un_cycle)
        p.english_is_treatment_n = next(english_n_ing_cycle)
        p.steve_treatment_is_probability = next(steve_probability_cycle)
        p.loss_aversion_cruise_ship_gain_treatment = next(loss_aversion_cruise_ship_cycle)
        p.allais_treatment_is_66_2400 = next(allais_cycle)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    experiment_finished = models.BooleanField(initial=False)
    
    # medical test
    test_accuracy = models.IntegerField(min=0, max=100)
    # linda
    linda_rank_elementary = models.IntegerField()
    linda_rank_feminist = models.IntegerField()
    linda_rank_bank = models.IntegerField()
    linda_rank_psychiatric = models.IntegerField()
    linda_rank_insurance = models.IntegerField()
    linda_rank_bank_feminist = models.IntegerField()
    linda_rank_book_yoga = models.IntegerField()
    # steve
    steve_treatment_is_probability = models.BooleanField()
    steve_farmer_rank = models.IntegerField()
    steve_pilot_rank = models.IntegerField()
    steve_salesman_rank = models.IntegerField()
    steve_librarian_rank = models.IntegerField()
    steve_physician_rank = models.IntegerField()
    # english ing
    english_is_treatment_n = models.BooleanField()
    availability_percentage_english_n_ing = models.FloatField(min=0, max=100)
    
    # percentage african countries in un
    africa_un_is_treatment_anchor_10 = models.BooleanField()
    un_above = models.BooleanField(choices=[[True, "Above"], [False, "Below"]],)
    anchoring_percentage_african_un = models.FloatField(min=0, max=100)
    # loss aversion
    loss_aversion_cruise_ship_gain_treatment = models.BooleanField()
    option_chosen_loss_aversion_cruise_ship = models.IntegerField()
    # allais paradox
    allais_treatment_is_66_2400 = models.BooleanField()
    option_chosen_allais_paradox = models.IntegerField()
    

# FUNCTIONS
def vars_for_admin_report(subsession):
    # make results dictionary
    results_dictionary = {}
    if subsession.session.config["use_conjunction_fallacy_linda"]:
        average_rank_banking, average_rank_banking_feminist = get_results_conjunction_fallacy_linda(subsession)
        results_dictionary["average_rank_banking"] = average_rank_banking
        results_dictionary["average_rank_banking_feminist"] = average_rank_banking_feminist
    if subsession.session.config["use_availability_percentage_english_n_ing"]:
        percentage_n_english, percentage_ing_english = get_results_use_availability_percentage_english_n_ing(subsession)
        results_dictionary["percentage_n_english"] = percentage_n_english
        results_dictionary["percentage_ing_english"] = percentage_ing_english
    if subsession.session.config["use_anchoring_percentage_african_un"]:
        percentage_africa_un_10, percentage_africa_un_65 = get_results_anchoring_percentage_african_un(subsession)
        results_dictionary["percentage_africa_un_10"] = percentage_africa_un_10
        results_dictionary["percentage_africa_un_65"] = percentage_africa_un_65
    if subsession.session.config["use_base_rate_fallacy_medical_test"]:
        results_dictionary["medical_test_accuracy_average_percentage"] = get_results_base_rate_fallacy_medical_test(subsession)
    if subsession.session.config["use_base_rate_vs_similarity_steve_profession"]:
        temp_dict = get_results_base_rate_vs_similarity_steve_profession(subsession)
        results_dictionary = {**results_dictionary, **temp_dict}
    if subsession.session.config["use_loss_aversion_cruise_ship"]:
        temp_list = get_results_loss_aversion_cruise_ship(subsession)
        results_dictionary["loss_aversion_cruise_ship_gain_treatment_number_option_a"] = temp_list[0]
        results_dictionary["loss_aversion_cruise_ship_gain_treatment_number_option_b"] = temp_list[1]
        results_dictionary["loss_aversion_cruise_ship_loss_treatment_number_option_a"] = temp_list[2]
        results_dictionary["loss_aversion_cruise_ship_loss_treatment_number_option_b"] = temp_list[3]
    if subsession.session.config["use_allais_paradox"]:
        allais_paradox_66_2400_lottery_a, allais_paradox_66_2400_lottery_b, allais_paradox_66_0_lottery_a, allais_paradox_66_0_lottery_b = get_results_allais_paradox(subsession)
        results_dictionary["allais_paradox_66_2400_lottery_a"] = allais_paradox_66_2400_lottery_a
        results_dictionary["allais_paradox_66_2400_lottery_b"] = allais_paradox_66_2400_lottery_b
        results_dictionary["allais_paradox_66_0_lottery_a"] = allais_paradox_66_0_lottery_a
        results_dictionary["allais_paradox_66_0_lottery_b"] = allais_paradox_66_0_lottery_b
    return results_dictionary


# PAGES
class base_rate_fallacy_medical_test(Page):
    form_model = 'player'
    form_fields = [
        "test_accuracy",
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.session.config["use_base_rate_fallacy_medical_test"]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "page_title": "Medical Test",
        }


class base_rate_vs_similarity_steve_profession(Page):
    form_model = 'player'
    form_fields = [
        'steve_farmer_rank',
        'steve_pilot_rank',
        'steve_salesman_rank',
        'steve_librarian_rank',
        'steve_physician_rank',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.session.config["use_base_rate_vs_similarity_steve_profession"]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "page_title": "Steve",
        }


class conjunction_fallacy_linda(Page):
    form_model = 'player'
    form_fields = [
        "linda_rank_elementary",
        "linda_rank_feminist",
        "linda_rank_bank",
        "linda_rank_psychiatric",
        "linda_rank_insurance",
        "linda_rank_bank_feminist",
        "linda_rank_book_yoga",
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.session.config["use_conjunction_fallacy_linda"]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "page_title": "Linda",
        }


class availability_percentage_english_n_ing(Page):
    form_model = 'player'
    form_fields = ['availability_percentage_english_n_ing']

    @staticmethod
    def is_displayed(player: Player):
        return player.session.config["use_availability_percentage_english_n_ing"]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "page_title": "English Words",
        }


class anchoring_percentage_african_un(Page):
    form_model = 'player'
    form_fields = ['anchoring_percentage_african_un', 'un_above']

    @staticmethod
    def is_displayed(player: Player):
        return player.session.config["use_anchoring_percentage_african_un"]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "page_title": "Africa in the UN",
        }


class loss_aversion_cruise_ship(Page):
    form_model = 'player'
    form_fields = ["option_chosen_loss_aversion_cruise_ship"]

    @staticmethod
    def is_displayed(player: Player):
        return player.session.config["use_loss_aversion_cruise_ship"]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "page_title": "Cruise Ship in a Storm",
        }


class allais_paradox(Page):
    form_model = 'player'
    form_fields = ["option_chosen_allais_paradox"]

    @staticmethod
    def is_displayed(player: Player):
        return player.session.config["use_allais_paradox"]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "page_title": "Lotteries",
        }


class experiment_over(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.experiment_finished = True
        return {
            "page_title": "Experiment Over"
        }


page_sequence = [
    base_rate_vs_similarity_steve_profession,
    conjunction_fallacy_linda,
    base_rate_fallacy_medical_test,
    anchoring_percentage_african_un,
    availability_percentage_english_n_ing,
    loss_aversion_cruise_ship,
    allais_paradox,
    experiment_over,
]
