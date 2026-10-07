import numpy as np

# Ensemble des mesures effectuées
mesures = [ 49.01 ,
            53.64 ,
            53.30 ,
            51.08 ,
            51.77 ,
            53.64 ,
            51.46 ,
            45.91 ,
            55.60 ,
            55.52 ]

# Calcul moyenne
moyenne = np.mean(mesures)
print('valeur moyenne des mesures =', moyenne)

# Calcul ecart-type
ecartType = np.std(mesures,ddof=1)
print('écart-type des mesures =', ecartType)


