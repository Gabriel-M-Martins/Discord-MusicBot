class Queue:
    """
    A class used to represent a queue.

    This class handles all sort of Queue operations, making it easy to just
    call these methods in main.py without worrying about breaking anything in queue.

    Attributes
    ----------
    current_music_url : str
        The current url of the current music the bot is playing.

    current_music_title : str
        The current name of the current music the bot is playing.

    current_music_thumb : str
        The current thumbnail url of the current music the bot is playing.

    last_title_enqueued : str
        The title of the last music enqueued.

    queue : tuple list
        The actual queue of songs to play.
        (title, url, thumb)

    Methods
    -------
    enqueue(music_title, music_url, music_thumb)
        Handles enqueue process appending the music tuple to the queue
        while setting last_title_enqueued and the current_music variables as needed

    dequeue()
        TO DO!
        Removes the last music enqueued from the queue.

    previous()
        Goes back one place in queue, ensuring that the previous song isn't a negative index.
        current_music variables are set accordingly.

    next()
        Sets the next music in the queue as the current one.

    theres_next()
        Checks if there is a music in the queue after the current one.

    clear_queue()
        Clears the queue, resetting all variables.

    """
    def __init__(self):
        self.current_music_url = ''
        self.current_music_title = ''
        self.current_music_thumb = ''
        self.last_title_enqueued = ''
        self.queue = []

    def enqueue(self, music_title, music_url, music_thumb):
        """
        Handles enqueue process appending the music tuple to the queue
        while setting last_title_enqueued and the current_music variables as needed

        :param music_title: str
            The music title to be added to queue
        :param music_url: str
            The music url to be added to queue
        :param music_thumb: str
            The music thumbnail url to be added to queue
        :return: None
        """
        if len(self.queue) > 0:
            self.queue.append((music_title, music_url, music_thumb))
            self.last_title_enqueued = music_title
        else:
            self.queue.append((music_title, music_url, music_thumb))
            self.current_music_url = music_url
            self.current_music_title = music_title
            self.current_music_thumb = music_thumb

    def dequeue(self):
        pass
        # if self.queue:
        #     self.queue.pop(len(self.queue)-1)

    def previous(self):
        """
        Goes back one place in queue, ensuring that the previous song isn't a negative index.
        current_music variables are set accordingly.

        :return: None
        """
        index = self.queue.index((self.current_music_title, self.current_music_url, self.current_music_thumb)) - 1
        if index > 0:
            self.current_music_title = self.queue[index][0]
            self.current_music_url = self.queue[index][1]
            self.current_music_thumb = self.queue[index][2]

    def next(self):
        """
        Sets the next music in the queue as the current one.

        :return: None
        """
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
        """
        Checks if there is a music in the queue after the current one.

        :return: bool
            True if there is a next song in queue.
            False if there isn't a next song in queue.
        """
        if self.queue.index((self.current_music_title, self.current_music_url, self.current_music_thumb)) + 1\
                > len(self.queue) - 1:
            return False
        else:
            return True

    def clear_queue(self):
        """
        Clears the queue, resetting all variables.

        :return: None
        """
        self.queue.clear()
        self.current_music_url = ''
        self.current_music_title = ''
        self.current_music_thumb = ''


class Session:
    """
    A class used to represent an instance of the bot.

    To avoid mixed queues when there's more than just one guild sending commands to the bot, I came up with the concept
    of sessions. Each session is identified by its guild and voice channel where the bot is connected playing audio, so
    it's impossible to send a music from one guild to another by mistake. :)

    Attributes
    ----------
    id : int
        Session's number ID.

    guild : str
        Guild's name where the bot is connected.

    channel : str
        Voice channel where the bot is connected.
    """
    def __init__(self, guild, channel, id=0):
        """
        :param guild: str
             Guild's name where the bot is connected.
        :param channel: str
            Voice channel where the bot is connected.
        :param id: int
            Session's number ID.
        """
        self.id = id
        self.guild = guild
        self.channel = channel
        self.q = Queue()
