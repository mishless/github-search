% rebase('base.tpl')
<header>
  <h1>Github Search</h1>
  <form action="/search" method="get" onsubmit="return copyQuery()">
    <div id="searchbox" placeholder="Search for code here" contenteditable="true" spellcheck="false" innerText={{query}}></div>
    <input type="textarea" id="hiddenquery" name="query" hidden>
    <button type="submit" value=""><i class="fas fa-search"></i></button>
  </form>
</header>
{{!base}}
