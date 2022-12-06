function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

function SendRequest(type, product_id) {
    return fetch("/cart/checkout/edit/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
            Accept: "application/json",

            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ type: type, product_id: product_id }),
    })
        .then((response) => {
            return response.json();
        });
    }
