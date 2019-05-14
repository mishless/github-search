const searchbox = document.querySelector('#searchbox');
const selectionOutput = document.getElementById('selection');

const tags = ['returns', 'access'];

// Fill in search box if a value is passed through the attribute
searchbox.innerText = searchbox.attributes.innertext.value;

function renderText(text) {
  tagTexts = tags.map((tag) => {return tag + ':'});
  regex = new RegExp(tagTexts.join('|'), 'g')
  return text.replace(regex, renderTag);
}

function renderTag(tag) {
  return '<span class="tagtext">' + tag + '</span>';
}

function submitOnEnter(e) {
  if (e.keyCode == 13) {
    e.preventDefault();
    document.querySelector('button[type="submit"]').click();
  }
}
searchbox.addEventListener('keydown', submitOnEnter);

function copyQuery() {
  document.getElementById('hiddenquery').value = searchbox.innerText;
  return true;
}

function createQuery(that, index) {
  booleanElements = that.getElementsByClassName("boolean_property")
  classProperties = that.getElementsByClassName(index + "_property")
  classPropertiesValues = that.getElementsByClassName(index + "_property_value")
  query = ''
  query += classProperties[0].value + ":"
  query += classPropertiesValues[0].value
  for (var i=1; i<booleanElements.length; i++) {
    query += ' '
    query += booleanElements[i].value
    query += ' '
    query += classProperties[i].value + ":"
    query += classPropertiesValues[i].value
  }
  document.getElementById("hidden_" + index + "_query").value = query
  return true;
}

function getTextSegments(element) {
  const textSegments = [];
  Array.from(element.childNodes).forEach((node) => {
    switch (node.nodeType) {
      case Node.TEXT_NODE:
        textSegments.push({text: node.nodeValue, node});
        break;

      case Node.ELEMENT_NODE:
        textSegments.splice(textSegments.length, 0, ...(getTextSegments(node)));
        break;

      default:
        throw new Error(`Unexpected node type: ${node.nodeType}`);
    }
  });
  return textSegments;
}

searchbox.addEventListener('input', updateSearchbox);

function updateSearchbox() {
  const sel = window.getSelection();
  const textSegments = getTextSegments(searchbox);
  const textContent = textSegments.map(({text}) => text).join('');
  let anchorIndex = null;
  let focusIndex = null;
  let currentIndex = 0;
  textSegments.forEach(({text, node}) => {
    if (node === sel.anchorNode) {
      anchorIndex = currentIndex + sel.anchorOffset;
    }
    if (node === sel.focusNode) {
      focusIndex = currentIndex + sel.focusOffset;
    }
    currentIndex += text.length;
  });

  searchbox.innerHTML = renderText(textContent);

  restoreSelection(anchorIndex, focusIndex);
}

function restoreSelection(absoluteAnchorIndex, absoluteFocusIndex) {
  const sel = window.getSelection();
  const textSegments = getTextSegments(searchbox);
  let anchorNode = searchbox;
  let anchorIndex = 0;
  let focusNode = searchbox;
  let focusIndex = 0;
  let currentIndex = 0;
  textSegments.forEach(({text, node}) => {
    const startIndexOfNode = currentIndex;
    const endIndexOfNode = startIndexOfNode + text.length;
    if (startIndexOfNode <= absoluteAnchorIndex &&
        absoluteAnchorIndex <= endIndexOfNode) {
      anchorNode = node;
      anchorIndex = absoluteAnchorIndex - startIndexOfNode;
    }
    if (startIndexOfNode <= absoluteFocusIndex &&
        absoluteFocusIndex <= endIndexOfNode) {
      focusNode = node;
      focusIndex = absoluteFocusIndex - startIndexOfNode;
    }
    currentIndex += text.length;
  });

  sel.setBaseAndExtent(anchorNode, anchorIndex, focusNode, focusIndex);
}
updateSearchbox();

function addNewProperty(index) {
    var timestamp = new Date().getUTCMilliseconds();
  	var newDiv = document.createElement('div');
  	newDiv.innerHTML = document.getElementById(index + '-properties').innerHTML;
    newDiv.setAttribute('class', 'form-group row');
    newDiv.setAttribute('id', index + '-properties-' + timestamp);
  	// append to our form, so that template data
  	//become part of form
  	document.getElementById(index + '-fields').appendChild(newDiv);
}

function removeProperty(that) {
  document.getElementById(that.parentElement.id).remove()
}

function requestNewPage(index, pageNumber) {
  form = document.getElementById(index.id + "-property-search-form")
  page = form.getElementsByClassName("page")
  page[0].value = pageNumber
  return true;
}
