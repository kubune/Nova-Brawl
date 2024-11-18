from ByteStream.Reader import Reader
from Protocol.Messages.Server.Team.TeamStreamMessage import TeamStreamMessage

class TeamChatMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.message = self.readString()

    def process(self, db):
        TeamStreamMessage(self.client, self.player, self.message).send()
        
        # send packet to the rest of the team later...