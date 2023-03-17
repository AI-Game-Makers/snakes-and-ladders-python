import random

class Board:
    def __init__(self, size=10, num_snakes=5, num_ladders=5, snakes=None, ladders=None):
        self.size = size
        self.num_snakes = num_snakes
        self.num_ladders = num_ladders
        self.snakes = snakes if snakes is not None else {}
        self.ladders = ladders if ladders is not None else {}

        if not snakes or not ladders:
            self._generate_snakes_and_ladders()

    def _generate_snakes_and_ladders(self):
        for _ in range(self.num_snakes):
            self._add_snake()

        for _ in range(self.num_ladders):
            self._add_ladder()

    def _add_snake(self):
        head = random.randint(self.size + 1, self.size * self.size - 1)
        tail = random.randint(1, head - 1)

        while head in self.snakes or tail in self.snakes.values():
            head = random.randint(self.size + 1, self.size * self.size - 1)
            tail = random.randint(1, head - 1)

        self.snakes[head] = tail

    def _add_ladder(self):
        start = random.randint(1, self.size * self.size - self.size - 1)
        end = random.randint(start + 1, self.size * self.size)

        while start in self.ladders or end in self.ladders.values():
            start = random.randint(1, self.size * self.size - self.size - 1)
            end = random.randint(start + 1, self.size * self.size)

        self.ladders[start] = end

    def move(self, current_position, dice_roll):
        new_position = current_position + dice_roll

        if new_position in self.snakes:
            new_position = self.snakes[new_position]
        elif new_position in self.ladders:
            new_position = self.ladders[new_position]

        return min(new_position, self.size * self.size)

    def is_winning_position(self, position):
        return position == self.size * self.size
