class Belief:
    """
    Class which apply the Bayes Filter Algorithm
     Attributes
     ------------------------
     bel : float []
        probability distribution over all possible states, conditioned by the observations so far
        bel(xt):=P(xt∣e1:t)
     bel_projected : float []
        probability distribution over all the possible states at time t, given only past observations
        bel⎯projected(xt):=P(xt∣e1:t−1)
     pos : String []
        state domain
     prob_state : list(float [])
        list of probabilities to go in a room given the current room
     sensors_error_rate : list(float [])
        list of probabilities to be in a room given the sensors' measures
     Methods
     -----------------------
     bel_upgrade(self, sensor_output)
    """

    def __init__(self, bel, pos, prob_state, ser, movement_transaction):
        self.bel = bel
        self.bel_projected = [0 for x in range(0, len(pos))]
        self.pos = pos
        self.prob_state = prob_state
        self.sensors_error_rate = ser
        self._movement_transaction = movement_transaction

    @property
    def bel(self):
        return self.__bel

    @bel.setter
    def bel(self, bel):
        self.__bel = bel

    @property
    def bel_projected(self):
        return self.__bel_projected

    @bel_projected.setter
    def bel_projected(self, bel_projected):
        self.__bel_projected = bel_projected

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos

    @property
    def prob_state(self):
        return self.__prob_state

    @prob_state.setter
    def prob_state(self, prob_state):
        self.__prob_state = prob_state

    @property
    def sensors_error_rate(self):
        return self.__sensors_error_rate

    @sensors_error_rate.setter
    def sensors_error_rate(self, sensors_error_rate):
        self.__sensors_error_rate = sensors_error_rate

    def bel_upgrade(self, transactions):
        temp = []
        if self._movement_transaction in transactions:  # se si è acceso un sensore, ossia c'è una tupla 01
            i = transactions.index(self._movement_transaction)  # indice sensore acceso
            self.bel = [x*y for x, y in zip(self.bel_projected, self.sensors_error_rate[i][self._movement_transaction])] # la y è fatta dall'indice della stanza e indice del cambiamento 01 o 10 ecc
            #aggiorno le probabilita di ogni stanza prendendo le probabilita date da sensor error rate che mi dice le probabilita di errore di ognuna data la misura che cambia di un sensore : è P(x=x|y)
        else:
            for i in range(0, len(transactions)):  # se si è spento un sensore
                temp.append([y * x for y, x in zip(self.bel_projected, self.sensors_error_rate[i][transactions[i]])]) # se il sensore si è spento l'algoritmo è diverso!?
            self.bel = [sum(x) for x in zip(*temp)]
        eta = 1/sum(self.bel) # è η
        self.bel = [x * eta for x in self.bel]  # bel(pos′1)=η⋅P(MeasuredColor1=Orange|pos′1)⋅bel¯¯(pos′1)

    def bel_projected_upgrade(self):
        for i in range(0, len(self.pos)):
            self.bel_projected[i] = [x * self.bel[i] for x in self.prob_state[i]]  # moltiplico le probabilita delle possibili scelte di ogni camera per 0.2
        self.bel_projected = [sum(x) for x in zip(*self.bel_projected)]  # zip(*) serve per unzippare e creare parentesi con tutti i primi di self bel projected tutti i secondi ecc che vengono sommati
        # bel¯¯(pos′1)=∑pos′0 P(pos′1|pos′0)⋅bel(pos′0) QUESTO È BEL_PROJECTED
