# @kubune

from ByteStream import Writer

class TeamStreamMessage(Writer):
    def __init__(self, client, player, message):
        super().__init__(client)
        self.id = 24131
        self.player = player
        self.client = client
        self.message = message
        
    def encode(self):
        self.writeVInt(0) # High id
        self.writeVInt(1) # Low id, for the room
        
        MessagesCount = 1
        self.writeVInt(MessagesCount) # Messages Count
        for msg in range(MessagesCount):
            self.writeVInt(2) # event or something
            self.writeVInt(0)
            self.writeVInt(msg+1) #tick
            
            self.writeVInt(0) # High Id for player
            self.writeVInt(self.player.ID)
            self.writeString(self.player.name)
            
            self.writeVInt(0)
            self.writeVInt(0) # TID STREAM ENTRY AGE
            
            self.writeVInt(0)
            
            self.writeString(self.message) # Message
        