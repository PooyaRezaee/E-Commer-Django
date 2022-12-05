function AddItem(product_id) {
    SendRequest("add", product_id)
    .then((data) => {
        switch (data['status']) {
            case 'ok':
                ChangeCount(product_id, +1);
                break;
            default:
                // TODO disable button
                break;
        }
    });
}

function SubtractItem(product_id) {
    SendRequest("subtract", product_id)
    .then((data) => {
        if (data['status'] == 'ok'){
            ChangeCount(product_id, -1);
        }
    });
}

function ChangeCount(product_id, num) {
    let count_tag = document.getElementById(`p-c-${product_id}`);
    let price_product = parseInt(
        document.getElementById(`p-p-${product_id}`).innerHTML.replace(",", "")
    );
    let count_item = parseInt(count_tag.innerHTML);
    let count_final = count_item + num;
    count_tag.innerHTML = count_final;

    switch (count_final) {
        case 1:
            document.getElementById(`subtract-${product_id}`).innerHTML =
                '<i class="fa-solid fa-trash"></i>';
            break;
        case 0:
            document.getElementById(`t-${product_id}`).style.display = "none";
            break;
        default:
            document.getElementById(`subtract-${product_id}`).innerHTML =
                '<i class="fa-solid fa-minus"></i>';
            break;
    }

    ChangePrice(num == 1 ? price_product : -price_product);
}

function ChangePrice(diff) {
    const formatter = new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD",
    });

    let total_price_tag = document.getElementById("total-price");
    let total_final =
        parseFloat(total_price_tag.innerHTML.replace(",", "")) +
        parseFloat(diff);
    total_price_tag.innerHTML = formatter
        .format(total_final)
        .toString()
        .replace("$", "");
    
    DisplayPaymentBtn()
}

function DisplayPaymentBtn() {
    let total_price = document.getElementById("total-price").innerHTML;
    if (parseInt(total_price) == 0) {
        document.getElementById("p-btn").style.display = "none";
    }
}