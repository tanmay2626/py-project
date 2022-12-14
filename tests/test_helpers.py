import pytest
from app import helpers


def test_get_separate_event_list():
    #arrage
    log_dna_events = [{
        'message':
        "[event] signed_up: Test_SlawaShev (shevslawa@gmail.com, xyx@outlook.com, 37626862+SlawaShev@users.noreply.github.com) signed up.",
        'timestamp': '2022-05-21T12:54:50.605805+00:00'
    }, {
        'message':
        "[event] failed_stage: Test_SlawaShev failed stage #2 of the redis course using Python. Delay: 4s.",
        'timestamp': '2022-05-21T12:54:50.605805+00:00'
    }, {
        'message':
        "[event] violated_daily_limit: Test_Fearkin violated the daily limit when completing stage #4 of the redis challenge.",
        'timestamp': '2022-05-21T12:54:50.605805+00:00'
    }]
    expected_signup_events = {
        "Test_SlawaShev": {
            "name":
            "Test_SlawaShev",
            "primary_email":
            "shevslawa@gmail.com",
            "other_email":
            ["xyx@outlook.com", "37626862+SlawaShev@users.noreply.github.com"],
            "events":
            ["failed stage #2 of the redis course using Python. Delay: 4s."],
            "signup_timestamp":
            '2022-05-21T12:54:50.605805+00:00'
        }
    }
    expected_other_events = {
        "Test_SlawaShev":
        ["failed stage #2 of the redis course using Python. Delay: 4s."],
        "Test_Fearkin": [
            "violated the daily limit when completing stage #4 of the redis challenge."
        ]
    }

    #act
    (signup_events, other_events) = helpers.separate_event_list(log_dna_events)

    #assert
    assert signup_events == expected_signup_events
    assert other_events == expected_other_events
