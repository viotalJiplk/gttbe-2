class EventPermissions:
    create = "event.create"
    read = "event.read"
    update = "event.update"
    delete = "event.delete"
    listAll = "event.listAll"
    listMatches = "event.listMatches"
    listStages = "event.listStages"
class GamePermissions:
    create = "game.create"
    read = "game.read"
    update = "game.update"
    delete = "game.delete"
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
    listAll = "match.listAll"
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
    listAll = "stage.listAll"
    listMatches = "stage.listMatches"
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
    listParticipating = "team.listParticipating"
    listParticipatingDiscord = "team.listParticipatingDiscord"
    generateJoinString = "team.generateJoinString"
    generateJoinStringMyTeam = "team.generateJoinStringMy"
class UserPermissions:
    read = "user.read"
    update = "user.update"
    delete = "user.delete"
    listTeams = "user.listTeams"
    listTeamsMe = "user.listTeamsMe"
    readMe = "user.readMe"
    updateMe = "user.updateMe"
    deleteMe = "user.deleteMe"
    exists = "user.exists"
    permissionList = "user.permissionList"
    permissionListMe = "user.permsListMe"
    generatedRolesList = "user.generatedRolesList"
    generatedRolesListMe = "user.generatedRolesListMe"
    assignedRolesList = "user.assignedRolesList"
    assignedRolesListMe = "user.assignedRolesListMe"
class AssignedRoles:
    create = "assignedRole.create"
    read = "assignedRole.read"
    update = "assignedRole.update"
    delete = "assignedRole.delete"
    listAll = "generatedRole.listAll"
    listPermissions = "assignedRole.listPermissions"
class AssignedRolePermissions:
    create = "assignedRolePermission.create"
    read = "assignedRolePermission.read"
    update = "assignedRolePermission.update"
    delete = "assignedRolePermission.delete"
class GeneratedRoles:
    create = "generatedRole.create"
    read = "generatedRole.read"
    update = "generatedRole.update"
    delete = "generatedRole.delete"
    listAll = "generatedRole.listAll"
    listPermissions = "generatedRole.listPermissions"
class GeneratedRolePermissions:
    create = "generatedRolePermission.create"
    read = "generatedRolePermission.read"
    update = "generatedRolePermission.update"
    delete = "generatedRolePermission.delete"
class UserRoles:
    create = "userRole.create"
    read = "userRole.read"
    update = "userRole.update"
    delete = "userRole.delete"
class Permissions:
    listAll = "permission.listAll"

class Files:
    read = "file.read"
    upload = "file.upload"
    delete = "file.delete"
    listFiles = "file.listFiles"

class Ranks:
    create = "rank.create"
    read = "rank.read"
    update = "rank.update"
    delete = "rank.delete"
    listRanks = "rank.list"

class Sponsors:
    create = "sponsor.create"
    read = "sponsor.read"
    update = "sponsor.update"
    delete = "sponsor.delete"
    listAll = "sponsor.listAll"

class PermissionList:
    """Permission name translation layer"""
    event = EventPermissions()
    game = GamePermissions()
    gamePage = GamePagePermissions()
    match = MatchPermissions()
    page = PagePermissions()
    school = SchoolsPermissions()
    stage = StagePermissions()
    team = TeamPermissions()
    user = UserPermissions()
    assignedRole = AssignedRoles()
    assignedRolePermission = AssignedRolePermissions()
    generatedRole = GeneratedRoles()
    generatedRolePermission = GeneratedRolePermissions()
    userRole = UserRoles()
    permission = Permissions()
    file = Files()
    rank = Ranks()
    sponsor = Sponsors()

perms = PermissionList()
