import statistics

def get_results_conjunction_fallacy_linda(subsession):
    linda_banking_list = []
    linda_banking_feminist_list = []
    for p in subsession.get_players():
        if p.experiment_finished:
            linda_banking_list.append(p.linda_rank_bank)
            linda_banking_feminist_list.append(p.linda_rank_bank_feminist)

    # catch the case where no player has finished yet
    if len(linda_banking_list) >0:
        average_rank_banking = round(statistics.mean(linda_banking_list),2)
        average_rank_banking_feminist = round(statistics.mean(linda_banking_feminist_list), 2)
    else:
        average_rank_banking = average_rank_banking_feminist = None
    return average_rank_banking, average_rank_banking_feminist


def get_results_base_rate_fallacy_medical_test(subsession):
    medical_test_percentage_list = [p.test_accuracy for p in subsession.get_players() if p.experiment_finished]
    if len(medical_test_percentage_list) > 0:
        medical_test_accuracy_average_percentage = round(statistics.mean(medical_test_percentage_list), 2)
    else:
        medical_test_accuracy_average_percentage = None
    return medical_test_accuracy_average_percentage


def get_results_anchoring_percentage_african_un(subsession):
    list_africa_un_anchor_10 = []
    list_africa_un_anchor_65 = []
    for p in subsession.get_players():
        if p.experiment_finished:
            if p.africa_un_is_treatment_anchor_10:
                list_africa_un_anchor_10.append(p.anchoring_percentage_african_un)
            else:
                list_africa_un_anchor_65.append(p.anchoring_percentage_african_un)
    if len(list_africa_un_anchor_10)> 0:
        percentage_africa_un_10 = round(statistics.mean(list_africa_un_anchor_10), 2)
    else:
        percentage_africa_un_10 = None
    if len(list_africa_un_anchor_65 )> 0:
        percentage_africa_un_65 = statistics.mean(list_africa_un_anchor_65)
    else:
        percentage_africa_un_65 = None
    return percentage_africa_un_10, percentage_africa_un_65


def get_results_use_availability_percentage_english_n_ing(subsession):
    list_share_n = []
    list_share_ing = []
    for p in subsession.get_players():
        if p.experiment_finished:
            if p.english_is_treatment_n:
                list_share_n.append(p.availability_percentage_english_n_ing)
            else:
                list_share_ing.append(p.availability_percentage_english_n_ing)
    if len(list_share_n) > 0:
        percentage_n_english = round(statistics.mean(list_share_n), 2)
    else:
        percentage_n_english = None
    if len(list_share_ing) > 0:
        percentage_ing_english = round(statistics.mean(list_share_ing), 2)
    else:
        percentage_ing_english = None
    return percentage_n_english, percentage_ing_english


def get_results_base_rate_vs_similarity_steve_profession(subsession):
    list_of_probability_farmer_rank = []
    list_of_probability_salesman_rank = []
    list_of_probability_pilot_rank = []
    list_of_probability_librarian_rank = []
    list_of_probability_physician_rank = []

    list_of_similarity_farmer_rank = []
    list_of_similarity_salesman_rank = []
    list_of_similarity_pilot_rank = []
    list_of_similarity_librarian_rank = []
    list_of_similarity_physician_rank = []
    for p in subsession.get_players():
        if p.experiment_finished:
            if p.steve_treatment_is_probability:
                list_of_probability_farmer_rank.append(p.steve_farmer_rank)
                list_of_probability_salesman_rank.append(p.steve_salesman_rank)
                list_of_probability_pilot_rank.append(p.steve_pilot_rank)
                list_of_probability_librarian_rank.append(p.steve_librarian_rank)
                list_of_probability_physician_rank.append(p.steve_physician_rank)
            else:
                list_of_similarity_farmer_rank.append(p.steve_farmer_rank)
                list_of_similarity_salesman_rank.append(p.steve_salesman_rank)
                list_of_similarity_pilot_rank.append(p.steve_pilot_rank)
                list_of_similarity_librarian_rank.append(p.steve_librarian_rank)
                list_of_similarity_physician_rank.append(p.steve_physician_rank)
    if len(list_of_probability_farmer_rank) > 0:
        average_probability_farmer_rank = round(statistics.mean(list_of_probability_farmer_rank), 2)
        average_probability_salesman_rank = round(statistics.mean(list_of_probability_salesman_rank), 2)
        average_probability_pilot_rank = round(statistics.mean(list_of_probability_pilot_rank), 2)
        average_probability_librarian_rank = round(statistics.mean(list_of_probability_librarian_rank), 2)
        average_probability_physician_rank = round(statistics.mean(list_of_probability_physician_rank), 2)
    else:
        average_probability_farmer_rank = None
        average_probability_salesman_rank = None
        average_probability_pilot_rank = None
        average_probability_librarian_rank = None
        average_probability_physician_rank = None

    if len(list_of_similarity_farmer_rank) > 0:
        average_similarity_farmer_rank = round(statistics.mean(list_of_similarity_farmer_rank), 2)
        average_similarity_salesman_rank = round(statistics.mean(list_of_similarity_salesman_rank), 2)
        average_similarity_pilot_rank = round(statistics.mean(list_of_similarity_pilot_rank), 2)
        average_similarity_librarian_rank = round(statistics.mean(list_of_similarity_librarian_rank), 2)
        average_similarity_physician_rank = round(statistics.mean(list_of_similarity_physician_rank), 2)
    else:
        average_similarity_farmer_rank = None
        average_similarity_salesman_rank = None
        average_similarity_pilot_rank = None
        average_similarity_librarian_rank = None
        average_similarity_physician_rank = None
    temp_dict = {
        "average_probability_farmer_rank": average_probability_farmer_rank,
        "average_probability_salesman_rank": average_probability_salesman_rank,
        "average_probability_pilot_rank": average_probability_pilot_rank,
        "average_probability_librarian_rank": average_probability_librarian_rank,
        "average_probability_physician_rank": average_probability_physician_rank,
        "average_similarity_farmer_rank": average_similarity_farmer_rank,
        "average_similarity_salesman_rank": average_similarity_salesman_rank,
        "average_similarity_pilot_rank": average_similarity_pilot_rank,
        "average_similarity_librarian_rank": average_similarity_librarian_rank,
        "average_similarity_physician_rank": average_similarity_physician_rank,

    }

    return temp_dict


def get_results_loss_aversion_cruise_ship(subsession):
    loss_aversion_cruise_ship_gain_treatment_number_option_a = 0
    loss_aversion_cruise_ship_gain_treatment_number_option_b = 0
    loss_aversion_cruise_ship_loss_treatment_number_option_a = 0
    loss_aversion_cruise_ship_loss_treatment_number_option_b = 0
    for p in subsession.get_players():
        if p.experiment_finished:
            if p.loss_aversion_cruise_ship_gain_treatment:
                if p.option_chosen_loss_aversion_cruise_ship == 1:
                    loss_aversion_cruise_ship_gain_treatment_number_option_a += 1
                else:
                    loss_aversion_cruise_ship_gain_treatment_number_option_b += 1
            else:
                if p.option_chosen_loss_aversion_cruise_ship == 1:
                    loss_aversion_cruise_ship_loss_treatment_number_option_a += 1
                else:
                    loss_aversion_cruise_ship_loss_treatment_number_option_b += 1
    return_list = [
        loss_aversion_cruise_ship_gain_treatment_number_option_a,
        loss_aversion_cruise_ship_gain_treatment_number_option_b,
        loss_aversion_cruise_ship_loss_treatment_number_option_a,
        loss_aversion_cruise_ship_loss_treatment_number_option_b
    ]
    return return_list


def get_results_allais_paradox(subsession):
    allais_paradox_66_2400_lottery_a = 0
    allais_paradox_66_2400_lottery_b = 0
    allais_paradox_66_0_lottery_a = 0
    allais_paradox_66_0_lottery_b = 0
    for p in subsession.get_players():
        if p.experiment_finished:
            if p.allais_treatment_is_66_2400:
                if p.option_chosen_allais_paradox == 1:
                    allais_paradox_66_2400_lottery_a += 1
                else:
                    allais_paradox_66_2400_lottery_b += 1
            else:
                if p.option_chosen_allais_paradox == 1:
                    allais_paradox_66_0_lottery_a += 1
                else:
                    allais_paradox_66_0_lottery_b += 1
    return allais_paradox_66_2400_lottery_a, allais_paradox_66_2400_lottery_b, allais_paradox_66_0_lottery_a, allais_paradox_66_0_lottery_b


