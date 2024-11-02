from flask_restx import Resource
from flask import send_file, request
from shared.utils import config, perms
from os import listdir, remove, path
from re import fullmatch
from utils import errorList, hasPermissionDecorator, returnError

def filenameParser(fileName: str):
    return fullmatch(r'^[A-Za-z0-9][A-Za-z0-9\.]+$', fileName)

class File(Resource):
    @hasPermissionDecorator([perms.file.read], False)
    @returnError([errorList.file.wrongFileName, errorList.file.missingPermission])
    def get(self, fileName, authResult, permissions):
        if not filenameParser(fileName):
            raise errorList.file.wrongFileName
        try:
            return send_file(path.join(config.dynamicFileFolder, fileName))
        except FileNotFoundError:
            raise errorList.file.fileDoesNotExist

    @hasPermissionDecorator([perms.file.upload], False)
    @returnError([errorList.file.wrongFileName])
    def put(self, fileName, authResult, permissions):
        if not filenameParser(fileName):
            raise errorList.file.wrongFileName
        file = request.get_data()
        with open(path.join(config.dynamicFileFolder, fileName), 'wb') as f:
            f.write(file)
        return {
                "fileName": fileName,
                "address": f"/file/{fileName}"
            }
    @hasPermissionDecorator([perms.file.delete], False)
    @returnError([errorList.file.wrongFileName, errorList.file.missingPermission])
    def delete(self, fileName, authResult, permissions):
        if not filenameParser(fileName):
            raise errorList.file.wrongFileName
        try:
            remove(path.join(config.dynamicFileFolder, fileName))
            return 200
        except FileNotFoundError:
            raise errorList.file.fileDoesNotExist
        except PermissionError:
            raise errorList.file.missingPermission


class FileList(Resource):
    @hasPermissionDecorator([perms.file.listFiles], False)
    def get(self, authResult, permissions):
        fileList = listdir(config.dynamicFileFolder)
        result = []
        for file in fileList:
            result.append({
                "fileName": file,
                "address": f"/file/{file}"
            })
        return result
