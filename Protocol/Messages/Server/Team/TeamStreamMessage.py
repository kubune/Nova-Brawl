# @kubune

from ByteStream.Writer import Writer

class TeamStreamMessage(Writer):
    def __init__(self, client, player, message):
        super().__init__(client)
        self.id = 24131
        self.player = player
        self.message = message
        
    def encode(self):
        self.writeLogicLong(1) # Team ID
        
        MessagesCount = 1
        self.writeVInt(MessagesCount) # Messages Count
        
        print(self.message)
        
        for msg in range(MessagesCount):
            self.writeLogicLong(1) # Stream id
            self.writeLogicLong(self.player.ID) # player id
            self.writeString(self.player.name) # player name
            self.writeVInt(0) # role
            self.writeVInt(0) # Timestamp, stream creation
            self.writeBool(False) # unknown
            
            self.writeString(self.message) # Message
        