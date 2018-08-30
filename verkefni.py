from sys import argv

import bottle
from bottle import *

bottle.debug(True)

@route('/')
def index():
       return """
        <h2>Verkefni 1 a og b</h2>        
        <p><a href="http://localhost:8800/">Home</a></p>
        <p><a href="http://localhost:8800/about">About</a></p>
        <p><a href="http://localhost:8800/biography">Biography</a></p>
        <p><a href="http://localhost:8800/pitures">Pitures</a></p>
        <h3>Þetta hérna fyrir neðan er a hluti</h1>
        <p><a href="http://localhost:8800/hello">Hello</a></p>
        
        <h3>Þetta er Home Síðan</h3>    
       
       """

@route('/about')
def about():
      return """
        <h2>Verkefni 1 a og b</h2>        
        <p><a href="http://localhost:8800/">Home</a></p>
        <p><a href="http://localhost:8800/about">About</a></p>
        <p><a href="http://localhost:8800/biography">Biography</a></p>
        <p><a href="http://localhost:8800/pitures">Pitures</a></p>
        <p><a href="http://localhost:8800/hello">Hello</a></p>
        
        <h3>Þetta er About Síðan</h3>    
       
       """


@route('/biography')
def about():
          return """
        <h2>Verkefni 1 a og b</h2>        
        <p><a href="http://localhost:8800/">Home</a></p>
        <p><a href="http://localhost:8800/about">About</a></p>
        <p><a href="http://localhost:8800/biography">Biography</a></p>
        <p><a href="http://localhost:8800/pitures">Pitures</a></p>
        <p><a href="http://localhost:8800/hello">Hello</a></p>
        
        <h3>Þetta er Biography Síðan</h3>    
       
       """



@route('/pitures')
def about():
      return """
        <h2>Verkefni 1 a og b</h2>        
        <p><a href="http://localhost:8800/">Home</a></p>
        <p><a href="http://localhost:8800/about">About</a></p>
        <p><a href="http://localhost:8800/biography">Biography</a></p>
        <p><a href="http://localhost:8800/pitures">Pitures</a></p>
        <p><a href="http://localhost:8800/hello">Hello</a></p>
        
        <h3>Þetta er Pitures Síðan</h3>    
       
       """

@route('/hello')
def hello():
        return """
        <h2>Verkefni 1 a og b</h2>        
        <p><a href="http://localhost:8800/">Home</a></p>
        <p><a href="http://localhost:8800/about">About</a></p>
        <p><a href="http://localhost:8800/biography">Biography</a></p>
        <p><a href="http://localhost:8800/pitures">Pitures</a></p>
        <p><a href="http://localhost:8800/hello">Hello</a></p>
        
        <h3>Halló Heimur</h3>    
       
       """



#run(host='localhost', port=8800)

bottle.run(host='0.0.0.0', port=argv[1])
