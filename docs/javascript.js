const node = document.querySelector("#container"); 
const today = new Date().toISOString().split('T')[0];

fetch(`_data/result_${today}.json`)
  .then(resp => resp.json())
  .then(resp => {
    //node.textContent = JSON.stringify(resp, undefined, 2)
    const update_info = document.createElement('p');
    update_info.textContent = `本页面更新于：${today}`;
    node.appendChild(update_info);
    for (let location in resp) {
      const newDiv = document.createElement('div');
      const newSpan = document.createElement('span');
      newSpan.textContent = location;
      newDiv.appendChild(newSpan);

      const newUl = document.createElement('ul');
      for (let entry of resp[location]) {
        const newLi = document.createElement('li');
        newLi.textContent = entry;
        newUl.appendChild(newLi);
      }
      newDiv.appendChild(newUl);
      node.appendChild(newDiv);
    }
  });
