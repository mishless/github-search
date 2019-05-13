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
      <form id="search-form" action="/search" method="get" onsubmit="return copyQuery()">
        <div id="searchbox" placeholder="Search for code here" contenteditable="true" spellcheck="false" innerText="{{query}}"></div>
        <input type="textarea" id="hiddenquery" name="query" hidden>
        <button id="button-submit" type="submit" value=""><i class="fas fa-search"></i></button>
      </form>
    </div>
    <div class="tab-pane fade {{'show active' if index=='class' else ''}}" id="class" role="tabpanel" aria-labelledby="pills-profile-tab">
      <div id="search-form">
        <form id="property-search-form" action="/search-class-properties" method="get" onsubmit="return createQuery(this)">
          <div id="class-fields">
            <div id="class-properties" class="original-class-properties form-group row">
              <div class="boolean-property col-sm-2">
                <select class="form-control boolean_property" name="boolean_property">
                    <option>and</option>
                    <option>or</option>
                </select>
              </div>
              <label class="col-sm-2 col-form-label">Property</label>
              <div class="col-sm-3">
                <select class="form-control class_property" name="class_property">
                    <option value='class_name'>Class name</option>
                    <option value='access_modifier'>Access modifier</option>
                    <option value='is_abstract'>Abstract</option>
                    <option value='is_static'>Static</option>
                    <option value='is_final'>Final</option>
                    <option value='annotation'>Annotation</option>
                    <option value='extends_class'>Extends class</option>
                    <option value='implements_interfaces'>Implements interface</option>
                    <option value='imports'>Imports</option>
                    <option value='package'>Package</option>
                </select>
              </div>
              <label class="col-sm-1 col-form-label">Value</label>
              <div class="col-sm-3">
                <input type="text" name="class_property_value" class="form-control class_property_value" />
              </div>
              <button id="button-remove" class="col-sm-1 button-remove" type="button" value="" onclick="removeProperty(this)"><i class="fas fa-ban"></i></i></button>
            </div>
          </div>
          <input type="textarea" id="hidden_class_query" name="class_query" hidden>
          <!-- <button type="submit" class="button-search btn btn-primary float-right">Submit</button> -->
          <button type="submit" class="button-search float-right" value=""><i class="fas fa-search"></i></button>
          <button type="button" onclick="addNewProperty()" class="button-search btn btn-primary float-right">Add property</button>
        </form>
      </div>
    </div>
    <div class="tab-pane fade" id="interface" role="tabpanel" aria-labelledby="pills-contact-tab">Looking for interface here</div>
    <div class="tab-pane fade" id="enum" role="tabpanel" aria-labelledby="pills-contact-tab">Looking for enum here</div>
    <div class="tab-pane fade" id="method" role="tabpanel" aria-labelledby="pills-contact-tab">Looking for method here</div>
    <div class="tab-pane fade" id="variable" role="tabpanel" aria-labelledby="pills-contact-tab">Looking for variable here</div>
  </div>
</div>
{{!base}}
