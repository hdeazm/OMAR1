import web
import config
import json


class Api_alumnos:
    def get(self, id_alumno):
        try:
            # http://0.0.0.0:8080/api_alumnos?user_hash=12345&action=get
            if id_alumno is None:
                result = config.model.get_all_alumnos()
                alumnos_json = []
                for row in result:
                    tmp = dict(row)
                    alumnos_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(alumnos_json)
            else:
                # http://0.0.0.0:8080/api_alumnos?user_hash=12345&action=get&id_alumno=1
                result = config.model.get_alumnos(int(id_alumno))
                alumnos_json = []
                alumnos_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(alumnos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            alumnos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(alumnos_json)

# http://0.0.0.0:8080/api_alumnos?user_hash=12345&action=put&id_alumno=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,telefono_alum,telefono_tutor,direccion):
        try:
            config.model.insert_alumnos(nombre,telefono_alum,telefono_tutor,direccion)
            alumnos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(alumnos_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_alumnos?user_hash=12345&action=delete&id_alumno=1
    def delete(self, id_alumno):
        try:
            config.model.delete_alumnos(id_alumno)
            alumnos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(alumnos_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_alumnos?user_hash=12345&action=update&id_alumno=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_alumno, nombre,telefono_alum,telefono_tutor,direccion):
        try:
            config.model.edit_alumnos(id_alumno,nombre,telefono_alum,telefono_tutor,direccion)
            alumnos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(alumnos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            alumnos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(alumnos_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_alumno=None,
            nombre=None,
            telefono_alum=None,
            telefono_tutor=None,
            direccion=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_alumno=user_data.id_alumno
            nombre=user_data.nombre
            telefono_alum=user_data.telefono_alum
            telefono_tutor=user_data.telefono_tutor
            direccion=user_data.direccion
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_alumno)
                elif action == 'put':
                    return self.put(nombre,telefono_alum,telefono_tutor,direccion)
                elif action == 'delete':
                    return self.delete(id_alumno)
                elif action == 'update':
                    return self.update(id_alumno, nombre,telefono_alum,telefono_tutor,direccion)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
