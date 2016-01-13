"""Övningar på iterators"""

import math

class Cubes():
    """En iterator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.

    """

    def __init__(self):
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.x += 1
        return self.x ** 3
    

class Primes():
    """En iterator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    """
    @staticmethod
    def check_primes(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if (x % i) == 0:
                return False
        return True
    
    def __init__(self):
        self.x = 1  
        
    def __next__(self):
        while True:
            self.x += 1
            if Primes.check_primes(self.x):
                return self.x
    
    def __iter__(self):
        return self    


class Fibonacci():
    """En iterator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """
    def __init__(self):
        pass

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    
    def __next__(self):
        x = self.a 
        self.a, self.b = self.b, self.a + self.b
        return x

class Alphabet():
    """En iterator som returnerar namnen på tecknen i det hebreiska alfabetet.

    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, Tet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """
    pass

class Permutations():
    """En iterator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """
    pass


class LookAndSay():
    """En iterator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """
    def __init__(self):
        pass
    def __intr__(self):
        self.a = 1
        self.b = 10
        return self.a
        return self.a + self.b 

    def __next__(self):
        x = self.a + self.b * 2  






