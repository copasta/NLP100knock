
import re
import pydot_ng as pydot
from lxml import etree, objectify

def graph_4_edge(edges, gr_type='graph'):
    graph = pydot.Dot(graph_type=gr_type)
    for edge in edges:
        id1 = str(edge[0][0])
        label1 = str(edge[0][1])
        id2 = str(edge[1][0])
        label2 = str(edge[1][1])

        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        graph.add_edge(pydot.Edge(id1, id2))

    return graph

tree = etree.parse("nlp.txt.xml")
root = tree.getroot()
document = root.find('document')
sentences = document.find('sentences')

for sentence in sentences:
    edges = []
    sent_id = sentence.get('id')

    
    for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
        if dep.get('type') != 'punct':
            govr = dep.find('./governor')
            dept = dep.find('./dependent')
            edges.append(
                ((govr.get('idx'), govr.text), (dept.get('idx'), dept.text))
            )
    if len(edges) > 0:
        graph = graph_4_edge(edges, gr_type='digraph')
        graph.write_png('./result/{}.png'.format(sent_id))