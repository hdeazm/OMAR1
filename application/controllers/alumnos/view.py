import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    
    def GET(self, id_alumno):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_alumno) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                return self.GET_VIEW(id_alumno) # call GET_VIEW() function
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_alumno):
        id_alumno = config.check_secure_val(str(id_alumno)) # HMAC id_alumno validate
        result = config.model.get_alumnos(id_alumno) # search for the id_alumno data
        return config.render.view(result) # render view.html with id_alumno data
