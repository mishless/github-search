%rebase('search.tpl', query=query, queries=queries, index=index, sort=sort, page=page, max_pages=max_pages, total_results=total_results)
<div id="container" style="margin-bottom: 80px;">
  % if total_results > 10:
  <nav aria-label="...">
    <ul class="pagination">
      <li class="page-item {{'disabled' if page==1 else ''}}">
        <label for="external-submit" class="page-link" tabindex="-1" onclick="return requestNewPage('{{index}}', {{page-1}})" aria-disabled={{"true" if page==1 else "false"}}>Previous</label>
      </li>
      % if page-5 > 1:
        <li class="page-item">
          <label for="external-submit" class="page-link">...</label>
        </li>
      % end
      % for i in range(page-5, page + 6):
        % if i >= 1 and i <= max_pages:
          % if i == page:
            <li class="page-item active" aria-current="page">
              <label for="external-submit" class="page-link" onclick="return requestNewPage('{{index}}', {{i}})">{{i}}<span class="sr-only">(current)</span></label>
            </li>
          % else:
            <li class="page-item">
              <label for="external-submit" class="page-link" onclick="return requestNewPage('{{index}}', {{i}})">{{i}}</label>
            </li>
          % end
        % end
      % end
      % if page + 6 < max_pages:
        <li class="page-item" aria-current="page">
          <label for="external-submit" class="page-link">...</label>
        </li>
      % end
        <li class="page-item {{'disabled' if page==max_pages else ''}}">
        <label for="external-submit" class="page-link" onclick="return requestNewPage('{{index}}', {{page+1}})" aria-disabled={{"true" if page==max_pages else "false"}}>Next</label>
      </li>
    </ul>
    <button id="external-submit" type="submit" form="{{index}}-property-search-form" hidden>
  </nav>
  % end
  <span>Results: {{total_results}}</span>
  % for j, result in enumerate(results):
    <div class="result">
      <div class="result-title">
        <button class="btn btn-primary show-more" type="button" data-toggle="collapse" data-target="#collapseExample-{{j}}" aria-expanded="false" aria-controls="collapseExample">
          <i class="fas fa-chevron-down"></i>
        </button>
        <a href="{{result['url']}}">{{result['title']}}</a><br>
        <div class="result-title-info"><i style="color: khaki" class="fas fa-star"></i>{{result['stars_count']}}
          <i style="color: tomato" class="fas fa-exclamation-circle"></i>{{result['issues_count']}}</div>
      </div>
      % if 'snippet' in result:
        <div class="collapse" id="collapseExample-{{j}}">
          <div class="container-box">
            <pre>
              % for snippet in result['snippet']:
                <span>{{snippet}}</span>
              % end
            </pre>
          </div>
        </div>
      % end
    </div>
  % end
</div>
