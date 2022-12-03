function AddItem(product_id) {
    SendRequest("add", product_id);
    ChangeCount(product_id, +1);
}

function SubtractItem(product_id) {
    SendRequest("subtract", product_id);
    ChangeCount(product_id, -1);
}

function ChangeCount(product_id, num) {
    let count_tag = document.getElementById(`p-c-${product_id}`);
    if (count_tag) {
        let count_item = parseInt(count_tag.innerHTML);
        let count_final = count_item + num;
        count_tag.innerHTML = count_final;

        switch (count_final) {
            case 1:
                document.getElementById("subtract-product").innerHTML =
                    '<i class="fa-solid fa-trash"></i>';
                break;
            case 0:
                document.getElementById(
                    `g-b`
                ).innerHTML = `<button onclick="AddItem(${product_id})"  class="btn btn-success"><i class="fa-solid fa-plus"></i></a>`;
                break;
            default:
                document.getElementById("subtract-product").innerHTML =
                    '<i class="fa-solid fa-minus"></i>';
                break;
        }
    } else {
        document.getElementById(`g-b`).innerHTML = `
      
      <button onclick="SubtractItem(${product_id})" class="btn btn-danger" id="subtract-product">
            <i class="fa-solid fa-trash"></i>
      </button>
      <button class="btn btn-secondary" style="cursor: default;" id="p-c-${product_id}">1</button>
      <button onclick="AddItem(${product_id})"  class="btn btn-success"><i class="fa-solid fa-plus"></i></button>
      `;
    }
}
