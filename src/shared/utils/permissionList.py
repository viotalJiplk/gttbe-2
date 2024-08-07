class EventPermissions:
    create = "event.create"
    read = "event.read"
    update = "event.update"
    delete = "event.delete"
    listAll = "event.listAll"
    listMatches = "event.listMatches"
class GamePermissions:
    # create = "game.create"
    read = "game.read"
    update = "game.update"
    # delete = "game.delete"
    listAll = "game.listAll"
class GamePagePermissions:
    # create = "gamePage.create"
    read = "gamePage.read"
    update = "gamePage.update"
    # delete = "gamePage.delete"
class MatchPermissions:
    create = "match.create"
    read = "match.read"
    update = "match.update"
    delete = "match.delete"
class PagePermissions:
    # create = "page.create"
    read = "page.read"
    # update = "page.update"
    # delete = "page.delete"
class SchoolsPermissions:
    # create = "school.create"
    # read = "school.read"
    # update = "school.update"
    # delete = "school.delete"
    listAll = "school.listAll"
class StagePermissions:
    create = "stage.create"
    read = "stage.read"
    update = "stage.update"
    delete = "stage.delete"
class TeamPermissions:
    create = "team.create"
    read = "team.read"
    # update = "team.update"
    # delete = "team.delete"
    join = "team.join"
    kickTeam = "team.kickTeam"
    kick = "team.kick"
    leave = "team.leave"
    listUsers = "team.listUsers"
    listParticipating = "team.listPartic"
    listParticipatingDiscord = "team.listParticDisc"
    generateJoinString = "team.genJoinStr"
    generateJoinStringMyTeam = "team.genJoinStrMy"
class UserPermissions:
    read = "user.read"
    update = "user.update"
    delete = "user.delete"
    listTeams = "user.listTeams"
    readMe = "user.readMe"
    updateMe = "user.updateMe"
    deleteMe = "user.deleteMe"
    listTeamsMe = "user.listTeamsMe"
    exists = "user.exists"
    permissionList = "user.permissionList"
    permissionListMe = "user.permsListMe"

class PermissionList:
    event = EventPermissions()
    game = GamePermissions()
    gamePage = GamePagePermissions()
    match = MatchPermissions()
    page = PagePermissions()
    school = SchoolsPermissions()
    stage = StagePermissions()
    team = TeamPermissions()
    user = UserPermissions()

perms = PermissionList()
