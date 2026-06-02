import pytest

from main import OPTIONS, WINNING_CASES, determine_winner, is_valid_choice


def test_is_valid_choice_accepts_all_options():
    for choice in OPTIONS:
        assert is_valid_choice(choice) is True


def test_is_valid_choice_rejects_invalid_option():
    assert is_valid_choice("fire") is False
    assert is_valid_choice("") is False
    assert is_valid_choice("Rock") is False


def test_determine_winner_returns_tie_for_same_choice():
    for choice in OPTIONS:
        assert determine_winner(choice, choice) == "tie"


def test_determine_winner_returns_user_on_valid_winning_pairs():
    for user_choice, defeats in WINNING_CASES.items():
        for computer_choice in defeats:
            assert determine_winner(user_choice, computer_choice) == "user"
            assert determine_winner(computer_choice, user_choice) == "computer"
