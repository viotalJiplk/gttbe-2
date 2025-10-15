from .error import ReturnableError

class Jws:
    invalidToken = ReturnableError("Invalid JWS token!", "JWS", 401)
    InvalidSignature = ReturnableError("Invalid JWS signature!", "JWS", 401)
    missingAuthHeader = ReturnableError("Missing Authorization header!", "JWS", 400)
    expired = ReturnableError("Expired!", "JWS", 401)
    untrusted = ReturnableError("Untrusted issuer!", "JWS", 401)
    missingUserId = ReturnableError("Missing userId!", "JWS", 401)
    malformedToken = ReturnableError("Something is missing from token!", "JWS", 400)
    issuedInFuture = ReturnableError("The JWT is issued in future!", 400)
    wrongAudience = ReturnableError("Wrong audience!", 400)
class Json:
    notValidJson = ReturnableError("The data you sent is not a valid json.", "JSON", 401)
class Auth:
    invalidState = ReturnableError("Invalid state.", "Auth", 401)
class Permission:
    missingPermission = ReturnableError("Missing required permissions.", "Perms", 401)
    missingId = ReturnableError("Missing gameId!", "Perms", 400)
class Data:
    stillDepends = ReturnableError("There are still data, that depends on this.", "DATA", 400)
    doesNotExist = ReturnableError("Resource does not exist.", "DATA", 404)
    couldNotConvertDate = ReturnableError("Unable to convert date or time.", "DATA", 400)
    couldNotConvertInt = ReturnableError("Unable to convert string to int.", "DATA", 400)
    unableToConvert = ReturnableError("Unable to convert string to int.", "DATA", 400)
    alreadyExists = ReturnableError("Resource you are trying to create already exists.", "DATA", 424)
class Request:
    missingHeaderForMe = ReturnableError("Missing authentication from jws for @me.", "Request", 400)
class Team:
    missingGameIdOrName = ReturnableError("Missing game_id or name.", "JOIN", 400)
    registrationNotOpened = ReturnableError("Registration is not opened for this game", "JOIN", 410)
    alreadyRegistered = ReturnableError("Already registered for game.", "JOIN", 403)
    noSpaceLeft = ReturnableError("This team already has the maximum number of players permitted in this role.", "JOIN", 403)
    invalidPayload = ReturnableError("Missing fields in payload.", "PAYLOAD", 400)
    notCaptain = ReturnableError("You are not Captain of this team.", "TEAMROLE", 403)
    wrongJoinString = ReturnableError("Wrong joinString.", "JOIN", 403)
    userNotPartOfTeam = ReturnableError("User is not part of the team", "TEAM", 404)
class User:
    couldNotRegister = ReturnableError("You have not filled info required for creating Team.", "User", 400)
class File:
    wrongFileName = ReturnableError("The filename you provided is not a valid filename.", "File", 400)
    noFileUploaded = ReturnableError("There was no file provided in request", "File", 400)
    missingPermission = ReturnableError("Filesystem denied access to this file.", "File", 400)
    fileDoesNotExist = ReturnableError("File does not exist.", "File", 404)
class ErrorList:
    """List of all errors
    """
    jws = Jws()
    permission = Permission()
    data = Data()
    request = Request()
    team = Team()
    user = User()
    json = Json()
    auth = Auth()
    file = File()

errorList = ErrorList()
