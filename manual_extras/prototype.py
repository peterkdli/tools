from numpy.testing._private.parameterized import parameterized


def seat_extra(state, cost):
    return {
        "state": state,
        "type": "seat",
        "cost": cost,
    }


TRANSFERABLE_AIRLINE = "TRANSFERABLE"
UNTRANSFERABLE_AIRLINE = "UNTRANSFERABLE"

TRANSFERABLE_AIRLINES = [TRANSFERABLE_AIRLINE]


def single_leg_no_extras(leg_number):
    return {
        'leg_number': leg_number,
        'airline': UNTRANSFERABLE_AIRLINE,
        "extras": [],
        'segments': [1]
    }


def single_leg_with_1_paid_extras_transferable(leg_number, extra_state="inactive"):
    return {
        'leg_number': leg_number,
        'airline': TRANSFERABLE_AIRLINE,
        "extras": [seat_extra(extra_state, 10)],
        'segments': [1]
    }


def single_leg_with_1_paid_extras_untransferable(leg_number, extra_state="inactive"):
    return {
        'leg_number': leg_number,
        'airline': UNTRANSFERABLE_AIRLINE,
        "extras": [seat_extra(extra_state, 10)],
        'segments': [1]
    }


def single_leg_with_1_free_extras_transferable(leg_number, extra_state="inactive"):
    return {
        'leg_number': leg_number,
        'airline': TRANSFERABLE_AIRLINE,
        "extras": [seat_extra(extra_state, 0)],
        'segments': [1]
    }


def single_leg_with_1_free_extras_untransferable(leg_number, extra_state="inactive"):
    return {
        'leg_number': leg_number,
        'airline': UNTRANSFERABLE_AIRLINE,
        "extras": [seat_extra(extra_state, 0)],
        'segments': [1]
    }


def single_leg_with_multiple_extras(leg_number, extras):
    return {
        'leg_number': leg_number,
        'airline': UNTRANSFERABLE_AIRLINE,
        "extras": extras,
        'segments': [1]
    }



########## Both legs being modified ############

# In these scenarios, all extras will be made inactive,
# because both legs are deleted and recreated

# first we have 1 extra in the modification
two_legs_with_1_inactive_paid_extras_transferable = [
    single_leg_with_1_paid_extras_transferable(1),
    single_leg_no_extras(2)
]
two_legs_with_1_inactive_paid_extras_untransferable = [
    single_leg_with_1_paid_extras_untransferable(1),
    single_leg_no_extras(2)
]

two_legs_with_1_inactive_free_extras_transferable = [
    single_leg_with_1_free_extras_transferable(1),
    single_leg_no_extras(2)
]
two_legs_with_1_inactive_free_extras_untransferable = [
    single_leg_with_1_free_extras_untransferable(1),
    single_leg_no_extras(2)
]

two_legs_with_no_extras_at_all = [
    single_leg_no_extras(1),
    single_leg_no_extras(2)
]
# From here on 2 extras
# You cannot have both a paid and free extra in the same scenario
# You also cannot have different airlines per leg
two_legs_with_2_inactive_paid_extras_untransferable = [
    single_leg_with_1_paid_extras_untransferable(1),
    single_leg_with_1_paid_extras_untransferable(2)
]
two_legs_with_2_inactive_paid_extras_transferable = [
    single_leg_with_1_paid_extras_transferable(1),
    single_leg_with_1_paid_extras_transferable(2)
]

two_legs_with_2_inactive_free_extras_untransferable = [
    single_leg_with_1_free_extras_untransferable(1),
    single_leg_with_1_free_extras_untransferable(2)
]

two_legs_with_2_inactive_free_extras_transferable = [
    single_leg_with_1_free_extras_transferable(1),
    single_leg_with_1_free_extras_transferable(2)
]

# From here we have only one leg being modified, so there will be some active extras
# inital assumption is all will be single segment
two_legs_outbound_modified_free_extra_untransferable = [
    single_leg_with_1_free_extras_untransferable(1, "inactive"),
    single_leg_no_extras(2)
]
two_legs_outbound_modified_no_extras_on_outbound = [
    single_leg_no_extras(1),
    single_leg_with_1_free_extras_untransferable(2, "active")
]

two_legs_outbound_modified_paid_extra_untransferable = [
    single_leg_with_1_paid_extras_untransferable(1, "inactive"),
    single_leg_with_1_paid_extras_untransferable(2, "active")
]

two_legs_outbound_modified_paid_extra_transferable = [
    single_leg_with_1_paid_extras_transferable(1, "inactive"),
    single_leg_with_1_paid_extras_transferable(2, "active")
]


# Lets look at the more niche cases. In this example, lets imagine a travelfusion booking
# where the agent adds the free extra to both legs manually during the modification. In this case, we
# don't want to show the banner, because the agent has already added the extra

two_legs_manual_mod_agent_readded_extra_free = [
    single_leg_with_multiple_extras(1, [seat_extra("active", 0), seat_extra("inactive", 0)]),
    single_leg_with_multiple_extras(2, [seat_extra("active", 0), seat_extra("inactive", 0)])
]

# now lets imagine the same scenario, but the agent only added one of the seats for some reason
two_legs_manual_mod_agent_readded_only_one_extra_free = [
    single_leg_with_multiple_extras(1, [seat_extra("inactive", 0)]),
    single_leg_with_multiple_extras(2, [seat_extra("active", 0), seat_extra("inactive", 0)])
]

# now lets imagine that the booking went from two segments to one segment, as a one leg journey
# there will be two inactive extras, and no active ones, so we will show the banner
single_leg_automated_mod_2_to_1_segment_free = [
{
        'leg_number': 1,
        'airline': UNTRANSFERABLE_AIRLINE,
        "extras": [seat_extra("inactive", 0), seat_extra("inactive", 0)],
        'segments': [1]
    }
]

# Now there was 1 segment originally, so only one inactive exta, but there are two segments now
single_leg_automated_mod_1_to_2_segment_free = [
{
        'leg_number': 1,
        'airline': UNTRANSFERABLE_AIRLINE,
        "extras": [seat_extra("inactive", 0)],
        'segments': [1, 2]
}]

# Now the above two but with an agent who came in and created the extras manually
single_leg_manual_mod_2_to_1_segment_free = [
{
        'leg_number': 1,
        'airline': UNTRANSFERABLE_AIRLINE,
        "extras": [seat_extra("inactive", 0), seat_extra("inactive", 0), seat_extra("active", 0), seat_extra("active", 0)],
        'segments': [1]
    }
]

single_leg_manual_mod_1_to_2_segment_free = [
{
        'leg_number': 1,
        'airline': UNTRANSFERABLE_AIRLINE,
        "extras": [seat_extra("inactive", 0), seat_extra("active", 0), seat_extra("active", 0)],
        'segments': [1, 2]
}]


def initialize_extras_counter(num_legs):
    return {i + 1: {"active": 0, "inactive": 0} for i in range(num_legs)}


def update_extras_counter(leg, extras_counter):
    leg_extras = leg.get("extras", [])
    for extra in leg_extras:
        free_or_transferable = (extra["cost"] == 0 or leg["airline"] in TRANSFERABLE_AIRLINES)
        if free_or_transferable:
            extras_counter[leg["leg_number"]][extra["state"]] += 1


def should_show_banner_confirmation_email(scenario):
    extras_counter_by_leg = initialize_extras_counter(len(scenario))

    for leg in scenario:
        update_extras_counter(leg, extras_counter_by_leg)

    num_active_extras = sum([extras_counter["active"] for extras_counter in extras_counter_by_leg.values()])
    num_inactive_extras = sum([extras_counter["inactive"] for extras_counter in extras_counter_by_leg.values()])
    num_segments = sum([len(leg["segments"]) for leg in scenario])

    return num_inactive_extras > 0 and num_active_extras < num_segments

@parameterized.expand([
    ### one leg
    ([single_leg_no_extras(1)], False),
    ([single_leg_with_1_paid_extras_transferable(1)], True),
    ([single_leg_with_1_paid_extras_untransferable(1)], False),
    ([single_leg_with_1_free_extras_transferable(1)], True),
    ([single_leg_with_1_free_extras_untransferable(1)], True), # 4
    ### two legs
    ## both modified
    # one extra
    (two_legs_with_no_extras_at_all, False),
    (two_legs_with_1_inactive_paid_extras_transferable, True),
    (two_legs_with_1_inactive_paid_extras_untransferable, False),
    (two_legs_with_1_inactive_free_extras_transferable, True),
    (two_legs_with_1_inactive_free_extras_untransferable, True),
    # two extras, one per leg
    (two_legs_with_2_inactive_paid_extras_untransferable, False),
    (two_legs_with_2_inactive_paid_extras_transferable, True), # 11
    (two_legs_with_2_inactive_free_extras_untransferable, True),
    (two_legs_with_2_inactive_free_extras_transferable, True),

    ## only one leg modified
    # unmodified leg had no extras
    (two_legs_outbound_modified_free_extra_untransferable, True),
    # modified leg had no extras
    (two_legs_outbound_modified_no_extras_on_outbound, False),

    (two_legs_outbound_modified_paid_extra_untransferable, False), # 16
    (two_legs_outbound_modified_paid_extra_transferable, True),
    (two_legs_manual_mod_agent_readded_extra_free, False),
    (two_legs_manual_mod_agent_readded_only_one_extra_free, True), # 19
    (single_leg_automated_mod_2_to_1_segment_free, True),
    (single_leg_automated_mod_1_to_2_segment_free, True),
    (single_leg_manual_mod_2_to_1_segment_free, False),
    (single_leg_manual_mod_1_to_2_segment_free, False),

])
def test_should_show_confirmation_page(scenario, result):
    assert should_show_banner_confirmation_email(scenario) == result
