from ByteStream.Writer import Writer
from Utils.Fingerprint import Fingerprint


class LoginFailedMessage(Writer):

    def __init__(self, client, player, msg):
        super().__init__(client)
        self.id = 20103
        self.player = player
        self.msg = msg
        self.fingerprint = Fingerprint.loadFinger_full("GameAssets/fingerprint.json")

        if len(msg) > 1:
            self.player.err_code = 1
        
        """
        << Error Code List >>
        # 1  = Custom Message
        # 7  = Patch
        # 8  = Update Available
        # 9  = Redirect
        # 10 = Maintenance
        # 11 = Banned
        # 13 = Acc Locked PopUp
        # 16 = Updating Cr/Maintenance/Too high version
        # 18 = Chinese Text?

        """

        if self.player.err_code == 7 or self.player.err_code == 8:
            self.isPatching = True
        else:
            self.isPatching = False

    def encode(self):

        self.writeInt(self.player.err_code)

        if self.isPatching:  # refer to above note about codes
            self.writeString(self.fingerprint)
        else:
            self.writeString()

        self.writeString()  # Server host

        self.writeString(self.player.patch_url)
        self.writeString(self.player.update_url)

        self.writeString(self.msg)

        self.writeInt(self.player.maintenance_time)
        self.writeBoolean(False)

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(3)

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(0)

        self.writeBoolean(False)
        self.writeBoolean(False)
