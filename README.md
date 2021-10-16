# RC-Circuit-Simulation
    
    Nume: Sturzu Cosmin
    Grupa: 322AB
    Facultatea de Automatica si Calculatoare, IS

    Tema a fost realizata in PYTHON si am folosit bibliotecile: "matplotlib", "numpy" si "scipy".

    Rulare (subsistem ubuntu, Python 3.6.9): 
        $ python3 script.py

    Scopul programului: trasarea a doua grafice pentru un circuit RC (serie cu intrare pe rezistenta, iesire pe condensator legat la Vcc) care vor arata incarcarea si descarcarea condensatorului din circuit la intrarea unui semnal patrat cu perioada 2T(T timp este pe ”1” logic, T timp este pe ”0” logic).

    Programul va primi date de la utilizator pentru cele 2 cazuri(R1, C1 si R2, C2) si va reazliza 2 fisiere png, cu graficele cerute.

    Am ales perioada T = 0.2s si pentru cele 2 cazuri voi avea:
                1) 3*tau = 0.0384 < T = 0.2 (R1 = 1600ohm, C1 = 8 microF)
                2) 3*tau = 0.3276 < T = 0.2 (R2 = 9100ohm, C2 = 12 microF)
    Semnalul de intrare este unul patratic cu Vmax = 5V si Vmin = 0V, acesta a fost realizat cu ajutorul bibliotecii scipy.

    In continuare am construit 2 vectori (grafic_1 si grafic_2) pentru cazurile 3*tau<T si 3*tau>T folosindu-ma de formulele specifice si tinand cont de valorile semnalului de intrare (daca semnalul este pe 1 logic(5V), condensatorul se incarca, altfel acesta se descarca).

    Ultimul pas a fost trasarea graficelor folosind cei doi vectori construiti, acestea au fost trasate cu ajutorul bibliotectii "matplotlib". In fig1.png am trasat 3 grafice(unul cu semnalul de intrare si doua pentru cazurile calculate), fiecare pe cate un sistem de axe propriu, iar in fig2.png acestea sunt trasate in acelasi sistem de axe pentru a se putea observa diferenta dintre acestea.




