import cherrypy
class index(object):
    @cherrypy.expose
    def example(self):
        var = "goodbye"
        index = open("index.html").read()
        return index

.box{
    display: none;
    width: 100%;
}

a:hover + .box,.box:hover{
    display: block;
    position: relative;
    z-index: 100;
}
This live preview for <a href="https://en.wikipedia.org/">Wikipedia</a>
  <div class="box">
    <iframe src="https://en.wikipedia.org/" width = "500px" height = "500px">
    </iframe>
  </div> .box{
    display: none;
    width: 100%;
}

a:hover + .box,.box:hover{
    display: block;
    position: relative;
    z-index: 100;
}
This live preview for <a href="https://en.wikipedia.org/">Wikipedia</a>
  <div class="box">
    <iframe src="https://en.wikipedia.org/" width = "500px" height = "500px">
    </iframe>
  </div> 
remains open on mouseover