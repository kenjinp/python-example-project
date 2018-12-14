# -*- coding: utf-8 -*-
import pytest
import animalsounds


def test_generator_cat():
    sound = animalsounds.generator("cat")
    assert sound == "meow"


def test_generator_dog():
    sound = animalsounds.generator("dog")
    assert sound == "woof"


def test_generator_fish():
    sound = animalsounds.generator("fish")
    assert sound == "..."


def test_generator_notfound():
    with pytest.raises(Exception):
        animalsounds.generator("emu")
