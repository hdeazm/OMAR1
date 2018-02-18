import web
import config
import json


class Api_docentes:
    def get(self, id_docente):
        try:
            # http://0.0.0.0:8080/api_docentes?user_hash=12345&action=get
            if id_docente is None:
                result = config.model.get_all_docentes()
                docentes_json = []
                for row in result:
                    tmp = dict(row)
                    docentes_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(docentes_json)
            else:
                # http://0.0.0.0:8080/api_docentes?user_hash=12345&action=get&id_docente=1
                result = config.model.get_docentes(int(id_docente))
                docentes_json = []
                docentes_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(docentes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            docentes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(docentes_json)

# http://0.0.0.0:8080/api_docentes?user_hash=12345&action=put&id_docente=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,telefono,direccion):
        try:
            config.model.insert_docentes(nombre,telefono,direccion)
            docentes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(docentes_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_docentes?user_hash=12345&action=delete&id_docente=1
    def delete(self, id_docente):
        try:
            config.model.delete_docentes(id_docente)
            docentes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(docentes_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_docentes?user_hash=12345&action=update&id_docente=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_docente, nombre,telefono,direccion):
        try:
            config.model.edit_docentes(id_docente,nombre,telefono,direccion)
            docentes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(docentes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            docentes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(docentes_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_docente=None,
            nombre=None,
            telefono=None,
            direccion=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_docente=user_data.id_docente
            nombre=user_data.nombre
            telefono=user_data.telefono
            direccion=user_data.direccion
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_docente)
                elif action == 'put':
                    return self.put(nombre,telefono,direccion)
                elif action == 'delete':
                    return self.delete(id_docente)
                elif action == 'update':
                    return self.update(id_docente, nombre,telefono,direccion)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
