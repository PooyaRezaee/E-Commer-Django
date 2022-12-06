btn_pay = document.getElementById('btn-pay')
way_pay = null

events = [
    'paytest',
    // 'paypal'
]
addEvents(events)

function ChangeWayPay(id) { 
    ways = document.getElementsByClassName('way-pay')
    for (const way of ways) {
        id_way = way.id
        if (id_way==id) {
            way.classList.remove('bg-white')
            way.classList.add('bg-warning')
            btn_pay.disabled = false
            way_pay = id
        }else{
            way.classList.remove('bg-warning')
            way.classList.add('bg-white')
        }
    }
 }

function addEvents(array) { 
    for (const key of array) {
        document.getElementById(key).addEventListener('click',() => ChangeWayPay(key))
    }
}

document.getElementById('btn-pay').onclick = function() { 
    window.location.href = `pay/?way=${way_pay}`
}