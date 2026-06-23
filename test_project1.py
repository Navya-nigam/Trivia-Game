import pytest
from project1 import update_score, question_bank

#test 1 - normal score update

def test_update_score():
    score=update_score(0,1)
    assert score==10

#test 2 - streak bonus

def test_update_score_bonus():
    score=update_score(20,3)
    assert score ==35

#test 3 - easy level exists
def test_easy_level_exists():
    assert "Easy" in question_bank

#test 4- medium level exists
def test_medium_level_exists():
    assert "Medium" in question_bank

#test 5 - hard level exists
def test_hard_level_exists():
    assert "Hard" in question_bank

#test 6 - easy has questions
def test_easy_not_empty():
    assert len(question_bank["Easy"])>0

#test 7 - easy has questions
def test_Medium_not_empty():
    assert len(question_bank["Medium"])>0

#test 8 - hard has questions
def test_Hard_not_empty():
    assert len(question_bank["Hard"])>0

#test 9 - questions have answer key
def test_question_structure():
    for level in question_bank:
        for q in question_bank[level]:
            assert "question" in q
            assert "answer" in q
            assert "hint" in q

#test 10 - score never decreases
def test_score_positive():
    score=update_score(50,1)
    assert score>=50