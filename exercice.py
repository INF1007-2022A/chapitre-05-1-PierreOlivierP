#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number <0:
        number = number * -1
    return number


def use_prefixes() -> List[str]:
    List = []
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    for i in prefixes:
        List.append(i+suffixe)
    return List


def prime_integer_summation() -> int:
    a = 0
    i = 3
    n = 2
    nombres = [2]
    resultat = 0
    while a <99:
        if n == i:
            i+=1
            n = 1
            a+=1
            nombres.append(i)
        if i%n ==0:
            i+=1
            n = 1
        n+=1
    for i in nombres:
        resultat += i




    return resultat


def factorial(number: int) -> int:
    factoriel = 1
    while number >1:
        factoriel = factoriel*number
        number-=1
    return factoriel


def use_continue() -> None:

    pass
    """""
    i = 1
    a = []
    while i<10:
        if i ==5:
            continue
            a.append(i)
        i+=1
    return a
    """""

def verify_ages(groups: List[List[int]]) -> List[bool]:
    pass
    #afaire
    """bon = []
    for groupe in groups:
        if len(groupe) > 3 or len(groupe) < 10:
            if groupe == 25:
                bon.append(groups)
            continue
        if (max(groupe) < 70 ) and (min(groupe) > 18):

            bon.append(groupe)
            continue
        if groupe == 25 and groupe not in bon:
            bon.append(groupe)
            continue


    return bon"""


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
