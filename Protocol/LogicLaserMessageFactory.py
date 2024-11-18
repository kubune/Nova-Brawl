from Protocol.Messages.Client.Home.EndClientTurnMessage import EndClientTurnMessage
from Protocol.Messages.Client.Home.LoginMessage import LoginMessage
from Protocol.Messages.Client.Home.KeepAliveMessage import KeepAliveMessage
from Protocol.Messages.Client.Home.SetNameMessage import SetNameMessage
from Protocol.Messages.Client.Team.TeamCreateMessage import TeamCreateMessage
from Protocol.Messages.Client.Team.TeamLeaveMessage import TeamLeaveMessage
from Protocol.Messages.Client.Team.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage
from Protocol.Messages.Client.Team.TeamToggleSettingsMessage import TeamToggleSettingsMessage
from Protocol.Messages.Client.Team.TeamSetLocationMessage import TeamSetLocationMessage
from Protocol.Messages.Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Protocol.Messages.Client.Battle.StartGameMessage import StartGameMessage
from Protocol.Messages.Client.Home.GetPlayerProfileMessage import GetPlayerProfileMessage
from Protocol.Messages.Client.Leaderboard.GetLeaderboardMessage import GetLeaderboardMessage
from Protocol.Messages.Client.Home.SetSupportedCreatorMessage import SetSupportedCreatorMessage
from Protocol.Messages.Client.Battle.AskForBattleEndMessage import AskForBattleEndMessage
from Protocol.Messages.Client.Home.AvatarNameCheckRequestMessage import AvatarNameCheckRequestMessage
from Protocol.Messages.Client.Alliance.CreateAllianceMessage import CreateAllianceMessage
from Protocol.Messages.Client.Alliance.AskForAllianceDataMessage import AskForAllianceDataMessage
from Protocol.Messages.Client.Alliance.ChangeAllianceSettingsMessage import ChangeAllianceSettingsMessage
from Protocol.Messages.Client.Alliance.JoinAllianceMessage import JoinAllianceMessage
from Protocol.Messages.Client.Alliance.AskForJoinableAlliancesListMessage import AskForJoinableAlliancesListMessage
from Protocol.Messages.Client.Alliance.LeaveAllianceMessage import LeaveAllianceMessage
from Protocol.Messages.Client.Alliance.SearchAlliancesMessage import SearchAlliancesMessage
from Protocol.Messages.Client.Alliance.ChatToAllianceStreamMessage import ChatToAllianceStreamMessage

packets = {
    10101: LoginMessage,
    14103: StartGameMessage,
    10108: KeepAliveMessage,
    10212: SetNameMessage,
    
    14102: EndClientTurnMessage,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: AskForBattleEndMessage,
    14113: GetPlayerProfileMessage,
    14301: CreateAllianceMessage,
    14302: AskForAllianceDataMessage,
    14303: AskForJoinableAlliancesListMessage,
    14305: JoinAllianceMessage,
    14308: LeaveAllianceMessage,
    14315: ChatToAllianceStreamMessage,
    14316: ChangeAllianceSettingsMessage,
    14324: SearchAlliancesMessage,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14354: TeamChangeMemberSettingsMessage,
    14363: TeamSetLocationMessage,
    14372: TeamToggleSettingsMessage,
    14403: GetLeaderboardMessage,
    14600: AvatarNameCheckRequestMessage,
    
    18686: SetSupportedCreatorMessage,
}
