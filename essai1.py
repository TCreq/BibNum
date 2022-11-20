#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

import copy #Pour copier différentes listes ou objets
import PyPDF2
import epub as e2
import ebooklib
from ebooklib import epub

book=e2.open_epub('stendhal_-_le_rouge_et_le_noir.epub')

for item in book.opf.manifest.values():
  # read the content
  data = book.read_item(item)
  #print(data)

t=book.toc
print("toc=",t)
print("toc.nav_map=",t.nav_map)
#print("toc.nav_map.nav_point=",t.nav_map.nav_point)
for i in t.nav_map.nav_point:
  print("nav_point.labels[0][0]=",i.labels[0][0])
  #print("nav_point.nav_point=",i.nav_point)
  #print("nav_point.src=",i.src)
print("toc.page_list=",t.page_list)
print("toc.page_list.infos=",t.page_list.infos)
xmlfile=book.toc.as_xml_document()

print(book.opf)

for item_id, linear in book.opf.spine.itemrefs:
  item = book.get_item(item_id)
  # Check if linear or not
  if linear:
    #print('Linear item "%s"' % item.href)
    pass
  else:
    #print('Non-linear item "%s"' % item.href)
    # read the content
    data = book.read_item(item)
    pass

###----------------------------------------------------------------------

book=epub.read_epub('stendhal_-_le_rouge_et_le_noir.epub')
print(book.get_metadata('DC', 'title')[0][0])
#[('Ratio', {})]
print(book.get_metadata('DC', 'creator')[0][0])
#[('Firstname Lastname ', {})]
print(book.get_metadata('DC', 'language')[0][0])


#cover_image = book.get_item_with_id('cover-image')
#print(cover_image) #None
#index = book.get_item_with_href('index.xhtml')
#print(index) #None

#print(book.metadata)

###-----------------------------------------------------------------------

book=e2.open_epub('stendhal_-_le_rouge_et_le_noir.epub')

t=book.toc.as_xml_document()
print(t)



###------------------------------------------------------------------------

import xml.dom.minidom

document = """\
<slideshow>
<title>Demo slideshow</title>
<slide><title>Slide title</title>
<point>This is a demo</point>
<point>Of a program for processing slides</point>
</slide>

<slide><title>Another demo slide</title>
<point>It is important</point>
<point>To have more than</point>
<point>one slide</point>
</slide>
</slideshow>
"""

"""
dom = xml.dom.minidom.parseString(document)

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def handleSlideshow(slideshow):
    print("<html>")
    handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
    slides = slideshow.getElementsByTagName("slide")
    handleToc(slides)
    handleSlides(slides)
    print("</html>")

def handleSlides(slides):
    for slide in slides:
        handleSlide(slide)

def handleSlide(slide):
    handleSlideTitle(slide.getElementsByTagName("title")[0])
    handlePoints(slide.getElementsByTagName("point"))

def handleSlideshowTitle(title):
    print(f"<title>{getText(title.childNodes)}</title>")

def handleSlideTitle(title):
    print(f"<h2>{getText(title.childNodes)}</h2>")

def handlePoints(points):
    print("<ul>")
    for point in points:
        handlePoint(point)
    print("</ul>")

def handlePoint(point):
    print(f"<li>{getText(point.childNodes)}</li>")

def handleToc(slides):
    for slide in slides:
        title = slide.getElementsByTagName("title")[0]
        print(f"<p>{getText(title.childNodes)}</p>")

print(dom)
handleSlideshow(dom)
"""
