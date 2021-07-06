from collections import deque
from functools import partial

import numpy as np

class WolffMonteCarlo:
    """Wolff Monte Carlo simulator for Ising model."""

    def __init__(self, L, T, method=None):
        self._L = L
        self._T = T
        self._K = 2. / T

        # set up updater
        self._updater = partial(self.wolff_iterative, method=method)

        # set up initial state
        self._state = np.random.randint(0, 2, size=[L, L])

    @property
    def L(self):
        return self._L

    @property
    def T(self):
        return self._T

    @property
    def K(self):
        return self._K

    @property
    def state(self):
        return self._state

    def probability_add_bond(self, x1, y1, x2, y2, state):
        """The probability for adding a bond."""
        return 1. - np.exp(-self.K * (1. if state[x1, y1] == state[x2, y2] else 0.))

    def set_T(self, T):
        self._T = T
        self._K = 2. / T

    def wolff_iterative(self, state, method=None):
        """ Iterative Wolff algorithm based on deque. """

        # geometry
        L = self.L
        left = [L - 1] + list(range(L - 1))
        right = list(range(1, L)) + [0]
        # book-keeping containers
        sites_to_consider = deque()
        sites_to_flip = set()
        bonds_considered = set()

        # Initial queue of sites to consider, just consisting of a single site
        sites_to_consider.append((
            np.random.randint(0, L),
            np.random.randint(0, L)
        ))

        # As long as there are sites to consider
        while sites_to_consider:

            # Pick a new site to consider from the queue, either using
            # breadth first or depth first
            if method == "BFS":
                # queue
                x1, y1 = sites_to_consider.popleft()
            if method == "DFS":
                # stack
                x1, y1 = sites_to_consider.pop()

            # For each neighbor of this site
            for x2, y2 in zip([left[x1], right[x1], x1, x1],
                              [y1, y1, left[y1], right[y1]]):
                # Check if we have not already considered this pair
                if not (x1, y1, x2, y2) in bonds_considered:
                    # Add the pair so that we don't flip it twice
                    bonds_considered.add((x1, y1, x2, y2))
                    bonds_considered.add((x2, y2, x1, y1))

                    if np.random.rand() < self.probability_add_bond(x1, y1, x2, y2, state):
                        if method == "BFS":
                            sites_to_consider.append((x2, y2))
                        if method == "DFS":
                            sites_to_consider.append((x2, y2))

                        sites_to_flip.add((x1, y1))
                        sites_to_flip.add((x2, y2))
        return sites_to_flip

    def step(self):
        """Use Wolff and perform update."""

        # Get a list of sites to flip...
        to_flip = self._updater(self._state)

        # ...and flip them
        for (x, y) in to_flip:
            # 0 and 1, not -1 and 1
            self._state[x, y] = 1 - self._state[x, y]

        return to_flip
