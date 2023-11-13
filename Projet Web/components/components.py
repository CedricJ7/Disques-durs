from browser import ajax
from browser import html
from browser import DOMNode
from browser import document
from browser import webcomponent
from browser.template import Template

# Some d4rk magic, don't touch it!
def defineCustomElements(tagname, path, tagtype = None):

	if tagtype == None:
		tagtype = DOMNode

	name = path.replace('.', '_').replace('/', '_');
	
	def read_css(req):
	
		if req.status == 404 :
			return

		style = html.STYLE(f'{tagname} {{ {req.text} }}')
		document.head <= style
		

	def read_html(req):
		TEMPLATE = html.TEMPLATE(req.text)

		def init(this):
			content = TEMPLATE.clone().content
			
			h4ck = html.DIV() if tagtype == DOMNode else tagtype()
			h4ck <= content

			elem = None

			if tagtype in [html.TD, html.TR, html.TBODY, html.TFOOT, html.THEAD]:

				cur_elem = h4ck
				tag = tagtype
				if tag == html.TD:
					tag = html.TR
					cur_elem = tag( cur_elem )
					if elem == None:
						elem = cur_elem
				if tag == html.TR:
					tag = html.TBODY
					cur_elem = tag( cur_elem )
					if elem == None:
						elem = cur_elem

				cur_elem = html.TABLE( cur_elem )
				if elem == None:
					elem = cur_elem
			else:
				elem = html.DIV( h4ck )
			
			parameters = {k[5:] : v for k, v in this.attrs.items() if k.startswith("data-")}
			Template(h4ck).render(**parameters)
			
			children = elem.children[0].childNodes

			this <= children

		Class = type(name, (tagtype,), {
			'__init__': init
		})
		webcomponent.define(tagname, Class)

	ajax.get(path +"/index.css" , oncomplete=read_css)
	ajax.get(path +"/index.html", oncomplete=read_html)


print(dir(DOMNode))