% rebase('base.tpl')
<!-- <header>
  <h1>GitHub Search</h1>
  <form action="/search" method="get" onsubmit="return copyQuery()">
    <div id="searchbox" placeholder="Search for code here" contenteditable="true" spellcheck="false" innerText="{{query}}"></div>
    <input type="textarea" id="hiddenquery" name="query" hidden>
    <button type="submit" value=""><i class="fas fa-search"></i></button>
  </form>
</header> -->
<div id='container'>
  <div id="nav-custom">
    <ul class="nav nav-pills mb-3 nav-fill navbar-dark" id="pills-tab" role="tablist">
      <li class="nav-item">
        <a class="nav-link active" id="pills-home-tab" data-toggle="pill" href="#code" role="tab" aria-controls="pills-home" aria-selected="true">Code</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" id="pills-home-tab" data-toggle="pill" href="#class" role="tab" aria-controls="pills-home" aria-selected="true">Class</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" id="pills-profile-tab" data-toggle="pill" href="#interface" role="tab" aria-controls="pills-profile" aria-selected="false">Interface</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" id="pills-contact-tab" data-toggle="pill" href="#enum" role="tab" aria-controls="pills-contact" aria-selected="false">Enum</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" id="pills-contact-tab" data-toggle="pill" href="#method" role="tab" aria-controls="pills-contact" aria-selected="false">Method</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" id="pills-contact-tab" data-toggle="pill" href="#variable" role="tab" aria-controls="pills-contact" aria-selected="false">Variable</a>
      </li>
    </ul>
  </div>
  <div class="tab-content" id="pills-tabContent">
    <div class="tab-pane fade show active" id="code" role="tabpanel" aria-labelledby="pills-home-tab">
      <form id="search-form" action="/search" method="get" onsubmit="return copyQuery()">
        <div id="searchbox" placeholder="Search for code here" contenteditable="true" spellcheck="false" innerText="{{query}}"></div>
        <input type="textarea" id="hiddenquery" name="query" hidden>
        <button id="button-submit" type="submit" value=""><i class="fas fa-search"></i></button>
      </form>
    </div>
    <div class="tab-pane fade" id="class" role="tabpanel" aria-labelledby="pills-profile-tab">Looking for class here</div>
    <div class="tab-pane fade" id="interface" role="tabpanel" aria-labelledby="pills-contact-tab">Looking for interface here</div>
    <div class="tab-pane fade" id="enum" role="tabpanel" aria-labelledby="pills-contact-tab">Looking for enum here</div>
    <div class="tab-pane fade" id="method" role="tabpanel" aria-labelledby="pills-contact-tab">Looking for method here</div>
    <div class="tab-pane fade" id="variable" role="tabpanel" aria-labelledby="pills-contact-tab">Looking for variable here</div>
  </div>
</div>
{{!base}}
