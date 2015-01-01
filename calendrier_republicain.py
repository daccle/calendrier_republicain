#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Daniel Clerc <mail@clerc.eu> - 2014-09-03

Translates the current date and time to date and time in Calendrier républicain
see: http://fr.wikipedia.org/wiki/Calendrier_r%C3%A9publicain
"""

from datetime import datetime
from datetime import date


def heure_republicain(timeobj=datetime.now()):
    dec_sec_of_day = (timeobj.hour * 3600 + timeobj.minute * 60 + timeobj.second) / 0.864
    dec_hours = dec_sec_of_day / 10000
    dec_minutes = (dec_sec_of_day - int(dec_hours) * 10000) / 100
    dec_seconds = ((dec_sec_of_day - int(dec_hours) * 10000) - int(dec_minutes) * 100)

    return (int(dec_hours), int(dec_minutes), int(dec_seconds))


def date_republicain(today=date.today()):
    """
    for reference:

    -Mois d'automne (terminaison en aire)
    Vendémiaire (22 septembre ~ 21 octobre) - Période des vendanges
    Brumaire (22 octobre ~ 20 novembre) - Période des brumes et des brouillards
    Frimaire (21 novembre ~ 20 décembre) - Période des froids (frimas)

    -Mois d'hiver (terminaison en ose à l'origine, abusivement orthographiée ôse par la suite)
    Nivôse (21 décembre ~ 19 janvier) - Période de la neige
    Pluviôse (20 janvier ~ 18 février) - Période des pluies
    Ventôse (19 février ~ 20 mars) - Période des vents

    -Mois du printemps (terminaison en al)
    Germinal (21 mars ~ 19 avril) - Période de la germination
    Floréal (20 avril ~ 19 mai) - Période de l'épanouissement des fleurs
    Prairial (20 mai ~ 18 juin) - Période des récoltes des prairies

    -Mois d'été (terminaison en idor)
    Messidor (19 juin ~ 18 juillet) - Période des moissons
    Thermidor (19 juillet ~ 17 août) - Période des chaleurs
    Fructidor (18 août ~ 16 septembre) - Période des fruits
    """

    mois = (("Vendémiaire", (22, 9, 21, 10)),
            ("Brumaire", (22, 10, 20, 11)),
            ("Frimaire", (21, 11, 20, 12)),
            ("Nivôse", (21, 12, 19, 1)),
            ("Pluviôse", (20, 1, 18, 2)),
            ("Ventôse", (19, 2, 20, 3)),
            ("Germinal", (21, 3, 19, 4)),
            ("Floréal", (20, 4, 19, 5)),
            ("Prairial", (20, 5, 18, 6)),
            ("Messidor", (19, 6, 18, 7)),
            ("Thermidor", (19, 7, 17, 8)),
            ("Fructidor", (18, 8, 16, 9)))

    def current_year(today=today):
        # FIXME: the year start on the 22th of september each year
        return today.year - 1792

    def in_mois((start_day, start_month, end_day, end_month), today=today):
        """
        if today is in between start and end date return day of month,
        else return 0
        """
        start_date = date(today.year, start_month, start_day)
        if(start_month > end_month):
            start_date = date(today.year-1, start_month, start_day)
        end_date = date(today.year, end_month, end_day)
        if today >= start_date and today <= end_date:
            return (today - start_date).days + 1
        return 0

    # just indices to access the tuple of tuples easier, ugly but they do the job:
    date_range = 1
    name = 0

    for m in mois:
        day_of_month = in_mois(m[date_range])
        if day_of_month != 0:
            return day_of_month, m[name], current_year()


def main():
    print "Temps du jour républicaine: %02d:%02d:%02d" % heure_republicain()
    print "Date républicaine: %d. %s %d" % date_republicain()

if __name__ == '__main__':
    main()
