import cherrypy
import jinja2
import json
import jinja2plugin
import jinja2tool
import os.path
from cherrypy.lib.static import serve_file

class WebApp():

    #Web application of the MangezDuClown (MDC) application
    def __init__ (self):
        self.jokes = self.loadjokes()
        #User's pseudo by default
        self.__pseudo = "monsieur anonyme"
    
    #function loading database from the'database.json' file
    def loadjokes(self):
        try:
            with open('database.json', 'r', encoding='utf-8') as file:
                content = json.loads(file.read())
                return content['jokes']
        #Admin can catch a possible error to resolve it
        #User can see a better interface then '404 error'
        except Exception as e:
            cherrypy.log('erreur de chargement.')
            print(e)
            return []
    
    #Save the new joke in the 'database.json' file.
    def savejokes(self):
        try:
            with open('database.json', 'w', encoding='utf-8') as file:
                file.write(json.dumps({
                    'jokes': self.jokes
                }, ensure_ascii=False))
        except:
            cherrypy.log('erreur de sauvegarde.')
    
    @cherrypy.expose
    def index (self):
        #Main page of the MDC's application.
        if len(self.jokes) == 0:
            jokes = '''<p> Il n'y a aucune blagues dans notre base de données, 
                    ajoutez en et faites nous rire! </p>'''
        else :
            jokes = '<ul>'
            for e in range (len(self.jokes)):
                joke = self.jokes[e]
                jokes += '''<li>
                    <h2>
                        <b>{}</b>
                    </h2>
                    <h3>
                        ({} votes <a href="addvote?i={}">+1</a>, 
                        Catégorie: {}, auteur : {})
                    </h3>
                    </br>
                    {}</br>
                </li></br>'''.format(joke['title'],joke['votes'], e,joke['Categorie'],joke['auteur'], joke['contenu'])
            jokes += '</ul>'
        return {"jokes": jokes, "pseudo": self.__pseudo}

    #Page which the user can log in.
    @cherrypy.expose
    def loginform(self):
        return {}
    
    #Post route to log in, The identity of the user is now known.
    @cherrypy.expose
    def login(self, pseudo):
        self.__pseudo = pseudo
        raise cherrypy.HTTPRedirect('/')
    
    #Page with a form to add a new joke.
    @cherrypy.expose
    def add(self):
        return {}
    
    #Post route to add a new joke in the database.
    @cherrypy.expose
    def addjoke(self, title, contenu, Categorie):
        if title != '' and contenu != '' :
            self.jokes.append({'title':title, 'contenu':contenu, 'Categorie':Categorie, 'votes':1,'auteur': self.__pseudo })
            self.savejokes()
        raise cherrypy.HTTPRedirect('/')
    
    
    #This is a route to add a new vote for a given joke.
    @cherrypy.expose
    def addvote(self, i):
        try:
            self.jokes[int(i)]['votes'] += 1
            self.savejokes()
        except:
            pass
        raise cherrypy.HTTPRedirect('/')
    
    #Page showing all the joke with some 'Humour noir'.
    @cherrypy.expose
    def Humnoir(self):
        Humn = '<ul>'
        for i in self.jokes:
            if i['Categorie'] == 'Humour noir':
                Hum = i 
                Humn += '''<li>
                    <h2>
                        <b>{}</b>
                    </h2>
                    <h3>
                        ({} votes <a href="addvote?i={}">+1</a>, 
                        Catégorie: {}, auteur: {})
                    </h3>
                    </br>
                    {}</br>
                </li></br>'''.format(Hum['title'],Hum['votes'], i,Hum['Categorie'], Hum['auteur'], Hum['contenu'])
        Humn += '</ul>'
        return {"Humn": Humn}
    
    #Page showing all stupid joke.
    @cherrypy.expose
    def Carambar(self):
        Cara = '<ul>'
        for i in self.jokes:
            if i['Categorie'] == 'Carambar':
                Car = i 
                Cara += '''<li>
                    <h2>
                        <b>{}</b>
                    </h2>
                    <h3>
                        ({} votes <a href="addvote?i={}">+1</a>, Catégorie: {}, auteur: {})
                    </h3></br>
                    {}</br>
                </li></br>'''.format(Car['title'],Car['votes'], i,Car['Categorie'],Car['auteur'], Car['contenu'])
        Cara += '</ul>'
        #Carapils is for beer, what carambar is for joke.
        #Not the best, but you will still be happy as you get it.
        return {"Cara": Cara} # ==> You just win a Cara ! Congrats !
    
    #Page showing all joke without main Category.
    @cherrypy.expose
    def Unk(self):
        Un = '<ul>'
        for i in self.jokes:
            if i['Categorie'] == 'Inconnue':
                u = i 
                Un += '''<li>
                    <h2>
                        <b>{}</b>
                    </h2>
                    <h3>
                        ({} votes <a href="addvote?i={}">+1</a>, Catégorie: {}, auteur: {})
                    </h3></br>
                    {}</br>
                </li></br>'''.format(u['title'], u['votes'], i,u['Categorie'], u['auteur'], u['contenu'],)
        Un += '</ul>'
        return {"Un": Un}
    
    @cherrypy.expose
    def getjokes(self):
        #GET route to get all jokes
        return json.dumps({
            'jokes': self.jokes
        }, ensure_ascii=False).encode('utf-8')

if __name__ == '__main__':
    #Register Jinja2 plugin and tool.
    ENV = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    jinja2plugin.Jinja2TemplatePlugin(cherrypy.engine, env=ENV).subscribe()
    cherrypy.tools.template = jinja2tool.Jinja2Tool()
    #Launch web server.
    cherrypy.quickstart(WebApp(), '', 'serv.conf')