% rebase('base.tpl')
<div id='container'>
  <div id="nav-custom">
    <ul class="nav nav-pills mb-3 nav-fill navbar-dark" id="pills-tab" role="tablist">
      <li class="nav-item">
        <a class="nav-link {{'active' if index=='code' else ''}}" id="pills-home-tab" data-toggle="pill" href="#code" role="tab" aria-controls="pills-home" aria-selected="true">Code</a>
      </li>
      <li class="nav-item">
        <a class="nav-link {{'active' if index=='class' else ''}}" id="pills-home-tab" data-toggle="pill" href="#class" role="tab" aria-controls="pills-home" aria-selected="true">Class</a>
      </li>
      <li class="nav-item">
        <a class="nav-link {{'active' if index=='interface' else ''}}" id="pills-profile-tab" data-toggle="pill" href="#interface" role="tab" aria-controls="pills-profile" aria-selected="false">Interface</a>
      </li>
      <li class="nav-item">
        <a class="nav-link {{'active' if index=='enum' else ''}}" id="pills-contact-tab" data-toggle="pill" href="#enum" role="tab" aria-controls="pills-contact" aria-selected="false">Enum</a>
      </li>
      <li class="nav-item">
        <a class="nav-link {{'active' if index=='method' else ''}}" id="pills-contact-tab" data-toggle="pill" href="#method" role="tab" aria-controls="pills-contact" aria-selected="false">Method</a>
      </li>
      <li class="nav-item">
        <a class="nav-link {{'active' if index=='variable' else ''}}" id="pills-contact-tab" data-toggle="pill" href="#variable" role="tab" aria-controls="pills-contact" aria-selected="false">Variable</a>
      </li>
    </ul>
  </div>
  <div class="tab-content" id="pills-tabContent">
    <div class="tab-pane fade {{'show active' if index=='code' else ''}}" id="code" role="tabpanel" aria-labelledby="pills-home-tab">
      <div id="search-form">
        <form  id="code-property-search-form" action="/search" class="property-search-form" method="get" onsubmit="return copyQuery()">
          <div class="form-group row text-search">
            <div id="searchbox" class="col-sm-10" placeholder="Search for code here" contenteditable="true" spellcheck="false" innerText="{{query}}"></div>
            <input type="textarea" id="hiddenquery" name="query" hidden>
            <input type="textarea" class="page" name="page" hidden value=1>
            <button id="button-submit" class="col-sm-1" type="submit" value=""><i class="fas fa-search"></i></button>
          </div>
          <label class="col-sm-1 col-form-label float-left">Sort</label>
          <select class="form-control col-sm-3 float-left" name="sort">
              <option value='stargazers_count:asc' {{'selected' if sort=='stargazers_count:asc' else ''}}>Stars (ascending)</option>
              <option value='stargazers_count:desc' {{'selected' if sort=='stargazers_count:desc' else ''}}>Stars (descending)</option>
              <option value='created_at:asc' {{'selected' if sort=='created_at:asc' else ''}}>Created at (ascending)</option>
              <option value='created_at:desc' {{'selected' if sort=='created_at:desc' else ''}}>Created at (descending)</option>
              <option value='open_issues_count:asc' {{'selected' if sort=='open_issues_count:asc' else ''}}>Open issues (ascending)</option>
              <option value='open_issues_count:desc' {{'selected' if sort=='open_issues_count:desc' else ''}}>Open issues (descending)</option>
              <option value='pushed_at:asc' {{'selected' if sort=='pushed_at:asc' else ''}}>Last commit (ascending)</option>
              <option value='pushed_at:desc' {{'selected' if sort=='pushed_at:desc' else ''}}>Last commit (descending)</option>
          </select>
        </form>
      </div>
    </div>
    <div class="tab-pane fade {{'show active' if index=='class' else ''}}" id="class" role="tabpanel" aria-labelledby="pills-profile-tab">
      <div id="search-form">
        <form id="class-property-search-form" class="property-search-form" action="/search-class-properties" method="get" onsubmit="return createQuery(this, 'class')">
          <fieldset>
            <legend>Query</legend>
          <div id="class-fields">
            <div id="class-properties" class="original-properties form-group row">
              <div class="boolean-property col-sm-2">
                <select class="form-control boolean_property">
                    <option>and</option>
                    <option>or</option>
                </select>
              </div>
              <label class="col-sm-2 col-form-label">Property</label>
              <div class="col-sm-3">
                <select class="form-control class_property">
                      <option value='class_name' {{'selected' if queries is not None and queries[0][1]=='class_name' else ''}}>Class name</option>
                      <option value='access_modifier' {{'selected' if queries is not None and queries[0][1]=='access_modifier' else ''}}>Access modifier</option>
                      <option value='is_abstract' {{'selected' if queries is not None and queries[0][1]=='is_abstract' else ''}}>Abstract</option>
                      <option value='is_static' {{'selected' if queries is not None and queries[0][1]=='is_static' else ''}}>Static</option>
                      <option value='is_final' {{'selected' if queries is not None and queries[0][1]=='is_final' else ''}}>Final</option>
                      <option value='annotation' {{'selected' if queries is not None and queries[0][1]=='annotation' else ''}}>Annotation</option>
                      <option value='extends_class' {{'selected' if queries is not None and queries[0][1]=='extends_class' else ''}}>Extends class</option>
                      <option value='implements_interfaces' {{'selected' if queries is not None and queries[0][1]=='implements_interfaces' else ''}}>Implements interface</option>
                      <option value='imports' {{'selected' if queries is not None and queries[0][1]=='imports' else ''}}>Imports</option>
                      <option value='package' {{'selected' if queries is not None and queries[0][1]=='package' else ''}}>Package</option>
                </select>
              </div>
              <label class="col-sm-1 col-form-label">Value</label>
              <div class="col-sm-3">
                <input type="text" class="form-control class_property_value" value={{queries[0][2] if queries is not None else ''}}></input>
              </div>
              <button id="button-remove" class="col-sm-1 button-remove" type="button" value="" onclick="removeProperty(this)"><i class="fas fa-ban"></i></i></button>
            </div>
            % if queries is not None:
            % for i in range(1, len(queries)):
            <div id="class-properties" class="form-group row">
              <div class="boolean-property col-sm-2">
                <select class="form-control boolean_property" value={{queries[i][0]}}>
                    <option value="and" {{'selected' if queries[i][0]=='and' else ''}}>and</option>
                    <option value="or" {{'selected' if queries[i][0]=='or' else ''}}>or</option>
                </select>
              </div>
              <label class="col-sm-2 col-form-label">Property</label>
              <div class="col-sm-3">
                <select class="form-control class_property">
                    <option value='class_name' {{'selected' if queries[i][1]=='class_name' else ''}}>Class name</option>
                    <option value='access_modifier' {{'selected' if queries[i][1]=='access_modifier' else ''}}>Access modifier</option>
                    <option value='is_abstract' {{'selected' if queries[i][1]=='is_abstract' else ''}}>Abstract</option>
                    <option value='is_static' {{'selected' if queries[i][1]=='is_static' else ''}}>Static</option>
                    <option value='is_final' {{'selected' if queries[i][1]=='is_final' else ''}}>Final</option>
                    <option value='annotation' {{'selected' if queries[i][1]=='annotation' else ''}}>Annotation</option>
                    <option value='extends_class' {{'selected' if queries[i][1]=='extends_class' else ''}}>Extends class</option>
                    <option value='implements_interfaces' {{'selected' if queries[i][1]=='implements_interfaces' else ''}}>Implements interface</option>
                    <option value='imports' {{'selected' if queries[i][1]=='imports' else ''}}>Imports</option>
                    <option value='package' {{'selected' if queries[i][1]=='package' else ''}}>Package</option>
                </select>
              </div>
              <label class="col-sm-1 col-form-label">Value</label>
              <div class="col-sm-3">
                <input type="text" class="form-control class_property_value" value={{queries[i][2]}} />
              </div>
              <button id="button-remove" class="col-sm-1 button-remove" type="button" value="" onclick="removeProperty(this)"><i class="fas fa-ban"></i></i></button>
            </div>
            % end
            % end
          </div>
          </fieldset>
          <input type="textarea" id="hidden_class_query" name="class_query" hidden>
          <input type="textarea" class="page" name="page" hidden value=1>
          <!-- <button type="submit" class="button-search btn btn-primary float-right">Submit</button> -->
          <label class="col-sm-1 col-form-label float-left">Sort</label>
          <select class="form-control col-sm-3 float-left" name="sort">
              <option value='stargazers_count:asc' {{'selected' if sort=='stargazers_count:asc' else ''}}>Stars (ascending)</option>
              <option value='stargazers_count:desc' {{'selected' if sort=='stargazers_count:desc' else ''}}>Stars (descending)</option>
              <option value='created_at:asc' {{'selected' if sort=='created_at:asc' else ''}}>Created at (ascending)</option>
              <option value='created_at:desc' {{'selected' if sort=='created_at:desc' else ''}}>Created at (descending)</option>
              <option value='open_issues_count:asc' {{'selected' if sort=='open_issues_count:asc' else ''}}>Open issues (ascending)</option>
              <option value='open_issues_count:desc' {{'selected' if sort=='open_issues_count:desc' else ''}}>Open issues (descending)</option>
              <option value='pushed_at:asc' {{'selected' if sort=='pushed_at:asc' else ''}}>Last commit (ascending)</option>
              <option value='pushed_at:desc' {{'selected' if sort=='pushed_at:desc' else ''}}>Last commit (descending)</option>
          </select>
          <button type="submit" class="button-search float-right" value=""><i class="fas fa-search"></i></button>
          <button type="button" onclick="addNewProperty('class')" class="button-search btn btn-primary float-right">Add property</button>
        </form>
      </div>
    </div>
    <div class="tab-pane fade {{'show active' if index=='interface' else ''}}" id="interface" role="tabpanel" aria-labelledby="pills-contact-tab">
      <div id="search-form">
        <form id="interface-property-search-form" class="property-search-form" action="/search-interface-properties" method="get" onsubmit="return createQuery(this, 'interface')">
          <fieldset>
            <legend>Query</legend>
            <div id="interface-fields">
              <div id="interface-properties" class="original-properties form-group row">
                <div class="boolean-property col-sm-2">
                  <select class="form-control boolean_property">
                      <option>and</option>
                      <option>or</option>
                  </select>
                </div>
                <label class="col-sm-2 col-form-label">Property</label>
                <div class="col-sm-3">
                  <select class="form-control interface_property">
                        <option value='interface_name' {{'selected' if queries is not None and queries[0][1]=='interface_name' else ''}}>Interface name</option>
                        <option value='access_modifier' {{'selected' if queries is not None and queries[0][1]=='access_modifier' else ''}}>Access modifier</option>
                        <option value='annotation' {{'selected' if queries is not None and queries[0][1]=='annotation' else ''}}>Annotation</option>
                        <option value='implements_interfaces' {{'selected' if queries is not None and queries[0][1]=='implements_interfaces' else ''}}>Implements interface</option>
                        <option value='imports' {{'selected' if queries is not None and queries[0][1]=='imports' else ''}}>Imports</option>
                        <option value='package' {{'selected' if queries is not None and queries[0][1]=='package' else ''}}>Package</option>
                  </select>
                </div>
                <label class="col-sm-1 col-form-label">Value</label>
                <div class="col-sm-3">
                  <input type="text" class="form-control interface_property_value" value={{queries[0][2] if queries is not None else ''}}></input>
                </div>
                <button id="button-remove" class="col-sm-1 button-remove" type="button" value="" onclick="removeProperty(this)"><i class="fas fa-ban"></i></i></button>
              </div>
              % if queries is not None:
              % for i in range(1, len(queries)):
              <div id="interface-properties" class="form-group row">
                <div class="boolean-property col-sm-2">
                  <select class="form-control boolean_property" value={{queries[i][0]}}>
                      <option value="and" {{'selected' if queries[i][0]=='and' else ''}}>and</option>
                      <option value="or" {{'selected' if queries[i][0]=='or' else ''}}>or</option>
                  </select>
                </div>
                <label class="col-sm-2 col-form-label">Property</label>
                <div class="col-sm-3">
                  <select class="form-control interface_property">
                      <option value='interface_name' {{'selected' if queries[i][1]=='interface_name' else ''}}>Interface name</option>
                      <option value='access_modifier' {{'selected' if queries[i][1]=='access_modifier' else ''}}>Access modifier</option>
                      <option value='annotation' {{'selected' if queries[i][1]=='annotation' else ''}}>Annotation</option>
                      <option value='implements_interfaces' {{'selected' if queries[i][1]=='implements_interfaces' else ''}}>Implements interface</option>
                      <option value='imports' {{'selected' if queries[i][1]=='imports' else ''}}>Imports</option>
                      <option value='package' {{'selected' if queries[i][1]=='package' else ''}}>Package</option>
                  </select>
                </div>
                <label class="col-sm-1 col-form-label">Value</label>
                <div class="col-sm-3">
                  <input type="text" class="form-control interface_property_value" value={{queries[i][2]}} />
                </div>
                <button id="button-remove" class="col-sm-1 button-remove" type="button" value="" onclick="removeProperty(this)"><i class="fas fa-ban"></i></i></button>
              </div>
              % end
              % end
            </div>
          </fieldset>
          <input type="textarea" id="hidden_interface_query" name="interface_query" hidden>
          <input type="textarea" class="page" name="page" hidden value=1>
          <!-- <button type="submit" class="button-search btn btn-primary float-right">Submit</button> -->
          <label class="col-sm-1 col-form-label float-left">Sort</label>
          <select class="form-control col-sm-3 float-left" name="sort">
              <option value='stargazers_count:asc' {{'selected' if sort=='stargazers_count:asc' else ''}}>Stars (ascending)</option>
              <option value='stargazers_count:desc' {{'selected' if sort=='stargazers_count:desc' else ''}}>Stars (descending)</option>
              <option value='created_at:asc' {{'selected' if sort=='created_at:asc' else ''}}>Created at (ascending)</option>
              <option value='created_at:desc' {{'selected' if sort=='created_at:desc' else ''}}>Created at (descending)</option>
              <option value='open_issues_count:asc' {{'selected' if sort=='open_issues_count:asc' else ''}}>Open issues (ascending)</option>
              <option value='open_issues_count:desc' {{'selected' if sort=='open_issues_count:desc' else ''}}>Open issues (descending)</option>
              <option value='pushed_at:asc' {{'selected' if sort=='pushed_at:asc' else ''}}>Last commit (ascending)</option>
              <option value='pushed_at:desc' {{'selected' if sort=='pushed_at:desc' else ''}}>Last commit (descending)</option>
          </select>
          <button type="submit" class="button-search float-right" value=""><i class="fas fa-search"></i></button>
          <button type="button" onclick="addNewProperty('interface')" class="button-search btn btn-primary float-right">Add property</button>
        </form>
      </div>
    </div>
    <div class="tab-pane fade {{'show active' if index=='enum' else ''}}" id="enum" role="tabpanel" aria-labelledby="pills-contact-tab">
      <div id="search-form">
        <form id="enum-property-search-form" class="property-search-form" action="/search-enum-properties" method="get" onsubmit="return createQuery(this, 'enum')">
          <fieldset>
            <legend>Query</legend>
            <div id="enum-fields">
              <div id="enum-properties" class="original-properties form-group row">
                <div class="boolean-property col-sm-2">
                  <select class="form-control boolean_property">
                      <option>and</option>
                      <option>or</option>
                  </select>
                </div>
                <label class="col-sm-2 col-form-label">Property</label>
                <div class="col-sm-3">
                  <select class="form-control enum_property">
                        <option value='enum_name' {{'selected' if queries is not None and queries[0][1]=='enum_name' else ''}}>Enum name</option>
                        <option value='access_modifier' {{'selected' if queries is not None and queries[0][1]=='access_modifier' else ''}}>Access modifier</option>
                        <option value='constants' {{'selected' if queries is not None and queries[0][1]=='constants' else ''}}>Constants</option>
                        <option value='annotation' {{'selected' if queries is not None and queries[0][1]=='annotation' else ''}}>Annotation</option>
                        <option value='implements_interfaces' {{'selected' if queries is not None and queries[0][1]=='implements_interfaces' else ''}}>Implements interface</option>
                        <option value='imports' {{'selected' if queries is not None and queries[0][1]=='imports' else ''}}>Imports</option>
                        <option value='package' {{'selected' if queries is not None and queries[0][1]=='package' else ''}}>Package</option>
                  </select>
                </div>
                <label class="col-sm-1 col-form-label">Value</label>
                <div class="col-sm-3">
                  <input type="text" class="form-control enum_property_value" value={{queries[0][2] if queries is not None else ''}}></input>
                </div>
                <button id="button-remove" class="col-sm-1 button-remove" type="button" value="" onclick="removeProperty(this)"><i class="fas fa-ban"></i></i></button>
              </div>
              % if queries is not None:
              % for i in range(1, len(queries)):
              <div id="enum-properties" class="form-group row">
                <div class="boolean-property col-sm-2">
                  <select class="form-control boolean_property" value={{queries[i][0]}}>
                      <option value="and" {{'selected' if queries[i][0]=='and' else ''}}>and</option>
                      <option value="or" {{'selected' if queries[i][0]=='or' else ''}}>or</option>
                  </select>
                </div>
                <label class="col-sm-2 col-form-label">Property</label>
                <div class="col-sm-3">
                  <select class="form-control enum_property">
                      <option value='enum_name' {{'selected' if queries[i][1]=='enum_name' else ''}}>Enum name</option>
                      <option value='access_modifier' {{'selected' if queries[i][1]=='access_modifier' else ''}}>Access modifier</option>
                      <option value='constants' {{'selected' if queries[i][1]=='constants' else ''}}>Constants</option>
                      <option value='annotation' {{'selected' if queries[i][1]=='annotation' else ''}}>Annotation</option>
                      <option value='implements_interfaces' {{'selected' if queries[i][1]=='implements_interfaces' else ''}}>Implements interface</option>
                      <option value='imports' {{'selected' if queries[i][1]=='imports' else ''}}>Imports</option>
                      <option value='package' {{'selected' if queries[i][1]=='package' else ''}}>Package</option>
                  </select>
                </div>
                <label class="col-sm-1 col-form-label">Value</label>
                <div class="col-sm-3">
                  <input type="text" class="form-control enum_property_value" value={{queries[i][2]}} />
                </div>
                <button id="button-remove" class="col-sm-1 button-remove" type="button" value="" onclick="removeProperty(this)"><i class="fas fa-ban"></i></i></button>
              </div>
              % end
              % end
            </div>
          </fieldset>
          <input type="textarea" id="hidden_enum_query" name="enum_query" hidden>
          <input type="textarea" class="page" name="page" hidden value=1>
          <!-- <button type="submit" class="button-search btn btn-primary float-right">Submit</button> -->
          <label class="col-sm-1 col-form-label float-left">Sort</label>
          <select class="form-control col-sm-3 float-left" name="sort">
              <option value='stargazers_count:asc' {{'selected' if sort=='stargazers_count:asc' else ''}}>Stars (ascending)</option>
              <option value='stargazers_count:desc' {{'selected' if sort=='stargazers_count:desc' else ''}}>Stars (descending)</option>
              <option value='created_at:asc' {{'selected' if sort=='created_at:asc' else ''}}>Created at (ascending)</option>
              <option value='created_at:desc' {{'selected' if sort=='created_at:desc' else ''}}>Created at (descending)</option>
              <option value='open_issues_count:asc' {{'selected' if sort=='open_issues_count:asc' else ''}}>Open issues (ascending)</option>
              <option value='open_issues_count:desc' {{'selected' if sort=='open_issues_count:desc' else ''}}>Open issues (descending)</option>
              <option value='pushed_at:asc' {{'selected' if sort=='pushed_at:asc' else ''}}>Last commit (ascending)</option>
              <option value='pushed_at:desc' {{'selected' if sort=='pushed_at:desc' else ''}}>Last commit (descending)</option>
          </select>
          <button type="submit" class="button-search float-right" value=""><i class="fas fa-search"></i></button>
          <button type="button" onclick="addNewProperty('enum')" class="button-search btn btn-primary float-right">Add property</button>
        </form>
      </div>
    </div>
    <div class="tab-pane fade {{'show active' if index=='method' else ''}}" id="method" role="tabpanel" aria-labelledby="pills-contact-tab">
      <div id="search-form">
        <form id="method-property-search-form" class="property-search-form" action="/search-method-properties" method="get" onsubmit="return createQuery(this, 'method')">
          <fieldset>
            <legend>Query</legend>
            <div id="method-fields">
              <div id="method-properties" class="original-properties form-group row">
                <div class="boolean-property col-sm-2">
                  <select class="form-control boolean_property">
                      <option>and</option>
                      <option>or</option>
                  </select>
                </div>
                <label class="col-sm-2 col-form-label">Property</label>
                <div class="col-sm-3">
                  <select class="form-control method_property">
                        <option value='method_name' {{'selected' if queries is not None and queries[0][1]=='method_name' else ''}}>Method name</option>
                        <option value='access_modifier' {{'selected' if queries is not None and queries[0][1]=='access_modifier' else ''}}>Access modifier</option>
                        <option value='is_abstract' {{'selected' if queries is not None and queries[0][1]=='is_abstract' else ''}}>Abstract</option>
                        <option value='is_static' {{'selected' if queries is not None and queries[0][1]=='is_static' else ''}}>Static</option>
                        <option value='is_final' {{'selected' if queries is not None and queries[0][1]=='is_final' else ''}}>Final</option>
                        <option value='return_type' {{'selected' if queries is not None and queries[0][1]=='return_type' else ''}}>Return Type</option>
                        <option value='input_type' {{'selected' if queries is not None and queries[0][1]=='input_type' else ''}}>Input type</option>
                        <option value='throws' {{'selected' if queries is not None and queries[0][1]=='throws' else ''}}>Throws</option>
                        <option value='annotation' {{'selected' if queries is not None and queries[0][1]=='annotation' else ''}}>Annotation</option>
                  </select>
                </div>
                <label class="col-sm-1 col-form-label">Value</label>
                <div class="col-sm-3">
                  <input type="text" class="form-control method_property_value" value={{queries[0][2] if queries is not None else ''}}></input>
                </div>
                <button id="button-remove" class="col-sm-1 button-remove" type="button" value="" onclick="removeProperty(this)"><i class="fas fa-ban"></i></i></button>
              </div>
              % if queries is not None:
              % for i in range(1, len(queries)):
              <div id="method-properties" class="form-group row">
                <div class="boolean-property col-sm-2">
                  <select class="form-control boolean_property" value={{queries[i][0]}}>
                      <option value="and" {{'selected' if queries[i][0]=='and' else ''}}>and</option>
                      <option value="or" {{'selected' if queries[i][0]=='or' else ''}}>or</option>
                  </select>
                </div>
                <label class="col-sm-2 col-form-label">Property</label>
                <div class="col-sm-3">
                  <select class="form-control method_property">

                      <option value='method_name' {{'selected' if queries[i][1]=='method_name' else ''}}>Method name</option>
                      <option value='access_modifier' {{'selected' if queries[i][1]=='access_modifier' else ''}}>Access modifier</option>
                      <option value='is_abstract' {{'selected' if queries[i][1]=='is_abstract' else ''}}>Abstract</option>
                      <option value='is_static' {{'selected' if queries[i][1]=='is_static' else ''}}>Static</option>
                      <option value='is_final' {{'selected' if queries[i][1]=='is_final' else ''}}>Final</option>
                      <option value='return_type' {{'selected' if queries[i][1]=='return_type' else ''}}>Return Type</option>
                      <option value='input_type' {{'selected' if queries[i][1]=='input_type' else ''}}>Input type</option>
                      <option value='throws' {{'selected' if queries[i][1]=='throws' else ''}}>Throws</option>
                      <option value='annotation' {{'selected' if queries[i][1]=='annotation' else ''}}>Annotation</option>
                  </select>
                </div>
                <label class="col-sm-1 col-form-label">Value</label>
                <div class="col-sm-3">
                  <input type="text" class="form-control method_property_value" value={{queries[i][2]}} />
                </div>
                <button id="button-remove" class="col-sm-1 button-remove" type="button" value="" onclick="removeProperty(this)"><i class="fas fa-ban"></i></i></button>
              </div>
              % end
              % end
            </div>
          </fieldset>
          <input type="textarea" id="hidden_method_query" name="method_query" hidden>
          <input type="textarea" class="page" name="page" hidden value=1>
          <!-- <button type="submit" class="button-search btn btn-primary float-right">Submit</button> -->
          <label class="col-sm-1 col-form-label float-left">Sort</label>
          <select class="form-control col-sm-3 float-left" name="sort">
              <option value='stargazers_count:asc' {{'selected' if sort=='stargazers_count:asc' else ''}}>Stars (ascending)</option>
              <option value='stargazers_count:desc' {{'selected' if sort=='stargazers_count:desc' else ''}}>Stars (descending)</option>
              <option value='created_at:asc' {{'selected' if sort=='created_at:asc' else ''}}>Created at (ascending)</option>
              <option value='created_at:desc' {{'selected' if sort=='created_at:desc' else ''}}>Created at (descending)</option>
              <option value='open_issues_count:asc' {{'selected' if sort=='open_issues_count:asc' else ''}}>Open issues (ascending)</option>
              <option value='open_issues_count:desc' {{'selected' if sort=='open_issues_count:desc' else ''}}>Open issues (descending)</option>
              <option value='pushed_at:asc' {{'selected' if sort=='pushed_at:asc' else ''}}>Last commit (ascending)</option>
              <option value='pushed_at:desc' {{'selected' if sort=='pushed_at:desc' else ''}}>Last commit (descending)</option>
          </select>
          <button id="test" type="submit" class="button-search float-right" value=""><i class="fas fa-search"></i></button>
          <button type="button" onclick="addNewProperty('method')" class="button-search btn btn-primary float-right">Add property</button>
        </form>
      </div>
    </div>
    <div class="tab-pane fade" id="variable" role="tabpanel" aria-labelledby="pills-contact-tab">
      <div id="search-form">
        <form id="variable-property-search-form" class="property-search-form" action="/search-variable-properties" method="get" onsubmit="return createQuery(this, 'variable')">
          <fieldset>
            <legend>Query</legend>
            <div id="variable-fields">
              <div id="variable-properties" class="original-properties form-group row">
                <div class="boolean-property col-sm-2">
                  <select class="form-control boolean_property">
                      <option>and</option>
                      <option>or</option>
                  </select>
                </div>
                <label class="col-sm-2 col-form-label">Property</label>
                <div class="col-sm-3">
                  <select class="form-control variable_property">
                        <option value='variable_name' {{'selected' if queries is not None and queries[0][1]=='variable_name' else ''}}>Variable name</option>
                        <option value='access_modifier' {{'selected' if queries is not None and queries[0][1]=='access_modifier' else ''}}>Access modifier</option>
                        <option value='variable_type' {{'selected' if queries is not None and queries[0][1]=='variable_type' else ''}}>Type</option>
                        <option value='is_static' {{'selected' if queries is not None and queries[0][1]=='is_static' else ''}}>Static</option>
                        <option value='is_final' {{'selected' if queries is not None and queries[0][1]=='is_final' else ''}}>Final</option>
                        <option value='annotation' {{'selected' if queries is not None and queries[0][1]=='annotation' else ''}}>Annotation</option>
                  </select>
                </div>
                <label class="col-sm-1 col-form-label">Value</label>
                <div class="col-sm-3">
                  <input type="text" class="form-control variable_property_value" value={{queries[0][2] if queries is not None else ''}}></input>
                </div>
                <button id="button-remove" class="col-sm-1 button-remove" type="button" value="" onclick="removeProperty(this)"><i class="fas fa-ban"></i></i></button>
              </div>
              % if queries is not None:
              % for i in range(1, len(queries)):
              <div id="variable-properties" class="form-group row">
                <div class="boolean-property col-sm-2">
                  <select class="form-control boolean_property" value={{queries[i][0]}}>
                      <option value="and" {{'selected' if queries[i][0]=='and' else ''}}>and</option>
                      <option value="or" {{'selected' if queries[i][0]=='or' else ''}}>or</option>
                  </select>
                </div>
                <label class="col-sm-2 col-form-label">Property</label>
                <div class="col-sm-3">
                  <select class="form-control variable_property">
                      <option value='variable_name' {{'selected' if queries[i][1]=='variable_name' else ''}}>Variable name</option>
                      <option value='access_modifier' {{'selected' if queries[i][1]=='access_modifier' else ''}}>Access modifier</option>
                      <option value='variable_type' {{'selected' if queries[i][1]=='variable_type' else ''}}>Type</option>
                      <option value='is_static' {{'selected' if queries[i][1]=='is_static' else ''}}>Static</option>
                      <option value='is_final' {{'selected' if queries[i][1]=='is_final' else ''}}>Final</option>
                      <option value='annotation' {{'selected' if queries[i][1]=='annotation' else ''}}>Annotation</option>
                  </select>
                </div>
                <label class="col-sm-1 col-form-label">Value</label>
                <div class="col-sm-3">
                  <input type="text" class="form-control variable_property_value" value={{queries[i][2]}} />
                </div>
                <button id="button-remove" class="col-sm-1 button-remove" type="button" value="" onclick="removeProperty(this)"><i class="fas fa-ban"></i></i></button>
              </div>
              % end
              % end
            </div>
          </fieldset>
          <input type="textarea" id="hidden_variable_query" name="variable_query" hidden>
          <input type="textarea" class="page" name="page" hidden value=1>
          <!-- <button type="submit" class="button-search btn btn-primary float-right">Submit</button> -->
          <label class="col-sm-1 col-form-label float-left">Sort</label>
          <select class="form-control col-sm-3 float-left" name="sort">
              <option value='stargazers_count:asc' {{'selected' if sort=='stargazers_count:asc' else ''}}>Stars (ascending)</option>
              <option value='stargazers_count:desc' {{'selected' if sort=='stargazers_count:desc' else ''}}>Stars (descending)</option>
              <option value='created_at:asc' {{'selected' if sort=='created_at:asc' else ''}}>Created at (ascending)</option>
              <option value='created_at:desc' {{'selected' if sort=='created_at:desc' else ''}}>Created at (descending)</option>
              <option value='open_issues_count:asc' {{'selected' if sort=='open_issues_count:asc' else ''}}>Open issues (ascending)</option>
              <option value='open_issues_count:desc' {{'selected' if sort=='open_issues_count:desc' else ''}}>Open issues (descending)</option>
              <option value='pushed_at:asc' {{'selected' if sort=='pushed_at:asc' else ''}}>Last commit (ascending)</option>
              <option value='pushed_at:desc' {{'selected' if sort=='pushed_at:desc' else ''}}>Last commit (descending)</option>
          </select>
          <button type="submit" class="button-search float-right" value=""><i class="fas fa-search"></i></button>
          <button type="button" onclick="addNewProperty('variable')" class="button-search btn btn-primary float-right">Add property</button>
        </form>
      </div>
    </div>
  </div>
</div>
{{!base}}
