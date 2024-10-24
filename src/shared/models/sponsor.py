from ..utils import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from datetime import date
from ..utils import ObjectDbSync
from typing import Union

class SponsorModel(ObjectDbSync):
    """Representation of sponsor
        Attributes:
            sponsorId (int): sponsor id
            sponsorName (str): sponsor name
            sponsorText (str): sponsor text
            sponsorLink (str): sponsor link
            logo (str): sponsor logo
    """
    tableName = "sponsors"
    tableId = "sponsorId"

    def __init__(self, sponsorId=-1, sponsorName="", sponsorText="", sponsorLink="", logo=""):
        self.sponsorId = sponsorId
        self.sponsorName = sponsorName
        self.sponsorText = sponsorText
        self.sponsorLink = sponsorLink
        self.logo = logo
        super().__init__()


    @classmethod
    @dbConn()
    def create(cls, sponsorName, sponsorText, sponsorLink, logo, cursor, db):
        """Creates new sponsor

        Args:
            sponsorName (str): sponsor name
            sponsorText (str): sponsor text
            logo (str): sponsor logo
        Returns:
            MatchModel: new match
        """
        query = f"INSERT INTO  {cls.tableName} (sponsorName, sponsorText, sponsorLink, logo) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (sponsorName, sponsorText, sponsorLink, logo))
        return cls(sponsorId=cursor.lastrowid , sponsorName=sponsorName, sponsorText = sponsorText, sponsorLink = sponsorLink, logo = logo)

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        return {
            "sponsorId": self.sponsorId,
            "sponsorName": self.sponsorName,
            "sponsorText": self.sponsorText,
            "sponsorLink": self.sponsorLink,
            "logo": self.logo
        }


    def __str__(self):
        return json.dumps(self.toDict())
