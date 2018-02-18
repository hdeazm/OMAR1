import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    
    def GET(self, id_docente):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_docente) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                return self.GET_VIEW(id_docente) # call GET_VIEW() function
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_docente):
        id_docente = config.check_secure_val(str(id_docente)) # HMAC id_docente validate
        result = config.model.get_docentes(id_docente) # search for the id_docente data
        return config.render.view(result) # render view.html with id_docente data
