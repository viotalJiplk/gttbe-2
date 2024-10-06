from .file import File, FileList

fileRoutes = [(FileList, '/list'), (File, '/<fileName>')]
