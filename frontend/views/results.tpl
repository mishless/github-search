%rebase('search.tpl', title="CS - " + query, query=query)
<div id="container">
  %for result in results:
    <div class="result">
      <a href="{{result['url']}}">{{result['title']}}</a><br>
      %if 'snippet' in result:
      <div class="container-box">
      <pre>
        %for snippet in result['snippet']:
          <span>{{snippet}}</span>
        %end
      </pre>
      </div>
      %end
    </div>
  %end
</div>
