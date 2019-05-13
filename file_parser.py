import javalang
import config
import os

def get_enum_doc(repo, path, response, type, imports, package):
    enum_doc = {
        "id": repo["id"],
        "owner": repo["owner"]["login"],
        "created_at": repo["created_at"],
        "description": repo["description"],
        "repository_name": repo["name"],
        "html_url": repo["html_url"],
        "open_issues_count": repo["open_issues_count"],
        "pushed_at": repo["pushed_at"],
        "stargazers_count": repo["stargazers_count"],
        "file_name": os.path.basename(path),
        "words": response,
        "enum_name": type.name,
        "access_modifier": get_access_modifier(type.modifiers),
        "constants": get_constants(type.body.constants),
        "implements_interfaces": get_references(type.implements),
        "annotation": get_annotations(type.annotations),
        "position": {
            "line": type._position.line,
            "column": type._position.column
        }
    }
    if imports is not None:
        enum_doc['imports'] = get_imports(imports)
    if package is not None:
        enum_doc['package'] = package.name
    return enum_doc
def get_interface_doc(repo, path, response, type, imports, package):
    interface_doc = {
        "id": repo["id"],
        "owner": repo["owner"]["login"],
        "created_at": repo["created_at"],
        "description": repo["description"],
        "repository_name": repo["name"],
        "html_url": repo["html_url"],
        "open_issues_count": repo["open_issues_count"],
        "pushed_at": repo["pushed_at"],
        "stargazers_count": repo["stargazers_count"],
        "file_name": os.path.basename(path),
        "words": response,
        "interface_name": type.name,
        "access_modifier": get_access_modifier(type.modifiers),
        "implements_interfaces": get_references(type.extends),
        "position": {
            "line": type._position.line,
            "column": type._position.column
        },
        "type_parameters": get_type_parameters(type.type_parameters),
        "annotation": get_annotations(type.annotations)
    }
    if imports is not None:
        interface_doc['imports'] = get_imports(imports)
    if package is not None:
        interface_doc['package'] = package.name
    return interface_doc
def get_class_doc(repo, path, response, type, imports, package):
    class_doc = {
            "id": repo["id"],
            "owner": repo["owner"]["login"],
            "created_at": repo["created_at"],
            "description": repo["description"],
            "repository_name": repo["name"],
            "html_url": repo["html_url"],
            "open_issues_count": repo["open_issues_count"],
            "pushed_at": repo["pushed_at"],
            "stargazers_count": repo["stargazers_count"],
            "file_name": os.path.basename(path),
            "words": response,
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
        class_doc['package'] = package.name
    return class_doc
def get_method_doc(repo, path, response, type, analysed_code):
    current_function_index = -1
    for function_index in range(len(analysed_code.__dict__['function_list'])):
        method_name = analysed_code.function_list[function_index].__dict__['name']
        if '::' in method_name:
            method_name = method_name.split('::')[1]
        if method_name == type.name:
            current_function_index = function_index
            break
    # if 'abstract' not in type.modifiers and current_function_index == -1:
    #     for function_index in range(len(analysed_code.__dict__['function_list'])):
    #         print(analysed_code.function_list[function_index].__dict__['name'])
    #     raise Exception('Error - no such function exists. Lizard found {}, javalang found {}.'.format(analysed_code.__dict__['function_list'], type.name))

    method_doc = {
            "id": repo["id"],
            "owner": repo["owner"]["login"],
            "created_at": repo["created_at"],
            "description": repo["description"],
            "repository_name": repo["name"],
            "html_url": repo["html_url"],
            "open_issues_count": repo["open_issues_count"],
            "pushed_at": repo["pushed_at"],
            "stargazers_count": repo["stargazers_count"],
            "file_name": os.path.basename(path),
            "words": response,
            "method_name": type.name,
            "access_modifier": get_access_modifier(type.modifiers),
            "is_abstract": 'abstract' in type.modifiers,
            "is_static": 'static' in type.modifiers,
            "is_final": 'final' in type.modifiers,
            "input_type": get_parameter_types(type.parameters),
            "annotation": get_annotations(type.annotations),
            "type_parameters": get_type_parameters(type.type_parameters),
            "position": {
                "line": type._position.line,
                "column": type._position.column
            }
    }
    # If the method couldn't be analyzed we don't incluce any information on these parameters
    if current_function_index != -1:
        method_doc['cyclomatic_complexity'] = analysed_code.function_list[current_function_index].__dict__['cyclomatic_complexity']
        method_doc['token_count'] = analysed_code.function_list[current_function_index].__dict__['token_count']
        method_doc['parameter_count'] = len(analysed_code.function_list[current_function_index].__dict__['parameters'])
    if type.throws is not None:
        method_doc['throws'] = type.throws
    if type.return_type is not None:
        method_doc['return_type'] = get_annotations([type.return_type])
    return method_doc
def get_variable_doc(repo, path, response, type):
    variable_doc = {
        "id": repo["id"],
        "owner": repo["owner"]["login"],
        "created_at": repo["created_at"],
        "description": repo["description"],
        "repository_name": repo["name"],
        "html_url": repo["html_url"],
        "open_issues_count": repo["open_issues_count"],
        "pushed_at": repo["pushed_at"],
        "stargazers_count": repo["stargazers_count"],
        "file_name": os.path.basename(path),
        "words": response,
        "variable_name": get_variable_names(type.declarators),
        "variable_type": get_references([type.type]),
        "annotation": get_annotations(type.annotations),
        "access_modifier": get_access_modifier(type.modifiers),
        "is_static": 'static' in type.modifiers,
        "is_final": 'final' in type.modifiers,
        "position": {
            "line": type._position.line,
            "column": type._position.column
        }
    }
    return variable_doc

def parse_data(data, repo, path, analysed_code):
    tree = javalang.parse.parse(data)
    docs = []
    if isinstance(tree, javalang.tree.CompilationUnit):
        for type in tree.types:
            if isinstance(type, javalang.tree.ClassDeclaration):
                class_doc = (config.class_index, get_class_doc(repo, path, data, type, tree.imports, tree.package))
                docs.append(class_doc)
                for method in type.methods:
                    method_doc = (config.method_index, get_method_doc(repo, path, data, method, analysed_code))
                    docs.append(method_doc)
                for field in type.fields:
                    variable_doc = (config.variable_index, get_variable_doc(repo, path, data, field))
                    docs.append(variable_doc)
            elif isinstance(type, javalang.tree.InterfaceDeclaration):
                interface_doc = (config.interface_index, get_interface_doc(repo, path, data, type, tree.imports, tree.package))
                docs.append(interface_doc)
                for method in type.methods:
                    method_doc = (config.method_index, get_method_doc(repo, path, data, method, analysed_code))
                    docs.append(method_doc)
                for field in type.fields:
                    variable_doc = (config.variable_index, get_variable_doc(repo, path, data, field))
                    docs.append(variable_doc)
            elif isinstance(type, javalang.tree.EnumDeclaration):
                enum_doc = (config.enum_index, get_enum_doc(repo, path, data, type, tree.imports, tree.package))
                docs.append(enum_doc)
                for method in type.methods:
                    method_doc = (config.method_index, get_method_doc(repo, path, data, method, analysed_code))
                    docs.append(method_doc)
                for field in type.fields:
                    variable_doc = (config.variable_index, get_variable_doc(repo, path, data, field))
                    docs.append(variable_doc)
    return docs

def get_references(references):
    references_list = []
    if references is not None:
        for reference in references:
            if isinstance(reference, javalang.tree.BasicType):
                references_list.append(reference.name)
            elif isinstance(reference, javalang.tree.TypeArgument):
                references_list.append(reference.type)
            else:
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

def get_constants(constants):
    constants_list = []
    for constant in constants:
        if isinstance(constant, javalang.tree.EnumConstantDeclaration):
            constants_list.append(constant.name)
    return constants_list

def get_parameter_types(parameters):
    parameters_types = []
    for parameter in parameters:
        parameters_types.append(get_references([parameter.type])[0])
    return parameters_types

def get_variable_names(names):
    names_list = []
    for name in names:
        if isinstance(name, javalang.tree.VariableDeclarator):
            names_list.append(name.name)
    return names_list

# with open('Test.java', 'r', encoding='utf_8') as file:
#     data = file.read()
#     tree = javalang.parse.parse(data)
#     docs = parse_data(data, 'url', None)
#     print(docs)
