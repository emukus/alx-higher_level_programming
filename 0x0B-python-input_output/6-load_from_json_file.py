#!/usr/bin/python3
"""Module for load_from_json method."""
import json


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)
