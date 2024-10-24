from .sponsors import Sponsors, SponsorCreate
from flask_restx import Resource

sponsorRoutes = [(Sponsors, '/<sponsorId>/'), (SponsorCreate, '/create')]
