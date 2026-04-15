from itertools import combinations

from models.candidat import Candidat
from fuzzy.individual import eval_candidat
from fuzzy.team import eval_equipe


def build_candidats():
    return [
        Candidat("Matys", 7, 5, 800, 15, 17, [8,9,10], 10, 20, 15, 40, 17, 10, 1),
        Candidat("Luu Ly", 5, 3, 950, 12, 14, [1,1,1], 1, 60, 85, 13, 15, 100, 1),
        Candidat("Zoe", 5, 3, 825, 14, 16, [2,3,4], 5, 85, 80, 65, 100, 60, 1),
        Candidat("Skander", 20, 5, 900, 19, 20, [7,8,9], 10, 60, 80, 100, 100, 60, 1),
        Candidat("Elio", 30, 5, 700, 17, 20, [12,14,15], 10, 60, 80, 100, 100, 60, 1),
        Candidat("Souleye", 2, 2, 300, 7, 8, [1,1.5,2], 1, 20, 80, 85, 50, 90, 0),
        Candidat("Vicenzo", 0, 2, 650, 5, 8, [0,0.5,1], 2, 60, 80, 100, 100, 60, 1),
    ]


def main():

    candidats = build_candidats()

    # evaluation individuelle
    for c in candidats:
        c.score_eval(eval_candidat(c))

    equipes = list(combinations(candidats, 4))

    results = []

    for e in equipes:
        entente = eval_equipe(e)
        eval_ = sum(c.eval_finale for c in e) / 4

        results.append((e, eval_, entente))

    results.sort(key=lambda x: (x[1] + x[2]), reverse=True)

    print("\nTOP 5 EQUIPES\n")

    for i in range(5):
        e, ev, en = results[i]
        print([c.prenom for c in e])
        print("eval:", ev, "| entente:", en, "\n")


if __name__ == "__main__":
    main()