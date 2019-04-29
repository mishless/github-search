%rebase('search.tpl', title=query, query=query)
<div id="container">
  %for result in results:
    <div class="result">
      <a href="{{result['url']}}">{{result['title']}}</a><br>
      %if 'snippet' in result:
      <code>
        {{result['snippet']}}
      </code>
      %end
    </div>
  %end
</div>
