from routes.page.get import Page
from flask_restx import Resource

pageRoutes = [(Page, "/<name>/", )]
