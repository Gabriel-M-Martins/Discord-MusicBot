class Queue:
    def __init__(self):
        self.current_music_url = ''
        self.current_music_title = ''
        self.current_music_thumb = ''
        self.last_title_enqueued = ''
        self.queue = []

    def enqueue(self, music_title, music_url, music_thumb):
        if len(self.queue) > 0:
            self.queue.append((music_title, music_url, music_thumb))
            self.last_title_enqueued = music_title
        else:
            self.queue.append((music_title, music_url, music_thumb))
            self.current_music_url = music_url
            self.current_music_title = music_title
            self.current_music_thumb = music_thumb

    # corrigir para tirar a música da esquerda
    # se tem /mus1/mus2/ na queue, quando chegar a mus2, tem que tirar a mus1 pra atual ser sempre a primeira da queue
    def dequeue(self):
        pass
        # if self.queue:
        #     self.queue.pop(len(self.queue)-1)

    def previous(self):
        index = self.queue.index((self.current_music_title, self.current_music_url, self.current_music_thumb)) - 1
        if index > 0:
            self.current_music_title = self.queue[index][0]
            self.current_music_url = self.queue[index][1]
            self.current_music_thumb = self.queue[index][2]

    def next(self):
        if (self.current_music_title, self.current_music_url, self.current_music_thumb) in self.queue:
            index = self.queue.index((self.current_music_title, self.current_music_url, self.current_music_thumb)) + 1
            if len(self.queue) - 1 >= index:
                if self.current_music_title == self.queue[index][0] and len(self.queue) - 1 > index + 1:
                    self.current_music_title = self.queue[index + 1][0]
                    self.current_music_url = self.queue[index + 1][1]
                    self.current_music_thumb = self.queue[index + 1][2]
                else:
                    self.current_music_title = self.queue[index][0]
                    self.current_music_url = self.queue[index][1]
                    self.current_music_thumb = self.queue[index][2]
        else:
            self.clear_queue()

    def theres_next(self):
        if self.queue.index((self.current_music_title, self.current_music_url, self.current_music_thumb)) + 1 > len(self.queue) - 1:
            return False
        else:
            return True

    def clear_queue(self):
        self.queue.clear()
        self.current_music_url = ''
        self.current_music_title = ''
        self.current_music_thumb = ''


class Session:
    def __init__(self, guild, channel, id=0):
        self.id = id
        self.guild = guild
        self.channel = channel
        self.q = Queue()
