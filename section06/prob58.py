from lxml import etree, objectify

def get_tuple(dependant):
    dict_pred = {}
    dict_nsubj = {}
    dict_dobj = {}
    for dep in dependant.findall('dep'):
        if dep.get('type') == 'nsubj' or dep.get('type') == 'dobj':
            gove = dep.find('./governor')
            idx = gove.get('idx')
            dict_pred[idx] = gove.text

            if dep.get('type') == 'nsubj':
                dict_nsubj[idx] = dep.find('./dependent').text
            elif dep.get('type') == 'dobj':
                dict_dobj[idx] = dep.find('./dependent').text
    for idx, pred in sorted(dict_pred.items(), key=lambda x: x[0]):
        nsubj = dict_nsubj.get(idx)
        dobj = dict_dobj.get(idx)
        if nsubj is not None and dobj is not None:
            print('{}\t{}\t{}'.format(nsubj, pred, dobj))

if __name__ == "__main__":
    tree = etree.parse("nlp.txt.xml")
    root = tree.getroot()
    documents = root.find('document')
    sentences = documents.find("sentences")
    
    for sentence in sentences:
        dependents = sentence.xpath('//dependencies[@type="collapsed-dependencies"]')
        for dependent in dependents:
            get_tuple(dependent)
