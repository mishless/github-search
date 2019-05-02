import javalang
import config

def get_class_doc(url, type, imports, package):
    class_doc = {
            "url": url,
            "class_name": type.name,
            "type_parameters": get_type_parameters(type.type_parameters),
            "access_modifier": get_access_modifier(type.modifiers),
            "is_abstract": 'abstract' in type.modifiers,
            "is_static": 'static' in type.modifiers,
            "is_final": 'final' in type.modifiers,
            "annotation": get_annotations(type.annotations),
            "extends_class": get_references([type.extends]),
            "implements_interfaces": get_references(type.implements),
            "position": {
                "line": type._position.line,
                "column": type._position.column
            }
    }
    if imports is not None:
        class_doc['imports'] = get_imports(imports)
    if package is not None:
        class_doc['name'] = package.name
    return class_doc

def parse_data(data, url):
    tree = javalang.parse.parse(data)
    docs = []
    if isinstance(tree, javalang.tree.CompilationUnit):
        for type in tree.types:
            if isinstance(type, javalang.tree.ClassDeclaration):
                class_doc = (config.class_index, get_class_doc(url, type, tree.imports, tree.package))
                docs.append(class_doc)
    return docs

def get_references(references):
    references_list = []
    if references is not None:
        for reference in references:
            reference_el = ''
            while (reference is not None):
                reference_el += reference.name + '.'
                reference = reference.sub_type
            references_list.append(reference_el[:-1])
    return references_list

def get_imports(imports):
    imports_list = []
    if imports is not [] and imports is not None:
        for import_el in imports:
            if import_el.wildcard:
                imports_list.append(import_el.path + '.*')
            else:
                imports_list.append(import_el.path)
    return imports_list

def get_type_parameters(type_parameters):
    type_parameters_list = []
    if type_parameters is not None:
        for type_parameter in type_parameters:
            extends = []
            if type_parameter.extends is not None:
                extends = get_references(type_parameter.extends)
            type_parameters_list.append({'extends': extends, 'name': type_parameter.name})
    return type_parameters_list

def get_annotations(annotations):
    annotations_list = []
    if annotations is not None:
        for annotation in annotations:
            annotations_list.append(annotation.name)
    return annotations_list

def get_access_modifier(modifier):
    if 'public' in modifier:
        return 'public'
    if 'protected' in modifier:
        return 'protected'
    if 'private' in modifier:
        return 'private'
