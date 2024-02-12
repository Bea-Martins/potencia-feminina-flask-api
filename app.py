from flask import Flask, render_template
import urllib.request, json
import ssl

# desativa verificacao do certificado SSL
ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)

@app.route('/')
def get_list_elements_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("characters.html", characters=dict['results'])

@app.route('/profile/<id>')
def get_profile(id):
  url = "https://rickandmortyapi.com/api/character" + id
  response = urllib.request.urlopen(url)
  data = response.read()
  dict = json.loads(data)

  return render_template("profile.html", profile=dict)

# rota e função
@app.route('/lista')
def get_list_elements():
  url = "https://rickandmortyapi.com/api/character"
  response = urllib.request.urlopen(url)
  characters = response.read()
  dict = json.loads(characters)

  characters_list = []

  for character in dict["results"]:
    character_data = {
      "name": character["name"],
      "status": character["status"]
    }
    characters_list.append(character_data)

  return {"characters": characters_list}