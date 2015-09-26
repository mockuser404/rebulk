#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-self-use, pointless-statement, missing-docstring, invalid-name
from rebulk.rules import Rule


class RemoveAllButLastYear(Rule):
    def when(self, matches, context):
        entries = matches.named('year')
        return entries[:-1]

    def then(self, matches, when_response, context):
        for to_remove in when_response:
            matches.remove(to_remove)


class PrefixedSuffixedYear(Rule):
    def when(self, matches, context):
        toRemove = []
        years = matches.named('year')
        for year in years:
            if not matches.previous(year, lambda p: p.name == 'yearPrefix') and \
                   not matches.next(year, lambda n: n.name == 'yearSuffix'):
                toRemove.append(year)
        return toRemove

    def then(self, matches, when_response, context):
        for to_remove in when_response:
            matches.remove(to_remove)


class PrefixedSuffixedYearNoLambda(Rule):
    def when(self, matches, context):
        toRemove = []
        years = matches.named('year')
        for year in years:
            if not [m for m in matches.previous(year) if m.name == 'yearPrefix'] and \
                    not [m for m in matches.next(year) if m.name == 'yearSuffix']:
                toRemove.append(year)
        return toRemove

    def then(self, matches, when_response, context):
        for to_remove in when_response:
            matches.remove(to_remove)
