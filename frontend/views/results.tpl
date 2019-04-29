% rebase('search.tpl', title=query)
<a href="/recipes" id="backbutton">
  <i class="fas fa-arrow-left"></i>
</a>
<div id="container">
  % for result in results:
    <p>THIS IS A RESULT</p>
  % end
</div>
