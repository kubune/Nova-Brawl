from ByteStream.Reader import Reader
from Protocol.Messages.Server.Team.TeamStreamMessage import TeamStreamMessage

from Protocol.Messages.Server.Home.LoginFailedMessage import LoginFailedMessage

class TeamChatMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.message = self.readString()

    def process(self, db):
        
        if self.message.startswith("/"):
            command = self.message.replace("/", "", 1).split(" ")
            if command[0] == 'server':
                new_server = command[1]
                server_db, player_db, club_db, id, acc_data = db.create_new_server(new_server, db, db.get_server_name(db), self.player.ID)
                LoginFailedMessage(self.client, self.player, f"Changing server to: {new_server}").send()
                return ["ChangeServer", new_server, id, acc_data]
                
        
        TeamStreamMessage(self.client, self.player, self.message).send()
        
        # send packet to the rest of the team later...