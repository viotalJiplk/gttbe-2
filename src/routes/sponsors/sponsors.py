from flask_restx import Resource
from utils import postJson, setAttributeFromList, AuthResult, errorList, jwsProtected, hasPermissionDecorator, returnParser, returnError, postJsonParse
from shared.models import SponsorModel
from datetime import datetime, date, time
from shared.utils import perms, DatabaseError
from typing import List
from copy import deepcopy
from helper import getSponsor

accessibleAttributes = {
    "sponsorName": [str],
    "sponsorText": [str],
    "logo": [str]
}

returnableAttributes = deepcopy(accessibleAttributes)
returnableAttributes["sponsorId"] = [int]

class Sponsors(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission])
    @hasPermissionDecorator([perms.sponsor.read, perms.sponsor.listAll], False)
    def get(self, sponsorId, authResult: AuthResult, permissions: List[str]):
        """Gets sponsor
        You can use <sponsorId> = all to list all sponsors.

        Args:
            sponsorId (str): id of the sponsor or 'all'

        Returns:
            dict: info about sponsor or sponsors
        """
        if(sponsorId == "all"):
            if perms.sponsor.listAll in permissions:
                return SponsorModel.getAllDict(), 200
            else:
                raise errorList.permission.missingPermission
        else:
            if perms.sponsor.read:
                sponsor = getSponsor(sponsorId)
                return sponsor.toDict(), 200
            else:
                raise errorList.permission.missingPermission

    @postJson(accessibleAttributes)
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.data.couldNotConvertInt, errorList.data.unableToConvert])
    @hasPermissionDecorator(perms.sponsor.update, False)
    def put(self, sponsorId, data, authResult: AuthResult, permissions: List[str]):
        """Updates sponsor

        Args:
            sponsorId (str): id of the sponsor

        Returns:
            dict: info about sponsor
        """
        sponsor = getSponsor(sponsorId)
        setAttributeFromList(sponsor, data, accessibleAttributes)
        return sponsor.toDict()

    @returnParser({"sponsorId": [int]}, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.data.stillDepends])
    @hasPermissionDecorator(perms.sponsor.delete, False)
    def delete(self, sponsorId, authResult: AuthResult, permissions: List[str]):
        """Deletes sponsor

        Args:
            sponsorId (str): id of the sponsor

        Returns:
            dict: info about sponsor
        """
        sponsor = getSponsor(sponsorId)
        try:
            sponsor.delete()
        except DatabaseError as e:
            raise errorList.data.stillDepends
        return {"sponsorId": sponsor.sponsorId}, 200

class SponsorCreate(Resource):
    @returnParser(returnableAttributes, 201, False, False)
    @postJsonParse(expectedJson=accessibleAttributes)
    @hasPermissionDecorator(perms.sponsor.create, False)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates sponsor

        Args:

        Returns:
            dict: info about sponsor
        """
        return SponsorModel.create(data["sponsorName"], data["sponsorText"], data["logo"]).toDict(), 201
