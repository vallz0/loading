import time


class Loading:
    def __init__(self, dots=None):
        self.dots = dots if dots else [".", "..", "..."]

    def show(self, duration: int):
        """
        Exibe o efeito de carregamento no terminal.

        :param duration: Tempo total (em segundos) que o carregamento deve durar.
        """
        cycles = len(self.dots)
        delay = duration / (cycles * duration // cycles)

        for _ in range(duration // cycles):
            for dot in self.dots:
                print(f"\rLoading{dot: <3}", end="")
                time.sleep(delay)
        print("\rLoading... Done!")  # Finaliza a mensagem
